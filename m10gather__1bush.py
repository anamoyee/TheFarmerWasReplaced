while 1:
	plant(Entities.Bush)
	move(North)
	if can_harvest():
		harvest()
