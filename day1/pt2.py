numbers_dict = {}  # dictionary for storing digits
speltNumbersDict = {'one': '1', 'two': '2', 'three': '3', 'four': '4',
                    'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

file = 'Day1/input.txt'


with open(file, 'r') as file:  # open the file
    for line in file:

        for i in speltNumbersDict:
            line = line.replace(i, i + speltNumbersDict[i] + i)

        # take only the numbers from the line
        numbers = [int(char) for char in line if char.isdigit()]

        if len(numbers) >= 1:  # if there are more than two numbers on the line
            # combine the number
            combined = int(str(numbers[0]) + str(numbers[-1]))

            # add the new number to the dictionary
            numbers_dict[line.strip()] = combined


total_sum = sum(numbers_dict.values())  # calc sum


print(numbers_dict)  # disp
print(total_sum)  # disp
