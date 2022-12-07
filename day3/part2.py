def priority(c: str):
    if c.isupper():
        return ord(c) - 38
    else:
        return ord(c) - 96


with open('input.txt') as f:
    lines = f.read().splitlines()

common = []
for x in range(0, len(lines), 3):
    common.append(tuple(set(list(lines[x])) & set(list(lines[x+1])) & set(list(lines[x+2])))[0])

print(sum(priority(c) for c in common))