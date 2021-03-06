import TerminalHandler
import constants
import Timeout
from sys import stdout


class Game:
    def __init__(self, terminalHandler=stdout, debug=None):
        self.output = TerminalHandler.TerminalHandler(terminalHandler)
        self.objects = []
        self.debugHandler = debug

    def addObject(self, obj):
        self.objects.append(obj)

    def addObjects(self, objs):
        for obj in objs:
            self.addObject(obj)

    def render(self, delta, state={}):
        for obj in self.objects:
            state.update(obj.render())

        self.output.writeState(state)


            # self.output.writeAtXY(
            #     "Time since last render: {}".format(delta), 0, 0)
            #
            # self.output.writeAtXY("COORS: ", 0, 2)
            # for obj in self.objects:
            #     self.output.output.write(
            #         "{} {},{}; ".format(obj.colour, int(
            #             round(obj.pos.x)), int(round(obj.pos.y)))
            #     )

    def update(self, timeDiff):
        for obj in self.objects:
            obj.update(timeDiff)

    def start(self, updateFreq, renderFreq):
        timer = Timeout.TaskList()

        timer.addTask(Timeout.FrequentTask(
            lambda x: self.update(x), updateFreq))
        timer.addTask(Timeout.FrequentTask(
            lambda x: self.render(x), renderFreq))

        if (self.debug != None):
            timer.addTask(Timeout.FrequentTask(
                lambda x: self.debug(x), renderFreq))

        while(True):
            timer.executeNextTask()

    def cleanup(self):
        if self.debugHandler != None:
            self.debugHandler.cleanup()
        self.output.cleanup()

    def debug(self, delta, output=[]):
        output.append(('Game', ["Time since last render: {}".format(delta)]))

        if (self.debugHandler != None):
            self.debugHandler.update(output)
