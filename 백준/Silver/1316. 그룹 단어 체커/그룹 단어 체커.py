N = int(input())

for i in range(0, N):
    s = input()
    sArr = []
    cntArr = []
    for i in range(0, len(s)):
        sArr.append(s[i])
    curr_letter = ''
    prev_letter = ''
    for i in range(0, len(sArr)):
        curr_letter = sArr[i]
        if curr_letter != prev_letter:
            if curr_letter in cntArr:
                N -= 1
                break
            else:
                cntArr.append(curr_letter)
        prev_letter = curr_letter

print(N)