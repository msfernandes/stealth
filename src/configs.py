from gi.repository import Gdk
screen = Gdk.Screen.get_default()
SCREEN_WIDTH = screen.get_width()
SCREEN_HEIGHT = screen.get_height()

BOARD_LINES = int(SCREEN_HEIGHT * 0.05)
BOARD_COLUMNS = int(SCREEN_WIDTH * 0.05)
WALLS = min(BOARD_LINES, BOARD_COLUMNS)
WALL_SIZE = min(BOARD_LINES / 6, BOARD_COLUMNS / 6)
