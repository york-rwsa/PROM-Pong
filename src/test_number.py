from Number import Number
from TerminalHandler import TerminalHandler
from Game import Game

number = Number(4, 10, 2, 'red')
print(number.render())

game = Game()
game.addObject(Number(4, 10, 2, 'red'))
game.addObject(Number(1, 20, 2, 'red'))
game.addObject(Number(123, 3, 10, 'blue'))

game.render(0)

while(True):
    pass
