from m04prelude import *
from m10gather__0hay import *
from m10gather__2carrot import *
from m10gather__3tree import *
from m10gather__4pumpkins import *
from m10gather__5sunflowe import *
from m10gather__6maze import *
from m10gather__7cacti import guarantee_cucktoose

reset()


def infstrat():
	while 1:
		num = num_items(Items.Pumpkin)
		guarantee_pumpkin(num * 1.2 + 1000)
		guarantee_carrot(num)
		guarantee_wood(num)
		guarantee_hay(num)


# guarantee_treasure(INF)
# guarantee_treasure_cheaty(INF)
# guarantee_wood(INF)

# guarantee_pumpkin_with_fertilizer(INF)

guarantee_cucktoose(INF)
infstrat()
