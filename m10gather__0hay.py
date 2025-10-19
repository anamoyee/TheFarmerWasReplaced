from m04prelude import *
from m10gather__5sunflowe import par_guarantee_power


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
		if par_guarantee_power(1000):
			this_reset()

		for _ in range(WS):
			if can_harvest():
				harvest()
			move(North)

	return True


def _hay_num_items():
	return num_items(Items.Hay)


def _hay_reset():
	clear()


def _col_hay_reset():
	for _ in range(WS):
		if get_ground_type() != Grounds.Grassland:
			till()
		move(North)


def _col_guarantee_hay_unchecked(n):
	while _hay_num_items() < n:
		for _ in range(WS):
			harvest()
			move(North)


def col_guarantee_hay(n):
	if _hay_num_items() >= n:
		return False  # skip reseting if already satisifed

	_col_hay_reset()

	_col_guarantee_hay_unchecked(n * 2)

	return True


def par_guarantee_hay(n):
	if _hay_num_items() >= n:
		return False  # skip reseting if already satisifed

	_hay_reset()

	def f(is_main):
		# type: (bool) -> None
		_col_guarantee_hay_unchecked(n * 2)

	await_drones(f, East)

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
