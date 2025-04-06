a = "00101101"

lenA = len(a)

ansR = [0] * lenA
ansL = [0] * lenA

finalAns = []

# left
ballCount = 0
for i in range(lenA - 1, 0, -1):
    if a[i] == "1":
        ballCount += 1
    ansL[i - 1] = ansL[i] + ballCount

# right
ballCount = 0
for i in range(0, lenA - 1):
    if a[i] == "1":
        ballCount += 1
    ansR[i + 1] = ansR[i] + ballCount
    finalAns.append(ansR[i] + ansL[i])

finalAns.append(ansR[-1])

print(finalAns)
