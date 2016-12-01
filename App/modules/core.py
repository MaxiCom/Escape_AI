from modules.window import *

class EscapeAI:
	characterList = [];

	def __init__(self):	
		self.window = Window();
		self.window.setParent(self);

	def addAiCharacter(self, character):
		self.characterList.append(character);
