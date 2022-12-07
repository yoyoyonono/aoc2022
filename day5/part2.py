with open("input.txt") as f:
    lines = f.read().splitlines()

stacks: list[list[str]] = []

stack_line_num = 0
# find number of stacks
for line in lines:
    if line.startswith(" 1"):
        for x in range(int(chr(max(ord(x) for x in line)))):
            stacks.append([])
        break
    stack_line_num += 1

for line in lines[stack_line_num - 1::-1]:
    for k, i in enumerate(range(1, len(line), 4)):
        if line[i] != " ":
            stacks[k].append(line[i])

for line in lines[stack_line_num + 2:]:
    num, origin, destination = tuple(int(x) for x in (line.split()[1::2]))
    popped = []
    for x in range(num):
        popped.append(stacks[int(origin) - 1].pop())
    for x in popped[::-1]:
        stacks[int(destination) - 1].append(x)

print(''.join(x[-1] for x in stacks))