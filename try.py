def gcd(f, s):
    maximum = max(f, s)
    minimum = min(f, s)
    sisa = maximum % minimum
    while sisa != 0:
        maximum = minimum
        minimum = sisa
        sisa = maximum % minimum
    return minimum


print(gcd(10, 45))
