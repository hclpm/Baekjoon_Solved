arr1 = []
arr2 = []
printed = 0
for i in range(0, 9):
    iNum = input().split()
    arr1.append(iNum)
for i in range(0, 9):
    for j in range(0, 9):
        arr2.append(int(arr1[i][j]))
maxVal = max(arr2)
for i in range(0, 9):
    for j in range(0, 9):
        if int(arr1[i][j]) == maxVal:
            if printed == 0:
                print(maxVal)
                print(i+1, end= " ")
                print(j+1)
                printed = 1