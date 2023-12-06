from parse import parse
import re

with open('adventofcode.com_2023_day_4_input.txt', 'r') as file:
    dataset = file.read().splitlines()

### PART ONE ###

total_worth = 0

for line in dataset:
    nb, wining_str, drawn_str = parse('Card {}: {} | {}', line)
    wining_cards = re.findall(r'\d+', wining_str)
    drawn_cards = re.findall(r'\d+', drawn_str)
    nb_wins = 0
    for draw in drawn_cards:
        nb_wins += 1 if draw in wining_cards else 0
    total_worth += 0 if nb_wins == 0 else 2 ** (nb_wins - 1)

print(total_worth)
