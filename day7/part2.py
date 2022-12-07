root = {}
cwd = root
path = []
totals = []


def dir_sum(d: dict):
    total = 0
    for k, v in d.items():
        if type(v) == dict:
            z = dir_sum(v)
            total += z
            totals.append(z)
        else:
            total += v
    return total

with open('input.txt') as f:
    lines = f.read().splitlines()

del lines[0]

idx = 0
while idx < len(lines):
    line = lines[idx]
    idx += 1
    if line.startswith('dir'):
        cwd[line.partition(' ')[2]] = {}
    elif line.startswith('$ cd'):
        if line.split(' ')[-1] == '..':
            cwd = path.pop()
            continue
        path.append(cwd)
        cwd = cwd[line.split(' ')[-1]]
    elif line.startswith('$ ls'):
        pass
    else:
        cwd[line.partition(' ')[2]] = int(line.partition(' ')[0])



free = 70_000_000 - (dir_sum(root))
q = (list(x for x in totals if x + free > 30_000_000))
print(sum(q), q)