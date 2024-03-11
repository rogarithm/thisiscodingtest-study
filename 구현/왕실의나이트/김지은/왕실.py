# print(ord("a"))
# print(ord("c"))
start = input() # 현재 나이트의 위치 str c2 이면, c가 열 2가 행이다. (2,3)

row = int(start[1])
column = (ord(start[0]) - ord("a") + 1)

dx = [1, 1, 2, 2, -1, -1, -2, -2]
dy = [2,-2,-1, 1, -2, 2, -1, 1]

nx = 0
ny = 0
answer = 0

for i in range(8):
    nx = row + dx[i]
    ny = column + dy[i]
    if nx < 1 or ny < 1 or ny > 8 or ny > 8:
        continue
    answer += 1

print(answer)


