from m04prelude import *
from m05yield import *
from m10gather__5sunflowe import guarantee_power


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
		if guarantee_power(1000):
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
