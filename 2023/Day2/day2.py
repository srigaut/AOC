from parse import parse

# Opens the input file
with open('adventofcode.com_2023_day_2_input.txt','r') as file:
    dataset = file.read().splitlines()

### PART ONE ###
total_game = 0

for game in dataset:
    nb_game, round = parse('Game {:d}: {}', game)
    if all(int(nb_cube) <= 12 if 'red' == color else
           int(nb_cube) <= 13 if 'green' == color else
           int(nb_cube) <= 14
    for sub_round in round.split('; ')
    for nb_cube, color in (sub_draw.split(' ') for sub_draw in sub_round.split(', '))):
        total_game += nb_game

print(total_game)
