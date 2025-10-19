from m04prelude import *
from m10gather__0hay import col_guarantee_hay, guarantee_hay
from m10gather__3tree import col_guarantee_wood, guarantee_wood
from m10gather__5sunflowe import par_guarantee_power


def guarantee_carrot(n, reseted_soil_already=False):
	# type: (int, bool) -> bool

	def this_num_items():
		return num_items(Items.Carrot)

	if this_num_items() >= n:
		return False  # skip reseting if already satisifed

	def this_reset():
		reset_ground(Grounds.Soil)
		reset_pos()

	if not reseted_soil_already:
		this_reset()

	while this_num_items() < n:
		guarantee_amt = 4 * calculate_crop_cost_for_entity_including_hardcoded_multipliers_for_full_field(Entities.Carrot)

		if guarantee_wood(guarantee_amt) or guarantee_hay(guarantee_amt) or par_guarantee_power(1000):
			this_reset()

		for _ in range(WS):
			for _ in range(WS):
				if can_harvest():
					harvest()
				plant(Entities.Carrot)

				move(North)
			move(East)

	return True


def _carrot_num_items():
	return num_items(Items.Carrot)


def _carrot_reset():
	par_reset_ground(Grounds.Soil)


def _carrot_col_reset():
	col_reset_ground(Grounds.Soil)


def col_guarantee_carrot(n, reseted_ground_already=False):
	if _carrot_num_items() >= n:
		return False  # skip reseting if already satisifed

	if not reseted_ground_already:
		_carrot_col_reset()

	_col_guarantee_carrot_unchecked(n * 2)

	return True


def _col_guarantee_carrot_unchecked(n):
	while _carrot_num_items() < n:
		guarantee_amt = 25 * calculate_crop_cost_for_entity_including_hardcoded_multipliers_for_full_field(Entities.Carrot)

		if any((col_guarantee_wood(guarantee_amt), col_guarantee_hay(guarantee_amt))):
			_carrot_col_reset()

		for _ in range(WS):
			if can_harvest():
				harvest()
			water_until(0.5)
			plant(Entities.Carrot)
			move(North)


def par_guarantee_carrot(n, reseted_ground_already=False):
	if _carrot_num_items() >= n:
		return False  # skip reseting if already satisifed

	if not reseted_ground_already:
		_carrot_reset()

	def f(is_main):
		# type: (bool) -> None

		col_guarantee_carrot(n)

	await_drones(f, East)

	return True
