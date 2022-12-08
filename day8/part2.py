with open('input.txt') as f:
    field = list(list(int(z) for z in (x)) for x in f.read().splitlines())

def visible(row, col):
    right = 1
    down = 1
    left = 1
    up = 1

    #check to the right
    if col < len(field[row]) - 1:
        for x in range(col + 1, len(field[row])):
            right = x - col
            if field[row][x] >= field[row][col]:
                break
    #check down
    if row < len(field) - 1:
        for y in range(row + 1, len(field)):
            down = y - row
            if field[y][col] >= field[row][col]:
                break
    #check left
    if col > 0:
        for x in range(col - 1, -1, -1):
            left = col - x
            if field[row][x] >=field[row][col]:
                break
    #check up
    if row > 0:
        for y in range(row - 1, -1, -1):
            up = row - y
            if field[y][col] >= field[row][col]:
                break
    return (up*down*left*right)

visible_field = [[None] * len(x) for x in field]

visible(1, 2)

for y in range(len(field)):
    for x in range(len(field[y])):
        visible_field[y][x] = visible(y, x)


print(visible_field)
print(max(max(x[1:-1]) for x in visible_field[1:-1]))