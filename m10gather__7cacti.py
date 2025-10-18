from m02reset import reset_ground, reset_pos
from m04prelude import *
from m10gather__5sunflowe import guarantee_power


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


def DRONE_bg_sort_cactus():
	move_to_random()

	while True:
		for _ in range(get_world_size()):
			_sort_current_col_or_row(North)
			move(East)
			for _ in range(random() * 3 // 1):
				move(South)

		for _ in range(get_world_size()):
			_sort_current_col_or_row(East)
			move(North)
			for _ in range(random() * 3 // 1):
				move(West)


def guarantee_cucktoose(n):
	# type: (int) -> bool

	def this_reset():
		reset_ground(Grounds.Soil, Entities.Cactus)
		reset_pos()

	def this_num_items():
		return num_items(Items.Cactus)

	if this_num_items() >= n:
		return False

	if get_ground_type() != Grounds.Soil:
		this_reset()

	# guarantee_power(20000, True)

	while spawn_drone(DRONE_bg_sort_cactus):
		pass

	while this_num_items() < n * 2:
		if get_entity_type() != Entities.Cactus:
			this_reset()

		sorted_all = False

		while not sorted_all:
			sorted_all = True

			reset_pos()
			for _ in range(get_world_size()):
				if not _sort_current_col_or_row(North):
					sorted_all = False
				move(East)

			reset_pos()
			for _ in range(get_world_size()):
				if not _sort_current_col_or_row(East):
					sorted_all = False
				move(North)

		harvest()
