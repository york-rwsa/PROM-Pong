from sys import stdout

COLOURS = {
  "reset": 0,
  "black": 40,
  "red": 41,
  "green": 42,
  "yellow": 43,
  "blue": 44,
  "pink": 45,
  "cyan": 46,
  "white": 47
}

class TerminalHandler:
  def __init__ (self, output_device = stdout):
    self.previousState = {}
    self.output = output_device
    self.blankOut = " "

    self.initDisplay()
  
  def hideCursor (self):
    self.output.write(u"\u001b[?25l")
  
  def showCursor (self):
    self.output.write(u"\u001b[?25h")
  
  def clearDisplay (self):
    self.output.write(u"\u001b[2J")
  
  def setCursorPos(self, x, y):
    self.output.write(u"\u001b[{};{}f".format(y, x))
  
  def setColour(self, colour):
    self.output.write(u"\u001b[{}m".format(COLOURS[colour]))

  def resetColour(self):
    self.output.write(u"\u001b[0m")
  
  def flush(self):
    self.output.flush()
  
  def writeAtXY(self, string, x, y, bgcolour="reset"):
    self.resetColour()    
    self.setCursorPos(x, y)
    self.setColour(bgcolour)
    
    self.output.write(string)

  def initDisplay(self):
    self.resetColour()
    self.clearDisplay()
    self.hideCursor()
    self.flush()

  def resetDisplay(self):
    self.resetColour()
    self.clearDisplay()
    self.setCursorPos(0, 0)
    self.flush()
  
  def drawPixel(self, x, y, colour):
    self.writeAtXY(self.blankOut, x, y, colour)
  
  def writeState(self, state):
    # state = { (x, y): "colourName" }
    # removed is the set of Vecors that are no longer displayed 
    
    removed = set(self.previousState.keys()) - set(state.keys())
    updated = { coors for (coors, colour) in state.items() if colour != self.previousState.get(coors) }

    for (x, y) in removed:
      self.drawPixel(x, y, 'reset')
    
    for (x, y) in updated:
      self.drawPixel(x, y, state[(x, y)])
  
    self.previousState = state
    self.flush()