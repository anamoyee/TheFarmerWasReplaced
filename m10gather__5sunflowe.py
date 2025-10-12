from m04prelude import *
from m05yield import *


def guarantee_sunflower(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Power)

	if this_num_items() >= n:
		return False

	reset_ground(Grounds.Soil)
	reset_pos()

	while this_num_items() < n * 2:
		d = {}  # type: dict[int, list[tuple[int, int]]]
		for k in range(7, 15 + 1):
			d[k] = []

		for _ in range(WS):
			for _ in range(WS):
				while get_water() < 0.75 and use_item(Items.Water):
					pass

				if get_entity_type() not in (None, Entities.Sunflower):
					harvest()

				plant(Entities.Sunflower)
				d[measure()].append(get_pos())

				move(North)
			move(East)

		for k in range(15, 7 - 1, -1):
			lst = d[k]

			for pos in lst:
				move_to2(pos)

				while not can_harvest():
					pass

				harvest()

	return True
