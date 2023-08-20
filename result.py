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
        recieves a sequence from function.
        best to use for known length sequences!!!
        """
        functools.wraps(func)

        def wrapper(*args, **kwargs):
            try:
                func_sequence = list(func(*args, **kwargs))
                total = len(func_sequence)
            except:
                print("ERROR > bad sequence given")

            for i, e in enumerate(func_sequence):
                col, row = os.get_terminal_size()
                show = f"{i, e} > "
                bar_length = col - len(show)
                completition = int((i+1)/total*bar_length)
                print(show, ("*"*completition).ljust(bar_length, "-"),
                      sep="", end="\r")
            print("Done!")

        return wrapper

    # add function for simpl wait and seperated total length for generators


if __name__ == "__main__":
    n = 1*10**5
    r = ProgressBar()

    @r.simple
    def p(n):
        return range(n)

    p(10**5)
