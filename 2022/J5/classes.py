class Pile:
    def __init__(self):
        self.pile = []

    def init(self, letter):
        self.pile.insert(0, letter)

    def empile(self, letter):
        self.pile.append(letter)

    def empileV2(self, letters):
            self.pile.extend(letters)

    def depile(self):
        return self.pile.pop(-1)

    def getTop(self):
        return self.pile[-1]

    def __str__(self):
        return '{}'.format(self.pile)

class Ship:
    def __init__(self):
        self.ship = {
            1: Pile(),
            2: Pile(),
            3: Pile(),
            4: Pile(),
            5: Pile(),
            6: Pile(),
            7: Pile(),
            8: Pile(),
            9: Pile()
        }

    def setupInitLine(self, initLine):
        self.ship[1].init(initLine[1])
        if(len(initLine) > 6 and initLine[5] != ' '):
            self.ship[2].init(initLine[5])
        if(len(initLine) > 10 and initLine[9] != ' '):
            self.ship[3].init(initLine[9])
        if(len(initLine) > 14 and initLine[13] != ' '):
            self.ship[4].init(initLine[13])
        if(len(initLine) > 18 and initLine[17] != ' '):
            self.ship[5].init(initLine[17])
        if(len(initLine) > 22 and initLine[21] != ' '):
            self.ship[6].init(initLine[21])
        if(len(initLine) > 26 and initLine[25] != ' '):
            self.ship[7].init(initLine[25])
        if(len(initLine) > 30 and initLine[29] != ' '):
            self.ship[8].init(initLine[29])
        if(len(initLine) > 34 and initLine[33] != ' '):
            self.ship[9].init(initLine[33])

    def doMove(self, lineMove):
        data = lineMove.split(' ')
        nb_move = int(data[1])
        sender = int(data[3])
        receiver = int(data[5])

        for i in range(nb_move):
            object = self.ship[sender].depile()

            self.ship[receiver].empile(object)

    def doMoveV2(self, lineMove):
            data = lineMove.split(' ')
            nb_move = int(data[1])
            sender = int(data[3])
            receiver = int(data[5])

            transport_pile = []
            for i in range(nb_move):
                transport_pile.append(self.ship[sender].depile())

            transport_pile.reverse()
            self.ship[receiver].empileV2(transport_pile)

    def getAllTop(self):
        allTop = []
        for pileNB in self.ship:
            allTop.append(self.ship[pileNB].getTop())
        return allTop
