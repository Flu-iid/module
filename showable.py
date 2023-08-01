import os


class Showable():
    def __init__(self, att: list, rows: list, title_space: int = 20) -> None:

        self.width, self.height = os.get_terminal_size()
        self.att = att
        self.rows = rows
        self.space = title_space if self.width / \
            len(att) > title_space else self.width//len(att)
        for row in self.rows:
            if len(self.att) > len(row):
                row += [None for _ in range(len(self.att)-len(row))]
            if len(row) > len(self.att):
                self.att += [None for _ in range(len(row)-len(self.att))]

    def __str__(self):
        return "<Showable object>"

    def titler(self, title: str):
        try:
            title = str(title)
        except:
            title = "badInput"
        ws = self.space - len(title) if self.space > len(title) else 0
        if ws % 2:  # if odd
            left_deli = ws//2 + 1
            right_deli = ws//2
            return left_deli*" "+title+right_deli*" "
        else:  # if even
            deli = ws//2
            return deli*" "+title+deli*" "

    def show(self, common_row: str = "-", common_col: str = " ", title_row: str = "+", title_col: str = "|"):
        """change values for more diverce table"""

        def seperator_row(self, token: str = common_row):
            for i in range(len(self.att)):
                print(self.space*common_row, end="")
                if i+1 == len(self.att):
                    print()
                else:
                    print(token, end="")

        for i, title in enumerate(self.att):
            print(Showable.titler(self, title), end="")
            if i+1 == len(self.att):
                print()
            else:
                print(title_col, end="")
        seperator_row(self, title_row)  # title under seperator
        for j, row in enumerate(self.rows):
            for i, r in enumerate(row):
                print(Showable.titler(self, r), end="")
                if i+1 == len(row):
                    print()
                else:
                    print(common_col, end="")
            if j+1 != len(self.rows):
                seperator_row(self)  # rows under seperator


if __name__ == "__main__":
    Showable([1, 2, 3, 4], [[1, 2, 3], [1, 2, 3, 4], []]).show(common_col="&")
