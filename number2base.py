def n2b(number: int, base: int):
    output = ""
    while number >= 1:
        output += str(number % base)
        number = number // base
    return output[::-1]
