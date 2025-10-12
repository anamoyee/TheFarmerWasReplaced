from m04prelude import *
from m10gather__0hay import *
from m10gather__2carrot import *
from m10gather__3tree import *
from m10gather__4pumpkins import *
from m10gather__5sunflowe import guarantee_sunflower

reset()


def infstrat():
	while 1:
		num = num_items(Items.Pumpkin)
		guarantee_pumpkin(num * 1.2 + 1000)
		guarantee_carrot(num)
		guarantee_wood(num)
		guarantee_hay2(num)


guarantee_sunflower(1000)
guarantee_wood(INF)
guarantee_hay2(INF)
infstrat()
