import timer
import re
import pandas as pd

with open('adventofcode.com_2023_day_9_input.txt', 'r') as file:
    data = file.read().splitlines()

Timer = timer.Timer()

dataset = [d.split(' ') for d in data]

def get_value(line):
    line_length = len(line)
    if line_length == 2:
        return int(line[1]) - int(line[0])
    temp_list = []
    for i in range(1, line_length):
        temp_list.append(int(line[i]) - int(line[i-1]))
    return int(line[-1]) + get_value(temp_list)

print(sum(map(get_value, dataset)))

Timer.get_time(1)
