from classes import Alphabet, BackPack, getBadge

alphabet = Alphabet()
total = 0

total_badges = 0

with open('./input.txt', 'r') as all_backpack_items:
    current_squad_backpack = []
    squad_member = 0

    for backpack_items in all_backpack_items:
        current_backpack = BackPack(backpack_items.replace('\n', ''))

        total += alphabet.getLetterPriority(current_backpack.getDuplicateItem())

        # Part 2
        if (squad_member < 3):
            current_squad_backpack.append(current_backpack.getItemsSet())
            squad_member += 1

        if (squad_member == 3):
            total_badges += alphabet.getLetterPriority(getBadge(*current_squad_backpack))

            current_squad_backpack.clear()
            squad_member = 0



print("Total is {}".format(total))

print("Total Badges is {}".format(total_badges))



