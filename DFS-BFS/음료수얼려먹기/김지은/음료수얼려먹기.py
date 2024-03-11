from collections import deque

# 직접 1로 바꾸게 되면,
N, M = map(int, input().split()) # 세로/가로 길이 4, 5

arr = [list(map(int, input()))for i in range(N)]
#visited = [[False]*M for i in range(N)]
# 상, 하, 좌, 우 로 붙어 있는 경우 == 연결 되어 있다.

answer = 0
#상, 좌, 우, 하
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
queue = deque()

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            arr[i][j] = 1
            queue.append((i, j))
            while queue:
                cur_x, cur_y = queue.popleft()
                for k in range(4):
                    nx = cur_x + dx[k]
                    ny = cur_y + dy[k]
                    if 0<=nx<N and 0<=ny<M and arr[nx][ny] == 0:
                        queue.append((nx, ny))
                        arr[nx][ny] = 1
            answer += 1
print(answer)

# 수요일: 미로 탈출
# 금 게임 맵 최단거리
# 토 퍼즐 조각
# 일 릿코드 https://leetcode.com/problems/minimum-genetic-mutation/description/?envType=study-plan-v2&envId=top-interview-150
