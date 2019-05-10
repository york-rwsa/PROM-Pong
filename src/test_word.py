from Word import Word
from TerminalHandler import TerminalHandler
from Game import Game

w = Word("PLAYER 1 WINS!", 12, 10, "red")
print(w.render())

game = Game()
game.addObject(w)
game.render(0)

while(True):
    pass
