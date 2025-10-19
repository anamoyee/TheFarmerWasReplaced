import m04prelude
from m01const import *
from m01const import _DEBUG_SKIP_EXTENSIVE_RESET


def reset_if_hedge():
	if get_entity_type() == Entities.Hedge:
		harvest()


def reset_pos():
	reset_if_hedge()

	if get_entity_type() == Entities.Hedge:
		return  # Do not reset pos if within a hedge

	m04prelude.move_to(0, 0)


def reset_ground(ground_type, plant_=None):
	# type: (Ground, Entity | None) -> None

	if _DEBUG_SKIP_EXTENSIVE_RESET:
		return

	for _ in range(WS):
		for _ in range(WS):
			if get_ground_type() != ground_type:
				till()
			if plant_ != NONE and get_entity_type() != plant_:
				harvest()
				plant(plant_)
			move(North)
		move(East)


def col_reset_ground(ground_type, plant_=None):
	# type: (Ground, Entity | None) -> None

	if _DEBUG_SKIP_EXTENSIVE_RESET:
		return

	for _ in range(WS):
		if get_ground_type() != ground_type:
			till()
		if plant_ != NONE and get_entity_type() != plant_:
			harvest()
			plant(plant_)
		move(North)


def par_reset_ground(ground_type, plant_=None):
	# type: (Ground, Entity | None) -> None

	if _DEBUG_SKIP_EXTENSIVE_RESET:
		return

	def f(is_main):
		for _ in range(WS):
			if get_ground_type() != ground_type:
				till()
			if plant_ != NONE and get_entity_type() != plant_:
				harvest()
				plant(plant_)
			move(North)

	m04prelude.await_drones(f, East)


# ground: Grounds | None
def reset():
	if _DEBUG_SKIP_EXTENSIVE_RESET:
		reset_pos()
		return

	reset_if_hedge()

	# reset_ground(Grounds.Soil)

	reset_pos()
