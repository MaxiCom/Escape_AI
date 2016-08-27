from modules.childGlobalFunctions import *
import math

class Bear:
	charType = "Bear";
	color = RED;
	
	def __init__(self, (x, y)):
		self.x = x;
		self.y = y;

class Human:
	charType = "Human";
	color = BLUE;

	def __init__(self, (x, y)):
		self.x = x;
		self.y = y;

def	getNewPosition(characterList):
	bear = characterList[0];
	tmpDiff = None;

	if (len(characterList) == 1):
		return
		
	for index, human in enumerate(characterList):
		if (human.charType == "Human"):
			totalDistance = math.fabs(human.x - bear.x) + math.fabs(human.y - bear.y);
			if (tmpDiff == None or totalDistance < tmpDiff):
				indexChoosen = index;
				tmpDiff = totalDistance;
	human = characterList[indexChoosen];

	xDifference = math.fabs(human.x - bear.x);
	yDifference = math.fabs(human.y - bear.y);

	# Bear
	if (xDifference != 0 or yDifference != 0):
		if (xDifference >= yDifference):
			if (human.x < bear.x and bear.x > 0):
				bear.x -= 1;
			elif (bear.x < 1300):
				bear.x += 1;
		else:
			if (human.y < bear.y and bear.y > 0):
				bear.y -= 1;
			elif (bear.y < 700):
				bear.y += 1;
	else:
		errorMessage("Human is dead at x: " + str(human.x) + ", y: " + str(human.y));
		characterList.remove(characterList[indexChoosen]);

	"""	
	# Human
	for human in characterList:	
	
		xDifference = math.fabs(human.x - bear.x);
		yDifference = math.fabs(human.y - bear.y);
		
		if (xDifference != 0 or yDifference != 0):
			if (xDifference >= yDifference):
				if (human.y < bear.y and human.y > 0):
					human.y -= 1;
				elif (human.y < 700):
					human.y += 1;
			else:
				if (human.x < bear.x and human.x > 0):
					human.x -= 1;
				elif (human.x < 1300):
					human.x += 1;
	"""
