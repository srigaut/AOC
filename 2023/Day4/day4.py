from parse import parse
import re

with open('adventofcode.com_2023_day_4_input.txt', 'r') as file:
    dataset = file.read().splitlines()

# Functions that returns a tuple comprised of 2 lists (wining cards and
# drawn cards lists)
def winings_and_drawn_lists(line):
    nb, wining_str, drawn_str = parse('Card {}: {} | {}', line)
    wining_cards = re.findall(r'\d+', wining_str)
    drawn_cards = re.findall(r'\d+', drawn_str)
    return (wining_cards, drawn_cards)

### PART ONE ###

total_worth = 0

# Function that computes the number of wins for a given scratchcard
def compute_wins(wining_cards, drawn_cards):
    nb_wins = 0
    for draw in drawn_cards:
        nb_wins += 1 if draw in wining_cards else 0
    return nb_wins

for line in dataset:
    wining_cards, drawn_cards = winings_and_drawn_lists(line)
    nb_wins_per_line = compute_wins(wining_cards, drawn_cards)
    total_worth += 0 if nb_wins_per_line == 0 else 2 ** (nb_wins_per_line - 1)

print(total_worth)

### PART TWO ###

i_line = 0
dataset_nb_instances = [1] * len(dataset)

for line in dataset:
    wining_cards, drawn_cards = winings_and_drawn_lists(line)
    nb_wins_per_line = compute_wins(wining_cards, drawn_cards)
    if nb_wins_per_line >= 1:
        for add_scratchcards in range(1, nb_wins_per_line + 1):
            dataset_nb_instances[i_line + add_scratchcards] += \
                dataset_nb_instances[i_line]
    else:
        pass
    i_line += 1

print(sum(dataset_nb_instances))
