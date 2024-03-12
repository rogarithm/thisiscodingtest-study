from collections import deque

N, M = map(int, input().split())

maze = []
for _ in range(N):
    maze.append(list(map(int, input())))

visited = [[0 for _ in range(M)] for _ in range(N)]
directions = [[0,1], [1,0], [-1,0], [0,-1]]

def bfs(y, x):
    q = deque()
    q.append((y,x))

    while q:
        y, x = q.popleft()

        for dy, dx in directions:
            ny = y + dy
            nx = x + dx

            if 0 <= ny < N and 0 <= nx < M:
                if maze[ny][nx] == 1:
                    maze[ny][nx] = maze[y][x] + 1
                    q.append((ny, nx))

    return maze[-1][-1]

print(bfs(0, 0)) 