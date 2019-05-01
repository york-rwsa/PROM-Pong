# from https://stackoverflow.com/questions/10154568/postpone-code-for-later-execution-in-python-like-settimeout-in-javascript

import time
import heapq


class FrequentTask:
    """ function takes timedelta as first argument
    """

    def __init__(self, function, frequency, *args):
        self.function = function
        self.args = args
        self.period = 1.0 / frequency
        self.lastRun = time.time()
        self.nextRun = time.time()

    def execute(self, timeDelta):
        self.function(timeDelta, *self.args)

    def __lt__(self, other):
        return self.nextRun < other.nextRun


class TaskList:
    def __init__(self):
        self.tasks = []

    def addTask(self, task):
        heapq.heappush(self.tasks, (task.nextRun, task))

    def executeNextTask(self):
        task = heapq.heappop(self.tasks)[1]
        timeNow = time.time()
        if (task and timeNow > task.nextRun):
            task.execute(timeNow - task.lastRun)
            task.lastRun = time.time()
            task.nextRun = task.lastRun + task.period

        self.addTask(task)
