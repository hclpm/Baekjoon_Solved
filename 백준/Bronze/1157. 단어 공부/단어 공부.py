str1 = input()
arr = []
abc = []
count = []

for i in range(0, len(str1)):
    arr.append(str1[i].upper())

for char in arr:
    if char in abc:
        count[abc.index(char)] += 1
    else:
        abc.append(char)
        count.append(1)

cnt = 0
for i in range(0, len(count)):
    if count[i] == max(count):
        cnt += 1

printLetter = abc[count.index(max(count))]
if cnt > 1:
    print("?")
elif cnt == 1:
    print(printLetter)