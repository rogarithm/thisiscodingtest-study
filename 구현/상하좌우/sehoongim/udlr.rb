def udlr input
  n = input.split("\n")[0]
  directions = input.split("\n")[1].split(" ")

  answer = [1,1]
  directions.each do |direction|
    if direction == "R" and answer[1] != n
      answer[1] += 1
    end
    if direction == "L" and answer[1] != 1
      answer[1] += 1
    end
    if direction == "U" and answer[0] != 1
      answer[0] += 1
    end
    if direction == "D" and answer[0] != n
      answer[0] += 1
    end
  end
  p answer
  return "#{answer[0]} #{answer[1]}"
end

udlr("5\nR R R U D D")