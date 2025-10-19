from m02reset import reset_ground, reset_pos
from m04prelude import *
from m10gather__4pumpkins import par_guarantee_pumpkin
from m10gather__5sunflowe import par_guarantee_power


def get_pos_of_dir(direction):
	# type: (Direction) -> int
	if direction in (North, South):
		return get_pos_y()
	elif direction in (East, West):
		return get_pos_x()

	err_while1(__name__, "get_pos_of_dir: Invalid direction:", direction)


def _sort_current_col_or_row(primary_direction):
	# type: (Direction) -> bool
	consecutive_okays = 0

	already_sorted = True

	while consecutive_okays < WS:
		if primary_direction == North and get_pos_y() == WS - 1:
			move(primary_direction)
		if primary_direction == East and get_pos_x() == WS - 1:
			move(primary_direction)

		val_souther = measure()  # type: int
		move(primary_direction)
		val_current = measure()  # type: int

		if val_souther > val_current:
			already_sorted = False
			swap(dir180(primary_direction))
			for _ in range(min(2, get_pos_of_dir(primary_direction))):
				move(dir180(primary_direction))
			consecutive_okays = 0
		else:
			consecutive_okays += 1

	return already_sorted


def par_guarantee_cucktoose(n):
	# type: (int) -> bool

	def _cucktoose_reset():
		par_reset_ground(Grounds.Soil, Entities.Cactus)
		reset_pos()

	def this_num_items():
		return num_items(Items.Cactus)

	if this_num_items() >= n:
		return False

	if get_ground_type() != Grounds.Soil:
		_cucktoose_reset()

	# guarantee_power(20000, True)

	while this_num_items() < n * 2:
		guarantee_amt = 4 * calculate_crop_cost_for_entity_including_hardcoded_multipliers_for_full_field(Entities.Cactus)

		par_guarantee_pumpkin(guarantee_amt, True)

		_cucktoose_reset()

		def f_col(is_main):
			_sort_current_col_or_row(North)

		def f_row(is_main):
			_sort_current_col_or_row(East)

		await_drones(f_col, East)
		await_drones(f_row, North)

		harvest()
