scores = {'X': 1, 'Y': 2, 'Z': 3}
letterindex = {'A': 0, 'B': 1, 'C': 2}
wins = ['A Y', 'B Z', 'C X']
losses = ['A Z', 'B X', 'C Y']
draws = ['A X', 'B Y', 'C Z']
wld = {'X': 0, 'Y': 3, 'Z': 6}

with open('input.txt') as f:
    score = 0
    for line in f:
        line = line.strip()
        score += wld[line[-1]]
        if line[-1] == 'X':
            score += scores[losses[letterindex[line[0]]][2]]            
        elif line[-1] == 'Y':
            score += scores[draws[letterindex[line[0]]][2]]
        else:
            score += scores[wins[letterindex[line[0]]][2]]

print(score)