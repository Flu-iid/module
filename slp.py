from time import sleep
import os


class Slp():
    def __init__(self, t: float = 0.2, delay_time: float = 1):
        self.t = t
        self.delay_time = delay_time
        self.shapes = ["|", "/", "-", "\\"]

    def __str__(self):
        return "<singleLinePrinter Object>"

    def next_shape(self, s: str = "-", shapes=[]) -> str:
        shapes = self.shapes if len(shapes) == 0 else shapes
        current_shape = s[0]
        next_shape = shapes[(shapes.index(current_shape)+1) % len(shapes)]
        return s.replace(current_shape, next_shape)

    def single_line_printer(self, s: str) -> None:
        all_time = self.delay_time + len(s)*self.t
        current_string = "- "
        while all_time > 0:
            current_string = Slp.next_shape(current_string)
            current_string += s[0] if s else ""
            s = s[1:]
            print(current_string, end="\r")
            sleep(self.t)
            all_time -= self.t

    def empty_cursor(self, total_time: int = 2):
        starting_s = "-"
        while total_time+self.delay_time > 0:
            print(starting_s, end="\r")
            sleep(self.t)
            total_time -= self.t
            starting_s = self.next_shape(starting_s)
        print(os.get_terminal_size().columns*"-")


if __name__ == "__main__":
    Slp().empty_cursor()
