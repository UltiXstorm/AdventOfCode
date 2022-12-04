from constant import *

class Player:
  def __init__(self, rock, paper, scissors):
    self.rock = rock
    self.paper = paper
    self.scissors = scissors

    self.score = 0

  def play(self, letter):
    if(letter == self.rock):
      self.score += SCORE[ROCK]
      return ROCK

    elif(letter == self.paper):
      self.score += SCORE[PAPER]
      return PAPER

    elif(letter == self.scissors):
      self.score += SCORE[SCISSORS]
      return SCISSORS

  def playV2(self, player_letter, opponent_play):
      if(opponent_play == ROCK):
          if(player_letter == 'X'):
              self.score += SCORE[SCISSORS]
              return SCISSORS
          elif(player_letter == 'Y'):
              self.score += SCORE[ROCK]
              return ROCK
          elif(player_letter == 'Z'):
              self.score += SCORE[PAPER]
              return PAPER

      elif(opponent_play == PAPER):
          if(player_letter == 'X'):
              self.score += SCORE[ROCK]
              return ROCK
          elif(player_letter == 'Y'):
              self.score += SCORE[PAPER]
              return PAPER
          elif(player_letter == 'Z'):
              self.score += SCORE[SCISSORS]
              return SCISSORS

      elif(opponent_play == SCISSORS):
          if(player_letter == 'X'):
              self.score += SCORE[PAPER]
              return PAPER
          elif(player_letter == 'Y'):
              self.score += SCORE[SCISSORS]
              return SCISSORS
          elif(player_letter == 'Z'):
              self.score += SCORE[ROCK]
              return ROCK

  def win(self):
    self.score += SCORE[WIN]

  def draw(self):
    self.score += SCORE[DRAW]

  def lose(self):
    self.score += SCORE[LOSE]
