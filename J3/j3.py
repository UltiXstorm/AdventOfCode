from classes import Alphabet, BackPack

alphabet = Alphabet()
total = 0

with open('./input.txt', 'r') as all_backpack_items:
    for backpack_items in all_backpack_items:
        current_backpack = BackPack(backpack_items.replace('\n', ''))

        total += alphabet.getLetterPriority(current_backpack.getDuplicateItem())


print("Total is {}".format(total))



