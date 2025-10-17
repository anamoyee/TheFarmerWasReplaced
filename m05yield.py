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


def yield_spot_carrot():
	if get_ground_type() != Grounds.Soil:
		till()
	if can_harvest():
		harvest()
	if get_entity_type() != Entities.Carrot:
		plant(Entities.Carrot)
	if can_harvest():
		harvest()


yield_spot = yield_spot_hay
