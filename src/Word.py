from Number import NUMBER_VALUES

LETTER_VALUES = {
	"P": [(0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2), (3,0), (4,0)],
	"L": [(0,0), (1,0), (2,0), (3,0), (4,0), (4,1), (4,2)],
	"A": [(3,2), (4,2), (0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2), (3,0), (4,0)],
	"Y": [(0,0), (0,2), (1,0), (1,2), (2,1), (3,1), (4,1)],
	"E": [(0,0), (0,1), (0,2), (1,0), (2, 0), (2,1), (3,0), (4,0), (4,1), (4,2)],
	"R": [(3,1), (4,2), (0,0), (0,1), (0,2), (1,0), (1,2), (2,0), (2,1), (2,2), (3,0), (4,0)],
	"W": [(0,0), (0,4), (1,0), (2,0), (3,0), (4,0), (3,1), (2,2), (3,3), (4,4), (3,4), (2,4), (1,4), (0,4)],
	"I": [(0,0), (0,1), (0,2), (1,1), (2,1), (3,1), (4,0), (4,1), (4,2)],
	"N": [(0,0), (0,3), (1,0), (2,0), (3,0), (4,0), (1,3), (2,3), (3,3), (4,3), (1,1), (2,2)],
	"S": [(0,0), (0,1), (0,2), (1,0), (2,0), (2,1), (4,1), (4,2), (2,2), (3,2), (4,0)],
	"!": [(0,1), (1,1), (2,1), (4,1)]
}

class Word:
    def __init__(self, value, x, y, colour):
        self.height = 5
        self.spaceWidth = 4
        self.value = value
        self.x = x
        self.y = y
        self.colour = colour

    def setValue(self, value):
        self.value = value

    def render(self):
        output = {}
        string = str(self.value)

        xOffset = 0
        for i, char in enumerate(string):
            if char == " ":
                xOffset += self.spaceWidth
                continue

            letter = NUMBER_VALUES[int(char)] if char.isdigit() else LETTER_VALUES.get(char, [])

            output.update({
                (x + self.x + xOffset, y + self.y): self.colour
                for y, x in letter
            })

            xOffset += max(letter, key=lambda x: x[1])[1] + 2

        return output

    def update(self, delta):
        pass
