#!/usr/bin/python2.7
from modules import core
from modules import ai

def	main():
	# init core
	escapeAI = core.EscapeAI();

	# init ai characters with (x, y) pos
	bear = ai.Bear((1000, 600));
	
	# Set window environment
	escapeAI.window.setEnv((1300, 700), "Escape AI");
	escapeAI.window.drawFloor();

	# Add characters
	escapeAI.addAiCharacter(bear);

	# Display window
	escapeAI.window.display();

if __name__ == "__main__":
	main();
