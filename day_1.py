def find_positional_value(input_dict, search_key='total', position=-1):
    """Find position value for a key in a dictionary.

    Args:
        input_dict (dict): Dict to search key
        search_key (str, optional): Key to search for in dict. Defaults to 'total'
        position (int, optional): Position to search for. Defaults to -1, i.e. maximum
    """

    val_array = []

    for key in input_dict.keys():
        val_array.append(input_dict[key][search_key])

    val_array.sort()
    positional_val = val_array[position]

    return positional_val


elf_dict = {}
elf_number = 1

new_elf = True

f = open('day_1/input.txt')

for line in f.readlines():

    if new_elf:
        elf_dict['elf_%d' % elf_number] = {'total': 0, 'individual': []}

    if line.strip() == '':
        new_elf = True
        elf_number += 1
    else:
        new_elf = False
        calorie_value = int(line.strip())
        elf_dict['elf_%d' % elf_number]['individual'].append(calorie_value)
        elf_dict['elf_%d' % elf_number]['total'] += calorie_value

f.close()

# Part 1: Find maximum calorie value any elf has

maximum_calorie_value = find_positional_value(elf_dict)
print('Max calorie value: %d' % maximum_calorie_value)

# Part 2: Find total of the three elves with the most calories
top_3_total_cals = maximum_calorie_value + \
                   find_positional_value(elf_dict, position=-2) + \
                   find_positional_value(elf_dict, position=-3)
print('Top 3 max calorie value: %d' % top_3_total_cals)
