while 1:
	plant(Entities.Carrot)
	if get_ground_type() != Grounds.Soil:
		till()
	move(North)
	if can_harvest():
		harvest()
