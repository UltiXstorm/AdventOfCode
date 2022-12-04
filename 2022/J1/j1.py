elfs_capacity = []

with open('./input.txt', 'r') as input_file:
    current_capacity = 0

    for line in input_file:
        if(line == '\n'):
            elfs_capacity.append(current_capacity)
            current_capacity = 0
        else:
            current_capacity += int(line)

max_capacity = max(elfs_capacity)
elf_number = elfs_capacity.index(max_capacity)

print("Max calories is {} carried by elf number {}".format(max_capacity, elf_number+1))

elfs_capacity.sort()
elfs_capacity.reverse()

print("Top 3 is, 1 : {}, 2 : {}, 3 : {}".format(elfs_capacity[0], elfs_capacity[1], elfs_capacity[2]))