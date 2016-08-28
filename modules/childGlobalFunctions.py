# CONSTANTS
WINDOW_WIDTH = 1300;
WINDOW_HEIGHT = 700;
WINDOW_NAME = "Escape AI";

BEAR_SPEED = 3;
HUMAN_SPEED = 1;

WHITE = (255, 255, 255);
BLACK = (0, 0, 0);
BLUE = (0, 0, 255);
RED = (255, 0, 0);


def successMessage(message):
	print ("\033[32m%s\033[m" % message);

def errorMessage(message):
	print ("\033[31m%s\033[m" % message);
