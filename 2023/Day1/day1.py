import re

# Opens the input file
with open("adventofcode.com_2023_day_1_input.txt","r") as file:
    dataset = file.read().splitlines()

### PART ONE ###
# Function that extract all numbers (only digits) for a given row
def get_numbers(element):
    return ''.join(re.findall(r'\d+', element))

# Function that concatenates the first and the last digit of each row
# and add them to compute the sum of all calibrations values
def sum_calibrations_values(data, nb_part):
    calibration_value = 0
    for elem in data:
        line = get_numbers(elem) if nb_part == 1 else get_numbers_2(elem)
        calibration_value += int(line[0] + line[-1])
    return calibration_value

### PART TWO ###
numbers_in_digits = {
    'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
    'seven': '7', 'eight': '8', 'nine': '9'
}

numbers = list(numbers_in_digits.keys())

# Function that extract all numbers (digits and letters) for a given row
def get_numbers_2(element):
    str_numbers = ''
    for i in range(len(element)):
        if element[i].isdigit():
            str_numbers += element[i]
        elif element[i:i+5] in numbers and i+5 <= len(element):
            str_numbers += numbers_in_digits[element[i:i+5]]
        elif element[i:i+4] in numbers and i+4 <= len(element):
            str_numbers += numbers_in_digits[element[i:i+4]]
        elif element[i:i+3] in numbers and i+3 <= len(element):
            str_numbers += numbers_in_digits[element[i:i+3]]
        else:
            pass
    return str_numbers

# Print the result - part 1 & part 2
print(sum_calibrations_values(dataset, 1))
print(sum_calibrations_values(dataset, 2))
