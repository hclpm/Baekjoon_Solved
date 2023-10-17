number = input()
a = []
for i in range(int(number)):
    strVal = input()
    a.append(strVal)

val = 0
for i in range(len(a[0])):
    for j in range(int(number)):
        if a[0][i] != a[j][i]:
            val = 1
    if val == 0:
        print(a[0][i], sep="", end="")
    else:
        print("?", sep="", end="")
        val = 0