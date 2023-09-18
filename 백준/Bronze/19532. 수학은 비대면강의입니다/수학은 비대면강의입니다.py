a, b, c, d, e, f = input().split()
a = int(a); b = int(b); c = int(c); d = int(d); e = int(e); f = int(f)
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y == f:
            print(x, end=" ")
            print(y)