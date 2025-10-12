from m04prelude import *
from m05yield import *
from m10gather__2carrot import guarantee_carrot


def guarantee_pumpkin(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Pumpkin)

	if this_num_items() >= n:
		return False

	reset_ground(Grounds.Soil)
	reset_pos()

	while this_num_items() < n * 2:
		grown_pumpkins = 0

		guarantee_amt = 2**10

		if guarantee_carrot(guarantee_amt):
			reset_ground(Grounds.Soil)

		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
				if get_water() < 0.75:
					use_item(Items.Water)

				if get_entity_type() != Entities.Pumpkin and can_harvest():
					harvest()

				if get_entity_type() == Entities.Pumpkin and can_harvest():
					grown_pumpkins += 1
				else:
					plant(Entities.Pumpkin)

				move(North)
			move(East)

		if grown_pumpkins == WS**2:
			harvest()

	return True
