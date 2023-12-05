import re

with open('adventofcode.com_2023_day_3_input.txt', 'r') as file:
    dataset = file.read().splitlines()

### PART ONE ###

# Function that enlarges the dataset adding two rows of dots (1 above / 1 below)
# and 3 columns of dots (1 before / two after)
def enlarge_database(data):
    new_data = [(len(data) + 3) * '.']
    for line in data:
        new_data.append('.' + line + '..')
    new_data.append((len(data) + 3) * '.')
    return new_data

# Function that tests if a given number is a valid gear or not
def test_number(database, i_line, n_start, n_end):
    block = database[i_line - 1][(n_start - 1):(n_end + 1 )] +\
        database[i_line][(n_start - 1):(n_end + 1 )] +\
            database[i_line + 1][(n_start - 1):(n_end + 1)]
    block = re.sub(r'\d+', '', block)
    block = block.replace('.', '')
    return False if block == '' else True

i_line_part1 = 0
sum_engine = 0

enlarged_database = enlarge_database(dataset)

for line in enlarged_database:
    numbers = re.finditer(r'\d+', line)
    for number in numbers:
        if test_number(enlarged_database, i_line_part1,
                       number.start(), number.end()):
            sum_engine += int(number.group())
    i_line_part1 += 1

print(sum_engine)

### PART TWO ###

# Function that multiplies valid gear for a given *
def get_valid_numbers(database, i_line, n_start, n_end):
    mul_gear = 1
    star_numbers = []
    for i in range(i_line - 1, i_line + 2):
        numbers = re.finditer(r'\d+', database[i])
        for number in numbers:
            if number.end() >= n_start and number.start() <= n_end:
                star_numbers.append(int(number.group()))
            else:
                pass
    print(star_numbers)
    if len(star_numbers) >= 2:
        for elem in star_numbers:
            mul_gear *= elem
    else:
        mul_gear = 0
    print(mul_gear)
    return mul_gear

i_line_part2 = 0
sum_gear = 0

for line in enlarged_database:
    stars = re.finditer(r'\*', line)
    for star in stars:
        mul_gear = get_valid_numbers(enlarged_database, i_line_part2,
                                     star.start(), star.end())
        print(mul_gear)
        print(type(mul_gear))
        sum_gear += mul_gear
    i_line_part2 += 1

print(sum_gear)
