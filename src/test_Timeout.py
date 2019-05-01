from Game import Game
from GameObject import GameObject
import time
import Timeout

# timer = Timeout.TaskList()
# timer.addTask(Timeout.FrequentTask(lambda x: print(x), 10))

game = Game()

obj1 = GameObject()
obj1.size.setxy(2, 1)
obj1.velocity.setxy(2, -1)
obj1.pos.setxy(10, 12)
obj1.colour = "pink"
game.addObject(obj1)

obj2 = GameObject()
obj2.pos.setxy(10, 3)
obj2.size.setxy(5, 3)
obj2.velocity.setxy(20, 0)
obj2.colour = "red"
game.addObject(obj2)

timer = Timeout.TaskList()
timer.addTask(Timeout.FrequentTask(lambda x: game.update(x), 100))
timer.addTask(Timeout.FrequentTask(lambda x: game.render(x), 60))

while(True):
    timer.executeNextTask()
