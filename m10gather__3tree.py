from m04prelude import *
from m05yield import *


def guarantee_wood(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Wood)

	if this_num_items() >= n:
		return False

	reset_ground(Grounds.Grassland)
	reset_pos()

	while this_num_items() < n:
		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
				if (get_pos_x() + get_pos_y()) % 2 == 0:
					if can_harvest():
						harvest()
					plant(Entities.Tree)
				else:
					yield_spot_bush()
				move(North)
			move(East)

	return True
