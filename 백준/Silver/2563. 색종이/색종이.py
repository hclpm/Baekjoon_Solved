N = int(input())
canvas = [[0 for i in range(100)]for j in range(100)]
area = 0

for i in range(0, N):       #N번 반복
    x_axis, y_axis = input().split()  #색종이 좌측 하단 좌표 입력(색종이 크기는 10)
    x_axis = int(x_axis)
    y_axis = int(y_axis)
    for x in range(x_axis, x_axis+10):
        for y in range(y_axis, y_axis+10):
            canvas[x][y] = 1

for i in range(0, 100):
    for j in range(0, 100):
        if canvas[i][j] == 1:
            area += 1
print(area)