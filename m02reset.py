from m01const import *


def reset_pos():
	while get_pos_y() > 0:
		move(South)
	while get_pos_x() > 0:
		move(West)


def reset_ground(ground_type, plant_=None):
	# type: (Grounds, Entities | None) -> None
	for _ in range(WS):
		for _ in range(WS):
			if get_ground_type() != ground_type:
				till()
			if plant_ != NONE:
				harvest()
				plant(plant_)
			move(North)
		move(East)


# ground: Grounds | None
def reset():
	# reset_ground(Grounds.Soil)

	reset_pos()
