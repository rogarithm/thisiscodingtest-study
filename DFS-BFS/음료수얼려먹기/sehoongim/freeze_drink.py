# dfs로 풀려면 얼음 틀을 어떻게 나타내야 할까?
# 언제 탐색을 멈춰야 할까?
# 방문한 칸인지를 어떻게 표시할까?
# 하나의 아이스크림으로 만들 수 있는 덩어리를 어떻게 구분할까?

def freeze_drink():
 #n, m = 3, 3
 #ice_tray = [[0,0,1],
 #            [0,0,0],
 #            [1,1,1]
 #           ] 
 n, m = 4, 5 #세로 4, 가로 5
 ice_tray = [[0,0,1,1,0],
             [0,0,0,1,1],
             [1,1,1,1,1],
             [0,0,0,0,0]
             ]

 ice_cream_count = 0
 # 탐색을 어떻게 해야 할까?
 # ice_try[0][0]부터 ice_tray[n-1][m-1]까지 for 루프로 돌면 모든 칸을 순회할 수 있다
 for i in range(n):
  for j in range(m):
   print('current is', i, j)
   if traverse(i,j,ice_tray) == True:
    ice_cream_count += 1
 return ice_cream_count

# 상, 하, 좌, 우 방향으로 붙어 있으면 연결된 걸로 간주한다
# -> 네 방향으로 탐색을 시도했을 때 어떤 방향으로 앞에 있는 칸의 값이 0이면 구멍이 뜷려 있고, 서로 연결되어 있다고 볼 수 있다

# 방문한 정보는 어디에 넣어야 하나? 그냥 1차원 스택이어도 상관없나?
# => 답에선 방문 정보를 넣을 자료구조를 따로 두지 않고 입력받은 얼음 틀을 바꾸고 있다. 0=>1로 바꾸는 식이다.
# visited = []
# 따라서 이전에 한 다음 고민은 쓸모 없어졌다.
#  어떤 식으로 넣어야 할까? visited.append(ice_tray[i][j]) 형식으로 넣게 되면 어떤 위치를 방문했는지 알 수 없으니 의미가 없다.
#   뭘 넣어야 할까? 인덱스 조합? (0,0), (2,0) 같은?
#   visited.append((x,y))
#  방문 정보에 넣은 인덱스 조합 정보는 언제 빼야 할까? => 해당 인덱스 조합을 방문했을 때?

def traverse(x,y,ice_tray):
 # 현재 탐색하는 위치가 구멍이 뚫려있는 곳이라면, 그리고 이전에 탐색하지 않았던 곳이라면
 # 상하좌우 방향으로 구멍이 뚫려있든 그렇지 않든 상관없이 하나의 아이스크림 공간으로 볼 수 있다
 # 다만 상하좌우 방향으로 연결된 구멍이 있다면, 연결된 그 모든 구멍은 새로운 아이스크림 공간으로 보면 안된다.
 x_max = len(ice_tray)
 y_max = len(ice_tray[0])
 if x < 0 or x >= x_max or y < 0 or y >= y_max: # 경계 너머로 나가면 무시한다
  print(x, y, 'false!')
  return False

 #if ice_tray[x][y] == 1: # 현재 위치가 칸막이라면, 탐색을 그만둔다
 # 여기서 False를 반환하면 traverse()의 값이 False가 된다.
 # 그러면 traverse() 실행 중 어떤 칸은 구멍이 뚫린 칸이었더라도
 # 무시하게 되어 실제 답과 달라지게 된다. 따라서 이 조건절은 올바르지 않다.
 # return False
 if ice_tray[x][y] == 0: # 현재 위치에 구멍이 뚫려있다면,
  # 방문처리하고
  ice_tray[x][y] = 1
  print(x, y, 'has a hole!')
  # 상,하,좌,우 방향으로 탐색을 계속한다
  # 어떤 방향은 True를, 어떤 방향은 False를 반환할 것이다. 그러면 여기서 반환하는 False는 다른 True에 영향을 주지 않나?
  traverse(x,y-1,ice_tray)
  traverse(x,y+1,ice_tray)
  traverse(x-1,y,ice_tray)
  traverse(x+1,y,ice_tray)
  return True # 현재 칸은 구멍이 뚫려 있으므로, True를 반환해야 한다.
 print(x, y, 'no hole...')
 return False

print(freeze_drink())
