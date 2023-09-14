a, b = input().split()
a = int(a)
b = int(b)
arr1 = []
arr2 = []
for i in range(0, a):
    iNum = input().split()
    arr1.append(iNum)
for i in range(0, a):
    iNum = input().split()
    arr2.append(iNum)
for i in range(0, a):
    for j in range(0, b):
        print(int(arr1[i][j]) + int(arr2[i][j]), end= " ")
    print()