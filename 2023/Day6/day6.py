import timer
import re

with open('adventofcode.com_2023_day_6_input.txt', 'r') as file:
    dataset = file.read().splitlines()

Timer = timer.Timer()

time_t = [int(x) for x in re.findall(r'\d+', dataset[0])]
distance = [int(x) for x in re.findall(r'\d+', dataset[1])]

print(time_t)
print(distance)

mul_win = 1

for i in range(len(time_t)):
    time_game = time_t[i]
    distance_game = distance[i]
    win_count = 0
    for t in range(time_game + 1):
        x = time_game - t
        d = x * t
        win_count += 1 if d > distance_game else 0
    mul_win *= win_count

print(mul_win)

Timer.get_time(1)

time_t = int(''.join(re.findall(r'\d+', dataset[0])))
distance = int(''.join(re.findall(r'\d+', dataset[1])))

win_count = 0
for t in range(time_t + 1):
    x = time_t - t
    d = x * t
    win_count += 1 if d > distance else 0

print(win_count)

Timer.get_time(2)
