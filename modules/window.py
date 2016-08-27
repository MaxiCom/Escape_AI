from modules.childGlobalFunctions import *
from modules import ai
import pygame
import sys

class Window:
	def __init__(self):
		# init pygame
		pygame.init();
		successMessage("Init pygame ...");

	def setParent(self, parentObject):
		self.parentObject = parentObject;

	def setEnv(self, sizeTuple, windowName):
		self.window = pygame.display.set_mode(sizeTuple, 0, 32);
		pygame.display.set_caption(windowName);
		successMessage("Set window environment ...");
	
	def drawCharacter(self, character):
		font = pygame.font.Font(None, 20);
		text = font.render(character.charType, 1, (10, 10, 10));

		pygame.draw.circle(self.window, character.color, (character.x, character.y), 5, 0);
		self.window.blit(text, (character.x - 15, character.y - 20));
		

	def	display(self):
		while True:
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					errorMessage("Window closed ...");
					pygame.quit();
					sys.exit();
			
				if event.type == pygame.MOUSEBUTTONUP:
					mPos = pygame.mouse.get_pos();
				
					self.parentObject.characterList.append(ai.Human((mPos[0], mPos[1])));
					successMessage("Human is born at x: " + str(mPos[0]) \
					+ ", y: " + str(mPos[1]));
			
			self.window.fill(WHITE);

			ai.getNewPosition(self.parentObject.characterList);
			for character in self.parentObject.characterList:
				self.drawCharacter(character);

			pygame.display.update();
