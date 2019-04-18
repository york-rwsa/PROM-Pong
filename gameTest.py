from Game import Game
from GameObject import GameObject
import time

game = Game()

obj1 = GameObject()
obj1.size.setxy(2, 2)
obj1.velocity.setxy(2, -1)
obj1.pos.setxy(10, 12)
obj1.colour = "blue"
game.addObject(obj1)

obj2 = GameObject()
obj2.size.setxy(1, 1)
obj2.velocity.setxy(1, 1)
obj2.colour = "red"
game.addObject(obj2)

prev_time = time.time()
while(True):
  cur_time = time.time()

  game.update(cur_time - prev_time)
  game.render()

  prev_time = cur_time