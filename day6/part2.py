with open('input.txt') as f:
    stream = f.read().strip()

print(stream)

for x in range(len(stream)):
    print(stream[x:x+14])
    if len(set([x for x in stream[x:x+14]])) == 14:
        print(x+14)
        break