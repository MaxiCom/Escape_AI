from modules.childGlobalFunctions import *
from modules import ai
import pygame
import sys


class Window:
	characterList = [];

	def __init__(self):
		# init pygame
		pygame.init();
		successMessage("Init pygame ...");

	def setEnv(self, sizeTuple, windowName):
		self.window = pygame.display.set_mode(sizeTuple, 0, 32);
		pygame.display.set_caption(windowName);
		successMessage("Set window environment ...");
	
	def drawFloor(self):
		self.window.fill(WHITE);

	def drawCharacter(self, character):
		pygame.draw.circle(self.window, character.color, (character.x, character.y), 5, 0);

	def	display(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					errorMessage("Window closed ...");
					pygame.quit();
					sys.exit();
			
				if event.type == pygame.MOUSEBUTTONUP:
						mPos = pygame.mouse.get_pos();
				
						self.characterList.append(ai.Human((mPos[0], mPos[1])));
						successMessage("Human is born at x: " + str(mPos[0]) \
						+ ", y: " + str(mPos[1]));
			
			self.drawFloor();

			ai.getNewPosition(self.characterList);
			for character in self.characterList:
				self.drawCharacter(character);

			pygame.display.update();
