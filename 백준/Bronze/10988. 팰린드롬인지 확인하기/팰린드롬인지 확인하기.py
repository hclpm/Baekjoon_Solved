s1 = input()
s1Size = len(s1)
Val = 0

for i in range(0, s1Size - 1):
    if s1[i] != s1[s1Size-i -1]:
        Val += 1

if Val > 0:
    print("0")
elif Val == 0:
    print("1")