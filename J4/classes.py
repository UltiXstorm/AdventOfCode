class Elf:
    def __init__(self, affectation):
        self.min = int(affectation.split('-')[0])
        self.max = int(affectation.split('-')[1])

class Pair:
    def __init__(self, pair_affectations):

        pair = pair_affectations.split(',')

        self.elf1 = Elf(pair[0])
        self.elf2 = Elf(pair[1])

    def isTotallyIn(self):
        if(self.elf1.min <= self.elf2.min <= self.elf2.max <= self.elf1.max):
            return True

        elif(self.elf2.min <= self.elf1.min <= self.elf1.max <= self.elf2.max):
            return True

        return False

    def isOverlap(self):
        if(self.elf1.min <= self.elf2.max <= self.elf1.max):
            return True

        elif(self.elf2.min <= self.elf1.max <= self.elf2.max):
            return True

        return False