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

  def win(self):
    self.score += SCORE[WIN]

  def draw(self):
    self.score += SCORE[DRAW]

  def lose(self):
    self.score += SCORE[LOSE]
