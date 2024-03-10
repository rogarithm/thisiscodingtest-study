def udlr(inputs):
    n = inputs.split("\n")[0]
    directions = inputs.split("\n")[1].split(" ")

    position = [1,1]
    for direction in directions:
        if direction == "R" and position[1] != n:
            position[1] += 1
        if direction == "L" and position[1] != 1:
            position[1] -= 1
        if direction == "U" and position[0] != 1:
            position[0] -= 1
        if direction == "D" and position[0] != n:
            position[0] += 1
    return position

print(udlr("5\nR R R U D D"))
print(udlr("5\nR D D U R"))