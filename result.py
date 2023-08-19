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
        """
        functools.wraps(func)

        def wrapper(*args, **kwargs):
            pctg = func(*args, **kwargs)
            col, row = os.get_terminal_size()
            success_width = int(pctg*col)
            result_line = ("*"*success_width).ljust(col, "-")
            print(result_line, end="\r")
        return wrapper


n = 1*10**5
r = ProgressBar()

for i in range(n):
    @r.simple
    def p_line(i, n):
        return i/n

    p_line(i, n)
