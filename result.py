import functools
import os

"""
decorator classes for showing different function statistics
"""


class ProgressBar:
    def __init__(self) -> None:
        pass

    def __str__(self) -> str:
        return "ProgressBar obj"

    def test(self, func):
        functools.wraps(func)

        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            print(func.__name__, f"{func.__name__!r}")
        return wrapper

    def simple(self, func):
        """
        Simple ProgressBar covering fill scale of terminal width.
        recieves generator from function and passes along the method.
        best for known length operations!!!
        """
        functools.wraps(func)

        def wrapper(*args, **kwargs):
            func_generator = func(*args, **kwargs)
            total = len(func_generator)
            for i, e in enumerate(func_generator):
                percentage = (i+1)/total
                col, row = os.get_terminal_size()
                success_width = int(percentage*col)
                result_line = f"{e} > "+("*"*success_width).ljust(col, "-")
                print(result_line, end="\r")
            print()
            return wrapper



if __name__=="__main__":
    n = 1*10**5
    r = ProgressBar()

    # make print line
    @r.simple
    def p(n):
        return (i for i in range(n))

    p()
