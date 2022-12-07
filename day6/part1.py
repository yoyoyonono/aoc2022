with open('input.txt') as f:
    stream = f.read().strip()

print(stream)

for x in range(len(stream)):
    print(stream[x:x+4])
    if len(set([x for x in stream[x:x+4]])) == 4:
        print(x+4)
        break