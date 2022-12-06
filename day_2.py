CHOICES = ['rock', 'paper', 'scissors']
RESULTS = ['loss', 'draw', 'win']


def parse_round(l):

    c = ['', '']

    if l[0].lower() == 'a':
        c[0] = CHOICES[0]
    elif l[0].lower() == 'b':
        c[0] = CHOICES[1]
    elif l[0].lower() == 'c':
        c[0] = CHOICES[2]
    else:
        raise Warning('Value %d not recognised' % l[0])

    if l[1].lower() == 'x':
        c[1] = CHOICES[0]
    elif l[1].lower() == 'y':
        c[1] = CHOICES[1]
    elif l[1].lower() == 'z':
        c[1] = CHOICES[2]
    else:
        raise Warning('Value %d not recognised' % l[0])

    return c


def parse_winner(c):
    if c[0] == 'rock':
        if c[1] == 'rock':
            r = 'draw'
        elif c[1] == 'paper':
            r = 'win'
        elif c[1] == 'scissors':
            r = 'loss'
        else:
            raise Warning('Choice %s unknown' % c[1])

    elif c[0] == 'paper':
        if c[1] == 'rock':
            r = 'loss'
        elif c[1] == 'paper':
            r = 'draw'
        elif c[1] == 'scissors':
            r = 'win'
        else:
            raise Warning('Choice %s unknown' % c[1])

    elif c[0] == 'scissors':
        if c[1] == 'rock':
            r = 'win'
        elif c[1] == 'paper':
            r = 'loss'
        elif c[1] == 'scissors':
            r = 'draw'
        else:
            raise Warning('Choice %s unknown' % c[1])

    else:
        raise Warning('Choice %s unknown' % c[0])

    return r

def parse_result(c):

    if c == 'X':
        r = 'loss'
    elif c == 'Y':
        r = 'draw'
    elif c == 'Z':
        r = 'win'
    else:
        raise Warning('Choice %s unknown' % c)

    return r


def parse_round_end(c, r):

    if r == 'draw':
        return c

    if c == 'rock':
        if r == 'loss':
            cc = 'scissors'
        elif r == 'win':
            cc = 'paper'
        else:
            raise Warning('Result %s unknown' % r)

    elif c == 'paper':
        if r == 'loss':
            cc = 'rock'
        elif r == 'win':
            cc = 'scissors'
        else:
            raise Warning('Result %s unknown' % r)

    elif c == 'scissors':
        if r == 'loss':
            cc = 'paper'
        elif r == 'win':
            cc = 'rock'
        else:
            raise Warning('Result %s unknown' % r)

    else:
        raise Warning('Choice %s unknown' % c[0])

    return cc


f = open('day_2/input.txt')

# Part 1: Get the total score

total_score = 0

for line in f.readlines():
    choices = parse_round(line.split())
    result = parse_winner(choices)

    correct_choice = parse_round_end(choices[0], result)

    round_score = CHOICES.index(correct_choice) + 1 + 3 * RESULTS.index(result)
    total_score += round_score

f.close()

print(total_score)

# Part 2: Use the second column to define lose/win/draw and the total score from there

f = open('day_2/input.txt')

# Part 1: Reverse, get the correct result

total_score = 0

for line in f.readlines():
    choices = parse_round(line.split())
    result = parse_result(line.split()[-1])
    correct_choice = parse_round_end(choices[0], result)

    round_score = CHOICES.index(correct_choice) + 1 + 3 * RESULTS.index(result)
    total_score += round_score

print(total_score)

f.close()
