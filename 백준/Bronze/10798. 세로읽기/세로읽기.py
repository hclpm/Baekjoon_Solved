printArr = [[0] for i in range(0, 5)]
maxLen = 0
for i in range(0, 5):
    strInput = input()
    if len(strInput) > maxLen:
        maxLen = len(strInput)
    for j in range(0, len(strInput)):
        printArr[i].append(strInput[j])

for i in range(0, 5):
    del printArr[i][0]
    if len(printArr[i]) < maxLen:
        for j in range(0, maxLen - len(printArr[i])):
            printArr[i].append(" ")

for i in range(0, maxLen):
    for j in range(0, 5):
        if printArr[j][i] != " ":
            print(printArr[j][i], sep="", end="")