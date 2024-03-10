def solution(args):
    splitted_args = args.split("\n")
    a, b = map(int, splitted_args[0].split(" "))
    x, y, direction = map(int, splitted_args[1].split(" "))
    game_map = [[0] * a for _ in range(a)]
    for i in range(a):
        line = map(int, splitted_args[2:][i].split(" "))
        game_map[i] = list(line)

    visited = [[0] * a for _ in range(a)]
    visited[x][y] = 1 #처음 방문한 곳을 표시한다

    #북 동 남 서
    #0 1 2 3
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    count = 1
    turn_count = 0
    while True:
        direction = turn_left(direction)
        turn_count += 1

        new_x = x + dx[direction]
        new_y = y + dy[direction]

        if visited[new_x][new_y] == 0 and game_map[new_x][new_y] == 0:
            visited[new_x][new_y] = 1
            x = new_x
            y = new_y
            count += 1
            turn_count = 0
            continue

        if turn_count == 4:
            x_back = x - dx[direction]
            y_back = y - dy[direction]
            if game_map[x_back][y_back] == 0:
                x = x_back
                y = y_back
                turn_count = 0
            else:
                break
    return count

def turn_left(direction):
    direction -= 1
    if direction == -1:
        direction = 3
    return direction


print(solution("4 4\n1 1 0\n1 1 1 1\n1 0 0 1\n1 1 0 1\n1 1 1 1"))

#초기화
# 맵 세팅
# 캐릭터 위치, 방향 설정
#캐릭터 멈추기 전까지 행동 반복
# 회전, 체크, (이동)
# 이동 시 카운트+, 들른 자리 표시
#캐릭터 멈춘 후 카운트 반환
#북 동 남 서
#0 1 2 3
#캐릭터가 들른 위치를 어떻게 저장해야할까?
#현재 방향에서 왼쪽으로 회전 시 방향값은 일일이 조건문으로 계산?
