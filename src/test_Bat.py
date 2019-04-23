from Bat import Bat
from TerminalHandler import TerminalHandler
from Game import Game
import Timeout


game = Game(True)
game.addObject(Bat(4, 10, 2, 'red'))
game.addObject(Bat(1, 20, 2, 'red'))
game.addObject(Bat(6, 3, 10, 'blue', 1, 5))

game.start(100, 60)