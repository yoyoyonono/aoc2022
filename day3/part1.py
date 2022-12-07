def priority(c: str):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96

prioritysum = 0

with open('input.txt') as f:
    for line in f:
        line = line[0:-1]
        both = set(list(line[0:int(len(line)/2)])) & set(list(line[int(len(line)/2):]))
        print(both)
        prioritysum += (priority(tuple(both)[0]))

print(prioritysum)