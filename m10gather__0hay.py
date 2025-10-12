from m04prelude import *


def guarantee_hay(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Hay)

	if this_num_items() >= n:
		return False  # skip reseting if already satisifed

	reset_pos()

	if True:
		for _ in range(WS):
			if get_ground_type() != Grounds.Grassland:
				till()
			move(North)

	while this_num_items() < n * 2:
		for _ in range(WS):
			if can_harvest():
				harvest()
			move(North)

	return True


def guarantee_hay2(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Hay)

	if this_num_items() >= n:
		return False  # skip reseting if already satisifed

	reset_pos()

	if get_ground_type() != Grounds.Grassland:
		till()

	plant(Entities.Grass)

	while this_num_items() < n * 2:
		if get_water() <= 0.95:
			use_item(Items.Water)

		if can_harvest():
			harvest()
