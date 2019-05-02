from TerminalHandler import TerminalHandler
import datetime

class Debugger(TerminalHandler):
    timeSinceLastUpdate = datetime.datetime.now()

    def update(self, debugArray):
        """
        arr = [
            ("Category", ['str1', 'str2']),
            ("Category1", ['str3', 'str4'])
        ]

        will print:

        Category:
            str1
            str2
        Category2:
            str3
            str4
        """

        lines = 0

        now = datetime.datetime.now()
        diff = now - self.timeSinceLastUpdate
        self.writeAtXY("Time since last debug update: {}".format(diff.total_seconds()), 0, lines * 2)
        self.timeSinceLastUpdate = now

        lines += 1

        for cat in debugArray:
            self.writeAtXY(cat[0] + ':', 0, lines * 2)
            lines += 1

            for string in cat[1]:
                self.writeAtXY('    ' + string, 0, lines * 2)
                lines += 1
