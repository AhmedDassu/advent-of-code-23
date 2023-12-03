numbers_dict = {}  # dictionary for storing digits

file = 'input.txt'


with open(file, 'r') as file:  # open the file
    for line in file:
        # take only the numbers from the line
        numbers = [int(char) for char in line if char.isdigit()]

        if len(numbers) >= 2:  # if there are more than two numbers on the line
            # combine the number
            combined = int(str(numbers[0]) + str(numbers[-1]))

            # add the new number to the dictionary
            numbers_dict[line.strip()] = combined


total_sum = sum(numbers_dict.values())  # calc sum


print(numbers_dict)  # disp
print(total_sum)  # disp
