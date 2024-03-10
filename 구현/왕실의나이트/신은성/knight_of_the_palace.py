current_position = input()

x, y = current_position

x_dict = {'a': 0,
          'b': 1,
          'c': 2,
          'd': 3,
          'e': 4,
          'f': 5,
          'g': 6,
          'h': 7
          }

# x_dict에 따라 위치값 변환 
x = x_dict[x]
y = int(y)


# 위치는 1과 8 사이의 값이여야함
def count_possible_move(x, y):
    return (1<=x<=8) and (1<=y<=8)

# 이동 가능 조합 전부 리턴. 총 8개
possible_directions = [[ 1, 2], [ 2, 1], 
                      [-1, 2], [-2, 1], 
                      [-2,-1], [-1,-2], 
                      [ 1,-2], [ 2,-1]]

count = 0
for direction in possible_directions:

    next_move = x + direction[0], y + direction[1]
    count += count_possible_move(next_move)

print(count)




