from m04prelude import *
from m05yield import *


def _traveling_sunflowersman(lst):
	# type: (list[tuple[int, int]]) -> list[tuple[int, int]]
	if not lst:
		return []
	start_x, start_y = get_pos()
	ordered = []
	remaining = lst[:]
	current_x, current_y = start_x, start_y

	while remaining:
		best_i = 0
		best_dist = 999999999
		i = 0
		while i < len(remaining):
			x, y = remaining[i]
			dx = x - current_x
			dy = y - current_y
			if dx < 0:
				dx = -dx
			if dy < 0:
				dy = -dy
			dist = dx + dy
			if dist < best_dist:
				best_dist = dist
				best_i = i
			i += 1

		nx, ny = remaining[best_i]
		ordered.append((nx, ny))
		remaining.pop(best_i)
		current_x, current_y = nx, ny

	return ordered


def guarantee_power(n, reseted_soil_already=False):
	# type: (int, bool) -> bool

	def this_num_items():
		return num_items(Items.Power)

	if this_num_items() >= n:
		return False

	def this_reset():
		reset_ground(Grounds.Soil)
		reset_pos()

	if not reseted_soil_already:
		this_reset()

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
			lst = _traveling_sunflowersman(d[k])

			for pos in lst:
				move_to2(pos)

				while not can_harvest():
					pass

				harvest()

	return True
