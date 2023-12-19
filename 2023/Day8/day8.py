import timer
from parse import parse
import pandas as pd
import math
import functools

with open('adventofcode.com_2023_day_8_input.txt', 'r') as file:
    directions, _, *dataset = file.read().splitlines()

Timer = timer.Timer()

def build_df(line):
    start, left, right = parse('{} = ({}, {})', line)
    return [start, left, right]

df = pd.DataFrame(list(map(build_df, dataset)),\
    columns = ['Start', 'L', 'R'])

df.sort_values(by='Start', inplace=True)
df.reset_index(drop=True, inplace=True)

End = False
start = 'AAA'
count = 0

while not End:
    for dir in directions:
        start = df[df['Start'].isin([start])][dir].item()
        count += 1
        if start == 'ZZZ':
            End = True
            break

print(count)

Timer.get_time(1)

starts = list(df[df['Start'].str.endswith('A')]['Start'])

def solve(start_pos):
    End = False
    count = 0
    while not End:
        for dir in directions:
            start_pos = df[df['Start'].isin([start_pos])][dir].item()
            count += 1
            if start_pos.endswith('Z'):
                End = True
                break
    return count

def my_lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def my_lcm(*integers):
    return functools.reduce(my_lcm_base, integers)

result = my_lcm(*map(solve, starts))
print(result)

Timer.get_time(2)
