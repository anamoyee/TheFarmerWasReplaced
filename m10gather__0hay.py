from m04prelude import *


def guarantee_hay(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Hay)

	if this_num_items() >= n:
		return False  # skip reseting if already satisifed

	reset_ground(Grounds.Grassland, Entities.Grass)
	reset_pos()

	while this_num_items() < n:
		for _ in range(WS):
			if can_harvest():
				harvest()
			move(North)

	return True
