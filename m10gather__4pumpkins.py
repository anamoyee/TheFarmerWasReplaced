from m04prelude import *
from m05yield import *
from m10gather__2carrot import col_guarantee_carrot, guarantee_carrot
from m10gather__5sunflowe import par_guarantee_power


def guarantee_pumpkin(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Pumpkin)

	if this_num_items() >= n:
		return False

	def this_reset():
		reset_ground(Grounds.Soil)
		reset_pos()

	this_reset()
	par_guarantee_power(10000, True)

	while this_num_items() < n * 2:
		grown_pumpkins = 0

		guarantee_amt = 2**10

		if guarantee_carrot(guarantee_amt) or par_guarantee_power(5000, True):
			this_reset()

		PUMPKIN_SIDELENGTH = 9
		YIELDED_SIDELENGTH = 3
		YIELD_FN = yield_spot_carrot
		DO_WATERING = False

		all_sidelength = PUMPKIN_SIDELENGTH + YIELDED_SIDELENGTH

		if all_sidelength > WS:
			err_while1(__name__, "Invalid config: all_sidelength > WS")

		for _ in range(all_sidelength):
			for _ in range(all_sidelength):
				if DO_WATERING and get_water() < 0.75:
					use_item(Items.Water)

				if get_pos_x() < PUMPKIN_SIDELENGTH and get_pos_y() < PUMPKIN_SIDELENGTH:  # optimal yield pumpkin
					if get_entity_type() != Entities.Pumpkin and can_harvest():
						harvest()

					if get_entity_type() == Entities.Pumpkin and can_harvest():
						grown_pumpkins += 1
					else:
						plant(Entities.Pumpkin)
				else:
					YIELD_FN()

				move(North)
			move_to(get_pos_x() + 1, 0)

		move_to(0, 0)

		if grown_pumpkins == PUMPKIN_SIDELENGTH**2:
			harvest()

	return True


def guarantee_pumpkin_with_fertilizer(n, reseted_soil_already=False):
	# type: (int, bool) -> bool

	def this_num_items():
		return num_items(Items.Pumpkin)

	if this_num_items() >= n:
		return False

	def this_reset():
		reset_ground(Grounds.Soil)
		reset_pos()

	if not reseted_soil_already:
		this_reset()
	par_guarantee_power(10000, True)

	while this_num_items() < n * 2:
		grown_pumpkins = 0

		guarantee_amt = 4 * calculate_crop_cost_for_entity_including_hardcoded_multipliers_for_full_field(Entities.Pumpkin)

		if any((guarantee_carrot(guarantee_amt, True), par_guarantee_power(5000, True))):
			# this_reset()
			pass  # same soil - no need to reset

		PUMPKIN_SIDELENGTH = WS
		YIELDED_SIDELENGTH = WS - PUMPKIN_SIDELENGTH
		YIELD_FN = yield_spot_carrot
		DO_WATERING = False

		all_sidelength = PUMPKIN_SIDELENGTH + YIELDED_SIDELENGTH

		if all_sidelength > WS:
			err_while1(__name__, "Invalid config: all_sidelength > WS")

		for _ in range(all_sidelength):
			for _ in range(all_sidelength):
				while DO_WATERING and get_water() < 0.95 and use_item(Items.Water):
					pass

				if get_pos_x() < PUMPKIN_SIDELENGTH and get_pos_y() < PUMPKIN_SIDELENGTH:  # optimal yield pumpkin
					if get_entity_type() != Entities.Pumpkin and can_harvest():
						harvest()

					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
						while not can_harvest() and num_items(Items.Fertilizer):
							if get_entity_type() == Entities.Dead_Pumpkin:
								plant(Entities.Pumpkin)
							use_item(Items.Fertilizer)

					if get_entity_type() == Entities.Pumpkin and can_harvest():
						grown_pumpkins += 1
					else:
						plant(Entities.Pumpkin)

					if grown_pumpkins == PUMPKIN_SIDELENGTH**2:
						harvest()
				else:
					YIELD_FN()

				move(North)

			move_to(get_pos_x() + 1, 0)

		move_to(0, 0)

	return True


def _f_col_guarantee_pumpkin(is_main):
	grown_pumpkins = 0
	while grown_pumpkins < WS:
		guarantee_amt = 4 * calculate_crop_cost_for_entity_including_hardcoded_multipliers_for_full_field(Entities.Pumpkin)

		col_guarantee_carrot(guarantee_amt, True)

		grown_pumpkins = 0
		for _ in range(WS):
			if get_entity_type() != Entities.Pumpkin and can_harvest():
				harvest()

			if get_entity_type() == Entities.Dead_Pumpkin:
				plant(Entities.Pumpkin)
				while not can_harvest() and num_items(Items.Fertilizer):
					if get_entity_type() == Entities.Dead_Pumpkin:
						plant(Entities.Pumpkin)
					use_item(Items.Fertilizer)

			if get_entity_type() == Entities.Pumpkin and can_harvest():
				grown_pumpkins += 1
			else:
				plant(Entities.Pumpkin)

			move(North)


def par_guarantee_pumpkin(n, reseted_ground_already=False):
	def this_num_items():
		return num_items(Items.Pumpkin)

	if this_num_items() >= n:
		return False

	def this_reset():
		par_reset_ground(Grounds.Soil)
		reset_pos()

	if not reseted_ground_already:
		this_reset()

	while this_num_items() < n * 2:
		await_drones(_f_col_guarantee_pumpkin, East)
		harvest()
