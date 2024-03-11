n, m = map(int, input().split())

y, x, head = map(int, input().split())

arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]

dy = [-1, 0, 1,  0]
dx = [ 0, 1, 0, -1]

def turn_left():
    global head
    head -= 1
    if head == -1:
        head = 3


turn_count = 0
num_visited = 1
while True: 

    turn_left()
    
    ny = y + dy[head]
    nx = x + dx[head]
    
    # 방문 가능하다면,
    if arr[ny][nx] == 0 and not visited[ny][nx]:
        y = ny
        x = nx
        visited[y][x] = 1
        turn_count = 0
        num_visited += 1
        continue
    else:
        turn_left()
        turn_count += 1
    
    # 종료 조건: 네 방향 모두 갈 수 없을 때(바다 또는 이미 가본 칸) + 뒤쪽 방향이 바다인 칸
    if turn_count == 4:
        ny = y - dy[head]
        nx = x - dx[head]

        if arr[ny][nx] == 1: # 뒤쪽 방향이 바다
            break
        else:
            y = ny
            x = ny
            turn_count = 0



print(num_visited)
