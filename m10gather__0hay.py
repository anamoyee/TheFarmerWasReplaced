from m04prelude import *
from m10gather__5sunflowe import guarantee_power


def guarantee_hay(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Hay)

	if this_num_items() >= n:
		return False  # skip reseting if already satisifed

	def this_reset():
		reset_pos()

		for _ in range(WS):
			if get_ground_type() != Grounds.Grassland:
				till()
			move(North)

	this_reset()

	while this_num_items() < n * 2:
		if guarantee_power(1000):
			this_reset()

		for _ in range(WS):
			if can_harvest():
				harvest()
			move(North)

	return True


if False:

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
