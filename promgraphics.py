import sys

def drawNet(column):
	sys.stdout.write(u"\u001b[24;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[23;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[20;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[19;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[16;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[15;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[12;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[11;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[8;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[7;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[4;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")
	sys.stdout.write(u"\u001b[3;"+str(column)+"H")
	print(u"\u001b[43m \u001b[0m")

	sys.stdout.flush()

def drawBars(a, b, c):
	'''Left Bar'''
	sys.stdout.write(u"\u001b["+str(a)+";3H")
	print(u"\u001b[45m \u001b[0m")
	sys.stdout.write(u"\u001b["+str(b)+";3H")
	print(u"\u001b[45m \u001b[0m")
	sys.stdout.write(u"\u001b["+str(c)+";3H")
	print(u"\u001b[45m \u001b[0m")

	'''Right Bar'''
	sys.stdout.write(u"\u001b["+str(25-a)+";77H")
	print(u"\u001b[45m \u001b[0m")
	sys.stdout.write(u"\u001b["+str(25-b)+";77H")
	print(u"\u001b[45m \u001b[0m")
	sys.stdout.write(u"\u001b["+str(25-c)+";77H")
	print(u"\u001b[45m \u001b[0m")

	sys.stdout.flush()

def score(sc_1, sc_2):
	if sc_1 == 0:
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")
		

	if sc_2 == 0:
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")
		

	if sc_1 == 1:
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")
		

	if sc_2 == 1:
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")
		

	if sc_1 == 2:
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")
		

	if sc_2 == 2:
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")
		

	if sc_1 == 3:
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")
		

	if sc_2 == 3:
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")

	if sc_1 == 4:
		sys.stdout.write(u"\u001b[2;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;31H" + u"\u001b[42m ")

	if sc_2 == 4:
		sys.stdout.write(u"\u001b[2;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;49H" + u"\u001b[42m ")

	if sc_1 == 5:
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;30H" + u"\u001b[42m ")

	if sc_2 == 5:
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;48H" + u"\u001b[42m ")

	if sc_1 == 6:
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")

	if sc_2 == 6:
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")

	if sc_1 == 7:
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")

	if sc_2 == 7:
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")

	if sc_1 == 8:
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;31H" + u"\u001b[42m ")

	if sc_2 == 8:
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;49H" + u"\u001b[42m ")

	if sc_1 == 9:
		sys.stdout.write(u"\u001b[2;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;30H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;31H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;32H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;31H" + u"\u001b[42m ")

	if sc_2 == 9:
		sys.stdout.write(u"\u001b[2;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[2;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[3;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[5;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;48H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;49H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[6;50H" + u"\u001b[42m ")
		sys.stdout.write(u"\u001b[4;49H" + u"\u001b[42m ")

	def win(player):
		if player == 1:
			pass


	sys.stdout.write(u"\u001b[0m")
	sys.stdout.flush()