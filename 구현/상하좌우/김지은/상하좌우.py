# 5
# R R R U D D
n = int(input()) # 공간의 크기
x, y = 1, 1
movement = input().split()

for i in movement:
    if i == 'R':
        if (y+1) > n:
            continue
        y += 1
        continue
    if i == 'L':
        if (y-1) < 1:
            continue
        y -= 1
        continue
    if i == 'U':
        if x-1 < 1:
            continue
        x -= 1
        continue
    if i == 'D':
        if (x+1) > n:
            continue
        x += 1
print(x, y)

