#!/usr/bin/python2.7
from modules import core
from modules import ai
from modules.childGlobalFunctions import *
from random import randint

def	main():
	# init core
	escapeAI = core.EscapeAI();

	# init ai bear with (x, y) pos
	bear = ai.Bear((randint(50, 1250), randint(50, 650)));
	
	# Set window environment
	escapeAI.window.setEnv((WINDOW_WIDTH, WINDOW_HEIGHT), WINDOW_NAME);

	# Add the bear and display window
	escapeAI.addAiCharacter(bear);
	escapeAI.window.display();

if __name__ == "__main__":
	main();
