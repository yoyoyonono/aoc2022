scores = {'X': 1, 'Y': 2, 'Z': 3}
wins = ['A Y', 'B Z', 'C X']
losses = ['A Z', 'B X', 'C Y']
draws = ['A X', 'B Y', 'C Z']

with open('input.txt') as f:
    score = 0
    for line in f:
        line = line.strip()
        score += scores[line[-1]]
        if line in wins:
            score += 6
        elif line in losses:
            pass
        else:
            score += 3

print(score)