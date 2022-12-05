import re
from classes import Ship, Pile

iteration = 1
piles = 9

ship = Ship()

with open('./input.txt', 'r') as piles_and_moves:
    for piles_or_move in piles_and_moves:
        if(iteration < 9):
            ship.setupInitLine(piles_or_move)
            print("###")
            print("1 : {}".format(ship.ship[1]))
            print("2 : {}".format(ship.ship[2]))
            print("3 : {}".format(ship.ship[3]))
            print("4 : {}".format(ship.ship[4]))
            print("5 : {}".format(ship.ship[5]))
            print("6 : {}".format(ship.ship[6]))
            print("7 : {}".format(ship.ship[7]))
            print("8 : {}".format(ship.ship[8]))
            print("9 : {}".format(ship.ship[9]))

        if(iteration > 10):
            ship.doMoveV2(piles_or_move.replace('\n', ''))

        iteration += 1


    print(ship.getAllTop())

