from m04prelude import *


def yield_spot_hay():
	if get_ground_type() != Grounds.Grassland:
		till()
	if get_entity_type() != Entities.Grass:
		plant(Entities.Grass)
	if can_harvest():
		harvest()


def yield_spot_bush():
	# if get_ground_type() != Grounds.Grassland:
	# 	till()
	# "can grow on grassland or soil"
	if can_harvest():
		harvest()
	if get_entity_type() != Entities.Bush:
		plant(Entities.Bush)


yield_spot = yield_spot_hay
