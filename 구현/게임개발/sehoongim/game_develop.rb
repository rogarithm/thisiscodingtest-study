def move(info)
  a, b = info.split("\n")[0].split(" ").map(&:to_i)
  x, y, direction = info.split("\n")[1].split(" ").map(&:to_i)
  map = []
  info.split("\n")[2..-1].each do |map_elem|
    map.push Array(map_elem.split(" ").map(&:to_i))
  end

  visited = Array.new(a){Array.new(b,0)}
  visited[x][y] = 1 #처음 방문한 곳을 표시한다

  # 북 동 남 서
  # 0  1  2  3
  dx = [-1, 0, 1, 0]
  dy = [0, 1, 0, -1]

  count = 1
  turn_time = 0
  while true do
    direction = turn_left(direction)

    new_x = x + dx[direction]
    new_y = y + dy[direction]
    if visited[new_x][new_y] == 0 and map[new_x][new_y] == 0
      visited[new_x][new_y] = 1
      x = new_x
      y = new_y
      count += 1
      turn_time = 0
      next
    else
      turn_time += 1
    end

    if turn_time == 4
      back_x = x - dx[direction]
      back_y = y - dy[direction]
      if map[back_x][back_y] == 0
        x = back_x
        y = back_y
        turn_time = 0
        next
      else
        break
      end
    end
  end

  count
end


def turn_left(direction_before)
  #동 서 남 북
  #1  3  2  0
  case direction_before
  when 1
    0
  when 0
    3
  when 3
    2
  when 2
    1
  end
end

puts move("4 4\n1 1 0\n1 1 1 1\n1 0 0 1\n1 1 0 1\n1 1 1 1")
