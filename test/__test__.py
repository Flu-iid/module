import keyword


def n2b(n: int, b: int):
    o = ""
    while n >= 1:
        o += str(n % b)
        n = n // b
    return o[::-1]


def b2n(n: str):
    base = int(n[0])
    s = n[2:]
    o = 0
    for i, c in enumerate(s[::-1]):
        o += int(c)*base**(i)
    return o


# print(n2b(4, 2))
# print(b2n("2b100"))

# complete and publish these

# practice roman conversion
