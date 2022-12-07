with open('input.txt') as f:
    elves = [0]    
    for line in f:
        if line == '\n':
            elves.append(0)
        else:
            elves[-1] += int(line)
elves.sort(reverse=True)

print(elves[0] + elves[1] + elves[2])
