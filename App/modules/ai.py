from modules.childGlobalFunctions import *
import math

class Bear:
	charType = "Bear";
	color = RED;
	speed = BEAR_SPEED;
	
	def __init__(self, (x, y)):
		self.x = x;
		self.y = y;

class Human:
	charType = "Human";
	color = BLUE;
	speed = HUMAN_SPEED;

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
	if (xDifference + yDifference > 5):
		if (xDifference >= yDifference):
			if (human.x < bear.x and bear.x > 0):
				bear.x -= bear.speed;
			elif (bear.x < WINDOW_WIDTH):
				bear.x += bear.speed;
		else:
			if (human.y < bear.y and bear.y > 0):
				bear.y -= bear.speed;
			elif (bear.y < WINDOW_HEIGHT):
				bear.y += bear.speed;
	else:
		errorMessage("Human is dead at x: " + str(human.x) + ", y: " + str(human.y));
		characterList.remove(characterList[indexChoosen]);

	# Human
	for human in characterList:	
	
		xDifference = math.fabs(human.x - bear.x);
		yDifference = math.fabs(human.y - bear.y);

		if (xDifference + yDifference > 5):
			if (xDifference >= yDifference):
				if (human.y < bear.y and human.y > 0):
					human.y -= human.speed;
				elif (human.y < WINDOW_HEIGHT):
					human.y += human.speed;
			else:
				if (human.x < bear.x and human.x > 0):
					human.x -= human.speed;
				elif (human.x < WINDOW_WIDTH):
					human.x += human.speed;
