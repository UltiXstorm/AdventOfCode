from classes import Player
from constant import ROCK, PAPER, SCISSORS

opponent = Player('A', 'B', 'C')
player = Player('X', 'Y', 'Z')

def roundMatch(opponent: Player, player: Player, opponent_letter: str, player_letter: str):
    print("Opponent : {}, Player : {}".format(opponent_letter, player_letter))
    opponent_play = opponent.play(opponent_letter)
    player_play = player.playV2(player_letter, opponent_play)

    print("Opponent : {}, Player : {}".format(opponent_play,player_play))

    if(opponent_play == ROCK):
        if(player_play == ROCK):
            opponent.draw()
            player.draw()
            print("It's a draw")
        elif(player_play == PAPER):
            opponent.lose()
            player.win()
            print("Player Win")
        elif(player_play == SCISSORS):
            opponent.win()
            player.lose()
            print("Player Lose")

    elif(opponent_play == PAPER):
        if(player_play == ROCK):
            opponent.win()
            player.lose()
            print("Player Lose")
        elif(player_play == PAPER):
            opponent.draw()
            player.draw()
            print("It's a draw")
        elif(player_play == SCISSORS):
            opponent.lose()
            player.win()
            print("Player Win")

    elif(opponent_play == SCISSORS):
        if(player_play == ROCK):
            opponent.lose()
            player.win()
            print("Player Win")
        elif(player_play == PAPER):
            opponent.win()
            player.lose()
            print("Player Lose")
        elif(player_play == SCISSORS):
            opponent.draw()
            player.draw()
            print("It's a draw")


with open('./input.txt', 'r') as rps_game:
    for round in rps_game:
        opponent_letter, player_letter = round.replace('\n', '').split(' ')
        roundMatch(opponent, player, opponent_letter, player_letter)

print(player.score)