from m04prelude import *
from m10gather__0hay import guarantee_hay
from m10gather__3tree import guarantee_wood
from m10gather__5sunflowe import guarantee_power


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
		guarantee_amt = 2**10

		if guarantee_wood(guarantee_amt) or guarantee_hay(guarantee_amt) or guarantee_power(1000):
			this_reset()

		for _ in range(WS):
			for _ in range(WS):
				if can_harvest():
					harvest()
				plant(Entities.Carrot)

				move(North)
			move(East)

	return True
