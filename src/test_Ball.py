from Bat import Bat
from Ball import Ball
from TerminalHandler import TerminalHandler, COLOURS
from Game import Game
from GameObject import GameObject
import Timeout
import random

bats = [Bat(10 + i * 12, 4, 3 + i*3, random.choice(["red", "green", "blue"])) for i in range(4)]

edges = [
  GameObject(5, 5, 50, 1,'pink'),
  GameObject(5, 29, 50, 1,'pink'),
  GameObject(5, 5, 1, 30,'pink'),
  GameObject(55, 5, 1, 30,'pink')
]

balls = [
  Ball(10, 20, 10, 'red', bats + edges, 65, 2, 1),
  Ball(18, 10, 15, 'blue', bats + edges, 120, 2, 1),
  Ball(20, 15, 20, 'green', bats + edges, 100, 2, 1)
]

game = Game(True)
for obj in bats + edges + balls:
  game.addObject(obj)


game.addObject(Ball(18, 20, 15, 'yellow', bats + edges + balls, 65, 2, 1))

game.start(100, 60)