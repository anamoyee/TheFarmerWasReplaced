from m04prelude import *
from m05yield import *
from m10gather__5sunflowe import par_guarantee_power


def guarantee_wood(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Wood)

	if this_num_items() >= n:
		return False

	def this_reset():
		# reset_ground(Grounds.Grassland)
		reset_pos()

	this_reset()

	while this_num_items() < n * 2:
		if par_guarantee_power(1000):
			this_reset()

		for _ in range(WS):
			for _ in range(WS):
				if (get_pos_x() + 2 * get_pos_y()) % 4 != 3:
					if can_harvest():
						harvest()
					plant(Entities.Tree)
					if get_water() < 0.75:
						use_item(Items.Water)
				else:
					# yield_spot_bush()
					pass
				move(North)
			move(East)

	return True


def _wood_num_items():
	return num_items(Items.Wood)


def _wood_reset():
	par_reset_ground(Grounds.Soil)


def _wood_col_reset():
	col_reset_ground(Grounds.Soil)


def col_guarantee_wood(n):
	if _wood_num_items() >= n:
		return False  # skip reseting if already satisifed

	_wood_col_reset()

	_col_guarantee_wood_unchecked(n * 2)

	return True


def _col_guarantee_wood_unchecked(n):
	while _wood_num_items() < n:
		for _ in range(WS):
			if can_harvest():
				harvest()
			water_until(0.5)
			if (get_pos_x() + get_pos_y()) % 2 == 0:
				plant(Entities.Tree)
			else:
				plant(Entities.Bush)
			move(North)


def par_guarantee_wood(n):
	if _wood_num_items() >= n:
		return False  # skip reseting if already satisifed

	_wood_reset()

	def f(is_main):
		# type: (bool) -> None
		_col_guarantee_wood_unchecked(n * 2)

	await_drones(f, East)

	return True
