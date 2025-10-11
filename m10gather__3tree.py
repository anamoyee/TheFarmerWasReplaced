def some_wood(n):
	# type: (int) -> None
	for _ in range(n):
		for _ in range(get_world_size()):
			for _ in range(get_world_size()):
				if (get_pos_x() + get_pos_y()) % 2 == 0:
					if can_harvest():
						harvest()
					plant(Entities.Tree)
				move(North)
			move(East)
