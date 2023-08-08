def num2roman(n: int):
    tmp = str(n)
    d = {(1, 0): "I",
         (5, 0): "V",
         (1, 1): "X",
         (5, 1): "L",
         (1, 2): "C",
         (5, 2): "D",
         (1, 3): "M"
         }
    m = len(tmp) - 1
    output = ""
    while m > 0:
        s = tmp[0]

        tmp = tmp[1:]
        m -= 1
