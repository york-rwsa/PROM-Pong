import TerminalHandler
import time

handler = TerminalHandler.TerminalHandler()

state = {
    (1, 2): 'red',
    (3, 5): 'blue',
    (5, 7): 'green'
}

newState = {
    (1, 2): 'blue',
    (3, 5): 'green',
    (5, 10): 'green'
}

handler.writeState(state)

time.sleep(2)

handler.writeState(newState)

while(True):
    pass
