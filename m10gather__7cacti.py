from m02reset import reset_ground, reset_pos
from m04prelude import *
from m10gather__5sunflowe import guarantee_power


def _sort_current_col_or_row(primary_direction):
	# type: (Direction) -> None
	consecutive_okays = 0

	while consecutive_okays < WS:
		if primary_direction == North and get_pos_y() == WS - 1:
			move(primary_direction)
		if primary_direction == East and get_pos_x() == WS - 1:
			move(primary_direction)

		val_souther = measure()  # type: int
		move(primary_direction)
		val_current = measure()  # type: int

		if val_souther < val_current:
			swap(dir180(primary_direction))
			for _ in range(2):
				move(dir180(primary_direction))
			consecutive_okays = 0
		else:
			consecutive_okays += 1


def guarantee_cucktoose(n):
	# type: (int) -> bool

	def this_reset():
		reset_ground(Grounds.Soil, Entities.Cactus)
		reset_pos()

	def this_num_items():
		return num_items(Items.Cactus)

	if this_num_items() >= n:
		return False

	this_reset()

	while this_num_items() < n * 2:
		if guarantee_power(10000, True):
			this_reset()

		for _ in range(WS):
			_sort_current_col_or_row(North)
			move(East)

		reset_pos()

		for _ in range(WS):
			_sort_current_col_or_row(East)
			move(North)

		reset_pos()
		harvest()
