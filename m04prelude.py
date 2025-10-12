from m01const import *
from m02reset import *


def get_pos():
	# type: () -> tuple[int, int]

	return (get_pos_x(), get_pos_y())


def move_to_x(x):
	# type: (int) -> None
	current_x = get_pos_x()
	dx = (x - current_x) % WS
	if dx > WS // 2:
		for _ in range(WS - dx):
			move(West)
	else:
		for _ in range(dx):
			move(East)


def move_to_y(y):
	# type: (int) -> None
	current_y = get_pos_y()
	dy = (y - current_y) % WS
	if dy > WS // 2:
		for _ in range(WS - dy):
			move(South)
	else:
		for _ in range(dy):
			move(North)


def move_to(x, y):
	# type: (int, int) -> None
	move_to_x(x)
	move_to_y(y)


def move_to2(pos):
	# type: (tuple[int, int]) -> None
	x, y = pos
	move_to(x, y)
