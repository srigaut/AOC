import timer
from parse import parse

with open('adventofcode.com_2023_day_7_input.txt', 'r') as file:
    dataset = file.read().splitlines()

Timer = timer.Timer()

def valuate_hand(round):
    hand, bid = round.split(" ")
    hand = hand.translate(str.maketrans('TJQKA', faces))
    best = max([sort_valued_hand(hand.replace('0', joker)) for joker in hand])
    return best, hand, bid

def sort_valued_hand(hand):
    return sorted(map(hand.count, hand), reverse=True)

faces = 'ABCDE'
print(sum(rank * int(bid) for rank, (*_, bid) in\
    enumerate(sorted(map(valuate_hand, dataset)), start=1)))

Timer.get_time(1)

faces = 'A0CDE'
print(sum(rank * int(bid) for rank, (*_, bid) in\
    enumerate(sorted(map(valuate_hand, dataset)), start=1)))

Timer.get_time(2)
