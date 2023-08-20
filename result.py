import functools
import os

"""
decorator classes for showing different function statistics
"""


class ProgressBar:
    def __init__(self) -> None:
        # add shapes and customizations here
        pass

    def __str__(self) -> str:
        return "ProgressBar obj"

    def test(self, func):
        @functools.wraps(func)
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
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                func_sequence = list(func(*args, **kwargs))
                total = len(func_sequence)
            except:
                print("ERROR > bad sequence given")

            for i, e in enumerate(func_sequence):
                col, row = os.get_terminal_size()
                show_start = f"{i, e} > "
                show_end = ""
                bar_length = col - len(show_start) - len(show_end)
                completition = int((i+1)/total*bar_length)
                print(show_start, ("*"*completition).ljust(bar_length, "-"), show_end,
                      sep="", end="\r")
            print("Done!")

        return wrapper

    # add function for simple wait and seperated total length for generators

    def gen_known(self, length):
        """
        decorator accepting generator-returned function with long known length in generator
        but length calculated by user.
        """
        def gen(func):
            @functools.wraps(func)
            def wrapper(*args, **kwargs):
                func_generator = func(*args, **kwargs)
                loops = 0
                while True:
                    try:
                        o = next(func_generator)
                        loops += 1
                        col, row = os.get_terminal_size()
                        print(f"{o}"[:col*(row-2)].ljust(col*(row-2), " "))
                        show_start = f"{loops} | {length} > "
                        show_end = ""
                        bar_length = col - len(show_start) - len(show_end)
                        completition = int((loops+1)/length*bar_length)
                        print(show_start, ("*"*completition).ljust(bar_length, "-"), show_end,
                              sep="", end="\r")
                    except StopIteration | EOFError:
                        if loops > length:
                            print("LENGTH calculated wrong")
                        print("Done")
                        break
                return wrapper
            return gen

    def gen_uknown(self, func):
        """
        decorator accepting generator-returned function 
        with long unknown length in generator.
        use with caution!!!
        """
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_generator = func(*args, **kwargs)
            loops = 0
            while True:
                # try:
                o = next(func_generator)
                loops += 1
                col, row = os.get_terminal_size()
                print(f"{o}"[:col*(row-2)].ljust(col*(row-2), " "))
                show_start = f"{loops} > "
                show_end = ""
                bar_length = col - len(show_start) - len(show_end)
                completition = int((loops+1)/length*bar_length)
                print(show_start, ("*"*completition).ljust(bar_length, "-"), show_end,
                      sep="", end="\r")
                # needs different shapes. probably from slp lib

            # needs redundency


if __name__ == "__main__":
    n = 1*10**5
    r = ProgressBar()

    @r.simple
    def p():
        # dummy function
        return range(n)

    p()
