import timer
import pandas as pd
import shapely
import numpy as np

with open('adventofcode.com_2023_day_10_input.txt', 'r') as file:
    data = file.read().splitlines()

Timer = timer.Timer()

df = pd.DataFrame([[*d] for d in data])

start_row, start_column = df[df == 'S'].stack().index.to_list()[0]

directions = {'|': ('NS', 'SN'), '-': ('WE', 'EW'), 'L': ('NE', 'EN'),
              'J': ('NW', 'WN'), '7': ('WS', 'SW'), 'F': ('SE', 'ES')}

movements = {'N': (-1, 0), 'S': (+1, 0), 'E': (0, +1), 'W': (0, -1)}

card = {'N': 'S', 'E': 'W', 'W': 'E', 'S': 'N'}

def reverse_directions(prov):
    return card[prov]

def get_directions(prov, direcs):
    return direcs[0] if direcs[0].startswith(prov) else direcs[1]

def move(row, column, dir):
    row = row + movements[dir][0]
    column = column + movements[dir][1]
    prov = reverse_directions(dir)
    dir = get_directions(prov, directions[df[column][row]])[1]
    return (row, column, dir)

End = False
move1 = (start_row, start_column, 'N')
move2 = (start_row, start_column, 'S')
count = 0
coordinates_list1 = []
coordinates_list1.append((start_row, start_column))
coordinates_list2 = []

while not End:
    move1 = move(move1[0], move1[1], move1[2])
    move2 = move(move2[0], move2[1], move2[2])
    coordinates_list1.append((move1[0], move1[1]))
    coordinates_list2.append((move2[0], move2[1]))
    count += 1
    if move1[0] == move2[0] and move1[1] == move2[1]:
        End = True
        coordinates_list1.pop()
        break

print(count)

Timer.get_time(1)

coordinates_list2.reverse()
coord = coordinates_list1 + coordinates_list2 + [(start_row, start_column)]

poly = shapely.Polygon(coord)

list_to_check = np.array([shapely.Point(d[0],d[1]) for d in df[df.isin(['.'])].stack().index.to_list()])

result = shapely.contains(poly, list_to_check)
print(sum(result))

Timer.get_time(2)
