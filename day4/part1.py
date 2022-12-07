def range1_contains_range2(range1, range2):
    return int(range1[0]) <= int(range2[0]) and int(range1[2]) >= int(range2[2])

def range1_overlaps_range2(range1, range2):
    return int(range1[0]) <= int(range2[0]) and int(range1[2]) >= int(range2[0]) or int(range1[0]) <= int(range2[2]) and int(range1[2]) >= int(range2[2])

def either_or_range(range1, range2):
    return range1_contains_range2(range1, range2) or range1_contains_range2(range2, range1)

def either_or_overlap(range1, range2):
    return range1_overlaps_range2(range1, range2) or range1_overlaps_range2(range2, range1)

number = 0
with open('input.txt') as f:
    for line in f:
        line = line[:-1]
        first, _, second = line.partition(',')
        if (either_or_overlap(first.partition('-'), second.partition('-'))):
            print("True")
            number += 1
        else:
            print("False")
print(number)