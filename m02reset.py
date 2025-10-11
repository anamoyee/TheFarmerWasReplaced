from m01const import *


def reset_pos():
	while get_pos_y() > 0:
		move(South)
	while get_pos_x() > 0:
		move(West)


def reset_ground(ground_type):
	# type: (Grounds) -> None
	for _ in range(WS):
		for _ in range(WS):
			if get_ground_type() != ground_type:
				till()
			move(North)
		move(East)


# ground: Grounds | None
def reset():
	# reset_ground(Grounds.Soil)

	reset_pos()
