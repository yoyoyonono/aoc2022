with open('input.txt') as f:
    field = list(list(int(z) for z in (x)) for x in f.read().splitlines())

def visible(row, col):
    right = True
    down = True
    left = True
    up = True

    #check to the right
    if col < len(field[row]) - 1:
        for x in range(col + 1, len(field[row])):
            if field[row][x] >= field[row][col]:
                right = False
                break
    #check down
    if row < len(field) - 1:
        for y in range(row + 1, len(field)):
            if field[y][col] >= field[row][col]:
                down = False
                break
    #check left
    if col > 0:
        for x in range(col - 1, -1, -1):
            if field[row][x] >=field[row][col]:
                left = False
                break
    #check up
    if row > 0:
        for y in range(row - 1, -1, -1):
            if field[y][col] >= field[row][col]:
                up = False
                break
    return 1 if right or down or left or up else 0

visible_field = [[None] * len(x) for x in field]

for y in range(len(field)):
    for x in range(len(field[y])):
        visible_field[y][x] = visible(y, x)

print(visible_field)
print(sum(sum(x) for x in visible_field))