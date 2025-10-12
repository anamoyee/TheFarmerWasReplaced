from m04prelude import *
from m10gather__0hay import guarantee_hay
from m10gather__3tree import guarantee_wood


def guarantee_carrot(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Carrot)

	if this_num_items() >= n:
		return False  # skip reseting if already satisifed

	reset_ground(Grounds.Soil)
	reset_pos()

	while this_num_items() < n:
		guarantee_amt = 8 * (WS**2)  # 4 (carrots are four in one plot) * (WS**2)

		if guarantee_wood(guarantee_amt) or guarantee_hay(guarantee_amt):
			reset_ground(Grounds.Soil)

		for _ in range(WS):
			for _ in range(WS):
				if can_harvest():
					harvest()
				plant(Entities.Carrot)

				move(North)
			move(East)

	return True
