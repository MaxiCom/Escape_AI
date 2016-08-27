from modules.window import *

class EscapeAI:
	def __init__(self):	
		self.window = Window();

	def addAiCharacter(self, character):
		self.window.characterList.append(character);
