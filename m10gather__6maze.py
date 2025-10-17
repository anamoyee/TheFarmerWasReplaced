from m04prelude import *
from m10gather__4pumpkins import guarantee_pumpkin_with_fertilizer


def spawn_maze(size=WS, stack=1):
	# type: (int, int) -> None

	substance_required = size * 2 ** (num_unlocked(Unlocks.Mazes) - 1)

	if get_entity_type() != Entities.Treasure:
		harvest()

		while num_items(Items.Weird_Substance) < (substance_required * stack):
			guarantee_pumpkin_with_fertilizer(num_items(Items.Pumpkin) + 69)

		plant(Entities.Bush)

	use_item(Items.Weird_Substance, substance_required)


def guarantee_treasure_cheaty(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Gold)

	if this_num_items() >= n:
		return False

	while this_num_items() < n * 2:
		spawn_maze(1)  # :troll:
		harvest()


def explore_maze(moves=[]):
	# type: (list[Direction]) -> bool

	if get_entity_type() == Entities.Treasure:
		return True

	for dir in DIRECTIONS:
		if moves and moves[-1] == dir180(dir):
			continue

		moved = move(dir)

		if moved:
			if explore_maze(merge_list(moves, [dir])):
				return True

			move(dir180(dir))

	return False


def guarantee_treasure(n):
	# type: (int) -> bool

	def this_num_items():
		return num_items(Items.Gold)

	if this_num_items() >= n:
		return False

	while this_num_items() < n * 2:
		if get_entity_type() != Entities.Hedge:  # if == Treasure, spawn_maze harvests
			# move_to(WS // 2, WS // 2) # dunno if this makes it any better but without it, it looks nicer!
			spawn_maze()
		if explore_maze([]):
			harvest()
		else:
			err_while1(__name__, "explore_maze() couldn't find the treasure...????? Where the fuck is it???")
