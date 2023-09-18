def find_constructor(N):
    result = N
    while N != 0:
        N = int(N)
        result += (N % 10)
        N /= 10
        N = int(N)  
    return result
N = int(input())
printVal = 0
for i in range(0, N):
    if find_constructor(i) == N:
        print(i)
        printVal = 1
        break
if printVal == 0:
    print(0)