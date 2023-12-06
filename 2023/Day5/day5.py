import re
from parse import parse

with open('adventofcode.com_2023_day_5_input.txt', 'r') as file:
    dataset = file.read().splitlines()

### PART ONE ###

# Parse data and return a tuple of 1 list (seeds list) and 1 list of lists
# (comprised of source-destination-length mapping table)
def parsing_data(data):
    seeds = [int(n) for n in re.findall('\d+', parse('seeds: {}', dataset[0])[0])]
    mapping_matrix = []
    current_map = []
    for line in data[3:]:
        if line == '':
            continue
        elif line.endswith(' map:'):
            mapping_matrix.append(current_map)
            current_map = []
        else:
            current_map.append([int(n) for n in re.findall(r'\d+', line)])
    mapping_matrix.append(current_map)
    return (seeds, mapping_matrix)

# Returns destination for a given source and a given mapping table
def return_destination(map, source):
    result = -1
    for destination_map, source_map, offset in map:
        if source_map <= source < source_map + offset:
            result = destination_map + (source - source_map)
        else:
            pass
    return source if result == -1 else result

# Gets the minimum of destinations recursively
def part_one(data):
    min_destination = []
    seeds, mapping_matrix = parsing_data(data)
    for seed in seeds:
        source = seed
        for data in mapping_matrix:
            source = return_destination(data, source)
        min_destination.append(source)
    return min(min_destination)

print(part_one(dataset))
