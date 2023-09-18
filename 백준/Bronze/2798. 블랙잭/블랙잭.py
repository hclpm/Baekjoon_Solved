N, M = input().split()
N = int(N)
M = int(M)
inputArr = input().split()
numArr = []
for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            numArr.append(int(inputArr[i]) + int(inputArr[j]) + int(inputArr[k]))
diff = 300000000
result = 0
for i in range(len(numArr)):
    if (M - numArr[i] < diff) and (M >= numArr[i]):
        diff = abs(M - numArr[i])
        result = numArr[i]
print(result)