from classes import Path, Arborescence

path = Path()
arbo = Arborescence()

with open('./input.txt', 'r') as commands_list:
    for raw_command in commands_list:
        command = raw_command.replace('\n', '').split(" ")

        # Command case
        if command[0] == '$':
            # Change Directory case
            if command[1] == 'cd':
                path.doChangeDirectory(command[2])

            elif command[1] == 'ls':
                continue

        elif command[0] != 'dir':
            arbo.addItem(command[1], int(command[0]), path.getCurrentPath())


print(arbo)
print(arbo.part1())