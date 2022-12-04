from constant import LOWER_ALPHABET, UPPER_ALPHABET

class Alphabet:
    def __init__(self):
        self.alphabet = ['', *LOWER_ALPHABET, *UPPER_ALPHABET]

    def getLetterPriority(self, letter):
        return self.alphabet.index(letter)

class BackPack:
    def __init__(self, items_list):
        total_size = len(items_list)
        part_size = int(total_size/2)

        self.all_items = items_list
        self.first_part = items_list[slice(part_size)]
        self.second_part = items_list[slice(part_size, total_size)]

    def getDuplicateItem(self):
        duplicate = []
        for item in self.first_part:
            if(self.second_part.find(item) != -1):
                duplicate.append(item)

        return duplicate[0]

    def getItemsSet(self):
        return set(self.all_items)


def getBadge(set1, set2, set3):
    for item in set1:
        if (item in set2):
            if (item in set3):
                return item