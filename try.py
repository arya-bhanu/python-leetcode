def countDigitNumber(n) -> int:
    if n == 0:
        return 1
    length = 0
    while n != 0:
        n = n // 10
        length += 1
    return length


print(countDigitNumber(12))
