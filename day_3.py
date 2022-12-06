def find_item_type(l):
    chars = list(l)
    chars_len = len(chars) // 2

    shared = set(chars[:chars_len]) & set(chars[-chars_len:])

    return list(shared)[0]


def find_group_item_type(l):

    shared = set(l[0]) & set(l[1]) & set(l[2])

    return list(shared)[0]


def get_item_priority(item):
    priority = ord(item.lower()) - 96 + 26 * item.isupper()

    return priority


f = open('day_3/input.txt')

# Part 1: Find the priority of items type in each compartment

total_priority = 0

for line in f.readlines():
    shared_item = find_item_type(line.strip())
    shared_item_val = get_item_priority(shared_item)

    total_priority += shared_item_val

print(total_priority)

f.close()

# Part 2: Group in threes and find the total priority

f = open('day_3/input.txt')

total_priority = 0

all_lines = f.readlines()
for i in range(len(all_lines) // 3):
    lines = [line.strip() for line in all_lines[3 * i:3 * i + 3]]
    shared_item = find_group_item_type(lines)
    shared_item_val = get_item_priority(shared_item)

    total_priority += shared_item_val

print(total_priority)

f.close()
