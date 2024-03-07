N = int(input())

moves = map(str, input().split())

directions = {
                'R': [0, 1], # y, x
                'L': [0,-1],
                'U': [-1,0],
                'D': [1, 0]
                }

cur_loc = [1, 1]
for instruction in moves:
    cur_loc = [cur_loc[0] + directions[instruction][0], cur_loc[1] + directions[instruction][1]]
    
    cur_loc[0] = min(max(1, cur_loc[0]), N)
    cur_loc[1] = min(max(1, cur_loc[1]), N)

print(' '.join(map(str, cur_loc)))
    




