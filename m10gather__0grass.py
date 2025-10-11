from m04prelude import *


def some_grass(n):
	# type: (int) -> None
	reset_ground()
	reset_pos()

	for _ in range(WS):
		move(North)

	for _ in range(n):
		for _ in range(WS):
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				if can_harvest():
					harvest()
				plant(Entities.Tree)
			move(North)
