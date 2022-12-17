# "The first column is what your opponent is going to play: A for Rock, B for Paper, and C for Scissors. 
# The second column--" Suddenly, the Elf is called away to help with someone's tent.
# The second column, you reason, must be what you should play in response: X for Rock, Y for Paper, and Z for Scissors. 
# Winning every time would be suspicious, so the responses must have been carefully chosen.

# The score for a single round is the score for the shape you selected 
# (1 for Rock, 2 for Paper, and 3 for Scissors)
#  plus the score for the outcome of the round 
# (0 if you lost, 3 if the round was a draw, and 6 if you won).

# calculate the score you would get if you were to follow the strategy guide.

A = X = ROCK = 1
B = Y = PAPER = 2
C = Z = SCISSORS = 3

WIN = 6
TIE = 3
LOSS = 0

def rps_strategy_guide(filename):
    points_grid = {
        'A X': TIE + X,
        'A Y': WIN + Y,
        'A Z': LOSS + Z,
        'B X': LOSS + X,
        'B Y': TIE + Y,
        'B Z': WIN + Z,
        'C X': WIN + X,
        'C Y': LOSS + Y,
        'C Z': TIE + Z
    }

    points = 0

    with open(filename, 'r') as f:
        for l in f:
            points += points_grid[l[0:3]]
    
    print("DAY 2 (part 1) points: %d" % (points))

# PART 2: X means you need to lose, 
#         Y means you need to end the round in a draw, and 
#         Z means you need to win. Good luck!"

def rps_strategy_guide_decrypted(filename):
    points_grid = {
        'A X': LOSS + SCISSORS,
        'A Y': TIE + ROCK,
        'A Z': WIN + PAPER,
        'B X': LOSS + ROCK,
        'B Y': TIE + PAPER,
        'B Z': WIN + SCISSORS,
        'C X': LOSS + PAPER,
        'C Y': TIE + SCISSORS,
        'C Z': WIN + ROCK
    }

    points = 0

    with open(filename, 'r') as f:
        for l in f:
            points += points_grid[l[0:3]]
    
    print("DAY 2 (part 2) points: %d" % (points))

if __name__ == "__main__":
    rps_strategy_guide("day2.input")
    rps_strategy_guide_decrypted("day2.input")

