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


# def par_guarantee_power(n=10000, reseted_soil_already=False):
# 	# type: (int, bool) -> bool

# 	def this_num_items():
# 		return num_items(Items.Power)

# 	if this_num_items() >= n:
# 		return False

# 	def this_reset():
# 		par_reset_ground(Grounds.Soil)
# 		reset_pos()

# 	if not reseted_soil_already:
# 		this_reset()

# 	while this_num_items() < n * 2:
# 		global d
# 		d = {}  # type: dict[int, list[tuple[int, int]]]
# 		for k in range(7, 15 + 1):
# 			d[k] = []

# 		for _ in range(WS):
# 			for _ in range(WS):
# 				# while get_water() < 0.75 and use_item(Items.Water):
# 				# 	pass

# 				if get_entity_type() not in (None, Entities.Sunflower):
# 					harvest()

# 				plant(Entities.Sunflower)
# 				d[measure()].append(get_pos())

# 				move(North)
# 			move(East)

# 		prev_drone = None

# 		for k in range(15, 7 - 1, -1):

# 			def deco(k, prev_drone):
# 				# type: (int, Any) -> Callable[[bool], None]
# 				def f(is_main, k=k, prev_drone=prev_drone):
# 					global d
# 					# type: (bool, int, Any) -> None
# 					lst = _traveling_sunflowersman(d[k])  # noqa: B023, RUF100

# 					if prev_drone != NONE:
# 						wait_for(prev_drone)

# 					for pos in lst:
# 						move_to2(pos)

# 						while not can_harvest():
# 							pass

# 						harvest()

# 				return f

# 			prev_drone = spawn_drone(deco(k, prev_drone))

# 		if prev_drone != NONE:
# 			wait_for(prev_drone)

# 	return True


def par_guarantee_power(n=10000, reseted_soil_already=False):
	# type: (int, bool) -> bool

	def this_num_items():
		return num_items(Items.Power)

	if this_num_items() >= n:
		return False

	def this_reset():
		par_reset_ground(Grounds.Soil)
		reset_pos()

	if not reseted_soil_already:
		this_reset()

	def f(n):
		inv_n = MD - n - 1
		sleep(400 * inv_n)

		lst = []  # type: list[int]
		for _ in range(WS):
			if can_harvest():
				harvest()
			else:
				sleep(200)

			plant(Entities.Sunflower)
			lst.append(measure())

			move(North)

		for v in [15, 14, 13, 12, 11, 10, 9, 8, 7]:
			for _ in range(WS):
				if measure() == v:
					harvest()
				else:
					sleep(200)

				move(North)

	while this_num_items() < n:
		await_drones(f, East)
		reset_pos()
