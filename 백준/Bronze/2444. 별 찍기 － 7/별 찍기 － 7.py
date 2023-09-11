N = int(input())
for i in range(0, N+1):
    for j in range(0, N-i):
        if i == 0:
            continue
        print(" ", end="")
    for k in range(0, i*2-1):
        print("*", end="")
    if i != 0:
        print("")
for i in range(N-1, 0, -1):
    for j in range(0, N-i):
        print(" ", end="")
    for k in range(0, i*2-1):
        print("*", end="")
    print("")