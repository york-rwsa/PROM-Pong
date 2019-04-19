import time, sys, curses, threading, promgraphics

stdscr = curses.initscr()
curses.curs_set(0) #Hides cursor 
curses.noecho()
curses.cbreak()

x = 1
y = 12

a = 22
b = 23
c = 24

score_un = 0
score_deux = 0

right = True;
up = True;

goingDown = False
goingUp = False

def loading(): #Shows a fancy loadng screen
	print(u"\u001b[2J")
	sys.stdout.write(u"\u001b[10;35H\u001b[0m")
	print("Loading...")
	sys.stdout.write(u"\u001b[12;19H")
	print("[" + " "*40 + "]")
	for i in range(1, 41):
		sys.stdout.write(u"\u001b[30m")
		sys.stdout.write(u"\u001b[12;19H")
		sys.stdout.write(u"\u001b[12;"+str(19+i)+"H" + u"\u001b[46m ")
		time.sleep(.02)
		sys.stdout.flush()

	sys.stdout.write(u"\u001b[0m")
	sys.stdout.write(u"\u001b[14;35H")
	print("Finished!")
	sys.stdout.flush()
	time.sleep(1)

def moveBars(linein):
	if linein == a:
		a-=1
		a-=2
		c-=3

def mainLoop(x=1, y=12, a=22, b=23, c=24, score1=0, score2=0, right=True, up=True, goingDown=False, goingUp=True):
	loading()
	while (True):
	
		if x == 80:
			right = False
			score1+=1
		if y == 24:
			up = True
		if x == 1:
			right = True
			score2+=1
		if y == 1:
			up = False
			
		if right:
			x+=1
		if up:
			y-=1
		if not right:
			x-=1
		if not up:
			y+=1

		if c == 24:
			goingDown = False
			goingUp = True
		if a == 1:
			goingDown = True
			goingUp = False

		'''
		if goingUp == True:
			a-=1
			b-=1
			c-=1
		if goingDown == True:
			a+=1
			b+=1
			c+=1
		'''
		

		if score1 == 10:
			promgraphics.win(1)
		if score2 == 10:
			promgraphics.win(2)

		promgraphics.drawBars(a, b, c)
		promgraphics.drawNet(40)
		promgraphics.score(score1, score2)

		sys.stdout.write(u"\u001b["+str(y)+";"+str(x)+"H")
		print(u"\u001b[46m \u001b[0m")
		sys.stdout.flush()
		
		time.sleep(.05)
		print(u"\u001b[2J")
try:
	mainLoop()
except KeyboardInterrupt:
	curses.endwin()
	print(u"\u001b[2J")
	


		