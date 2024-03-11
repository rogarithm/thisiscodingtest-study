N, M = map(int, input().split())

arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

# N, M = 4, 5
# arr = [
#     [0,0,1,1,0],
#     [0,0,0,1,1],
#     [1,1,1,1,1],
#     [0,0,0,0,0]
# ]

def dfs(y, x):
    global cnt
        
    if 0 <= y < N and 0 <= x < M:
        if arr[y][x] == 0 :
            arr[y][x] = 1
            dfs(y-1, x)
            dfs(y, x-1)
            dfs(y+1, x)
            dfs(y, x+1)
            return True
    return False



count = 0
for j in range(N):
    for i in range(M):
        if dfs(j, i):
            count += 1
print(count)


