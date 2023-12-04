from parse import parse

# Opens the input file
with open('adventofcode.com_2023_day_2_input.txt','r') as file:
    dataset = file.read().splitlines()

### PART ONE ###
total_game = 0

# Loop that verifies for each game if draws are valid
# i.e. red cubes <= 12 ; green cubes <= 13 ; blue cubes <= 14
for game in dataset:
    nb_game, round = parse('Game {:d}: {}', game)
    if all(int(nb_cube) <= 12 if 'red' == color else
           int(nb_cube) <= 13 if 'green' == color else
           int(nb_cube) <= 14
    for sub_round in round.split('; ')
    for nb_cube, color in (sub_draw.split(' ')
                           for sub_draw in sub_round.split(', '))):
        total_game += nb_game

print(total_game)

### PART TWO ###
total_powers = 0

# Function to obtain the maximum between current draw and current minimum known
# for a given color
def min_color(color, nb, current_min):
    return (color, max(nb, current_min))

# Loop that determines each minimum number of cubes for each game to make
# the game valid
for game in dataset:
    nb_game, round = parse('Game {:d}: {}', game)
    minimum = {'red': 1, 'green': 1, 'blue': 1}
    for sub_round in round.split('; '):
        for nb_cube, color in (sub_draw.split(' ')
                               for sub_draw in sub_round.split(', ')):
            color_current_min = min_color(color, int(nb_cube), minimum[color])
            minimum[color_current_min[0]] = color_current_min[1]
    total_powers += minimum['red'] * minimum['green'] * minimum['blue']

print(total_powers)
