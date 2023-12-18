import timer
import re

# Let's try a divide and conquer approach

with open('adventofcode.com_2023_day_6_input.txt', 'r') as file:
    dataset = file.read().splitlines()

Timer = timer.Timer()

time_array = [int(x) for x in re.findall(r'\d+', dataset[0])]
distance_array = [int(x) for x in re.findall(r'\d+', dataset[1])]

def check(time, distance, elem):
    x = time - elem
    d = x * elem
    return d > distance

def get_outbounds(time, distance, interval):
    pivot = (interval[0] + interval[1]) // 2
    if check(time, distance, pivot):
        if check(time, distance, pivot-1) != check(time, distance, pivot+1):
            return pivot
        else:
            return get_outbounds(time, distance, (interval[0], pivot))\
                if interval[1] <= (time // 2) else\
                    get_outbounds(time, distance, (pivot, interval[1]))
    else:
        return get_outbounds(time, distance, (pivot, interval[1]))\
            if interval[1] <= (time // 2) else\
                get_outbounds(time, distance, (interval[0], pivot))

def consolidate_results(time, distance):
    time_range = list(range(time + 1))
    pivot = len(time_range) // 2
    return (get_outbounds(time, distance, (0, pivot)),\
        get_outbounds(time, distance, (pivot, time)))

result = list(map(consolidate_results, time_array, distance_array))
diff = [x[1] - x[0] + 1 for x in result]

nb_result = 1
for x in diff:
    nb_result *= x

print(nb_result)
Timer.get_time(1)

time_array_part2 = int(''.join(re.findall(r'\d+', dataset[0])))
distance_array_part2 = int(''.join(re.findall(r'\d+', dataset[1])))

results = consolidate_results(time_array_part2, distance_array_part2)
print(results[1] - results[0] + 1)

Timer.get_time(2)
