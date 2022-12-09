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

# loop through the list of lines starting from the one before the numbers, going to the beginning, and working backwards
for line in lines[stack_line_num - 1::-1]:
    for k, i in enumerate(range(1, len(line), 4)): # loop through the characters in each line, starting on the second one, and skipping 4
        if line[i] != " ":
            stacks[k].append(line[i]) # add the letter in the character to the correct stack

# loop through the lines with the instructions
for line in lines[stack_line_num + 2:]:
    num, origin, destination = tuple(int(x) for x in (line.split()[1::2])) # split the line by spaces, get every other token starting with the second one
    popped = []
    for x in range(num):
        popped.append(stacks[int(origin) - 1].pop()) # take n items off the stack and put them in a variable
    for x in popped:
        stacks[int(destination) - 1].append(x) # put those on the correct stack

print(''.join(x[-1] for x in stacks)) # print the top letter (last item hence -1) form each stack and put them together