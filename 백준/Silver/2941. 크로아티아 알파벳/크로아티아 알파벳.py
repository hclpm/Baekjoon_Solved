str1 = input()
arr = []
for char in str1:
    arr.append(char)

prev_prev_letter = ""
prev_letter = ""
curr_letter = ""
cnt = len(arr)
arr.append("")

for i in range(0, len(arr)):
    prev_prev_letter = prev_letter
    prev_letter = curr_letter
    curr_letter = arr[i]
    # print(curr_letter + " -> " + prev_letter + " -> " + prev_prev_letter)
    if curr_letter == "=":
        if prev_letter == "c" or prev_letter == "s":
            cnt -= 1
            # print("=c/=s")
        elif prev_letter == "z":
            if prev_prev_letter == "d":
                cnt -= 2
                # print("=zd")
            else:
                cnt -= 1
                # print("=z")
    elif curr_letter == "-":
        if prev_letter == "c" or prev_letter == "d":
            cnt -= 1
            # print("-c/-d")
    elif curr_letter == "j":
        if prev_letter == "l" or prev_letter == "n":
            cnt -= 1
            # print("jl/jn")

print(cnt)