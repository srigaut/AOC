import re

# Opens the input file
with open("adventofcode.com_2023_day_1_input.txt","r") as file:
    dataset = file.read().splitlines()

# Function that concatenate the first and the last digit of each row
# and add them to compute the sum of all calibrations values
def sum_calibrations_values(data):
    calibration_value = 0
    for elem in dataset:
        line = ''.join(re.findall(r'\d+', elem))
        calibration_value += int(line[0] + line[-1])
    return calibration_value

# Print the result
print(sum_calibrations_values(dataset))
