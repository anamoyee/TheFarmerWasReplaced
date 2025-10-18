from m01const import *
from m02reset import *

if 1 - 1:
	from typing import TypeVar

	T = TypeVar("T")


def min(x, y):
	if x < y:
		return x
	else:
		return y


def max(x, y):
	if x > y:
		return x
	else:
		return y


def copy_list(lst):
	# type: (list[T]) -> list[T]

	new_lst = []

	for item in lst:
		new_lst.append(item)

	return new_lst


def merge_list(lst1, lst2):
	new_lst = []

	for item in lst1:
		new_lst.append(item)

	for item in lst2:
		new_lst.append(item)

	return new_lst


def dir180(dir):
	# type: (Direction) -> Direction

	return {
		North: South,
		East: West,
		West: East,
		South: North,
	}[dir]


def dir_vector(dir):
	# type: (Direction) -> tuple[int, int]

	return {
		North: (0, 1),
		East: (1, 0),
		West: (-1, 0),
		South: (0, -1),
	}[dir]


def add_vectors(pos1, pos2):
	# type: (tuple[int, int], tuple[int, int]) -> tuple[int, int]
	return (pos1[0] + pos2[0], pos1[1] + pos2[1])


def add_pos_dir(pos, dir):
	# type: (tuple[int, int], Direction) -> tuple[int, int]
	return add_vectors(pos, dir_vector(dir))


def get_pos():
	# type: () -> tuple[int, int]

	return (get_pos_x(), get_pos_y())


def _calculate_crop_cost_by_unlock(unlock):
	# type: (Unlock) -> int
	return 2 ** (num_unlocked(unlock) - 1)


def calculate_crop_cost_for_entity_including_hardcoded_multipliers(entity):
	# type: (Entity) -> int
	lookup = {
		Entities.Grass: (1, Unlocks.Grass),
		Entities.Bush: (1, Unlocks.Trees),
		Entities.Tree: (5, Unlocks.Trees),
		Entities.Carrot: (1, Unlocks.Carrots),
		Entities.Pumpkin: (1, Unlocks.Pumpkins),
	}  # type: dict[Entity, tuple[int, Unlock]]

	if entity not in lookup:
		err_while1(__name__, "calculate_...: Entity:", entity, "was not found in the lookup dict.")

	mult, unlock = lookup[entity]

	return mult * _calculate_crop_cost_by_unlock(unlock)


def calculate_crop_cost_for_entity_including_hardcoded_multipliers_for_full_field(unlock, WS_=WS):
	# type: (Unlock, int) -> int
	return (WS_**2) * calculate_crop_cost_for_entity_including_hardcoded_multipliers(unlock)


def move_to_x(x):
	# type: (int) -> bool
	current_x = get_pos_x()
	dx = (x - current_x) % WS
	if dx > WS // 2:
		for _ in range(WS - dx):
			if not move(West):
				return False
	else:
		for _ in range(dx):
			if not move(East):
				return False

	return True


def move_to_y(y):
	# type: (int) -> bool
	current_y = get_pos_y()
	dy = (y - current_y) % WS
	if dy > WS // 2:
		for _ in range(WS - dy):
			if not move(South):
				return False
	else:
		for _ in range(dy):
			if not move(North):
				return False

	return True


def move_to(x, y):
	# type: (int, int) -> bool
	if not move_to_x(x):
		return False
	if not move_to_y(y):  # noqa: SIM103
		return False

	return True


def move_to2(pos):
	# type: (tuple[int, int]) -> bool
	x, y = pos
	return move_to(x, y)


def err_while1(
	dunder_name,
	msg,
	move_to_middle=True,
	print_fn=print,
	sleep_fn=do_a_flip,
):
	# type: (str, str, bool, Callable[[str, str, str], None], Callable[[], None]) -> NoReturn

	if move_to_middle:
		move_to(WS // 2, WS // 2)

	while 1:
		print_fn(dunder_name, "->", msg)
		sleep_fn()
