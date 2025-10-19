from m04prelude import *
from m10gather__0hay import *
from m10gather__2carrot import *
from m10gather__3tree import *
from m10gather__4pumpkins import *
from m10gather__5sunflowe import *
from m10gather__6maze import *
from m10gather__7cacti import *

reset()


def infstrat():
	while 1:
		num = num_items(Items.Pumpkin)
		# guarantee_pumpkin(num * 1.2 + 1000)
		par_guarantee_carrot(num)
		par_guarantee_wood(num)
		par_guarantee_hay(num)


# guarantee_treasure(INF)
# guarantee_power(10000, True)

par_guarantee_power(100000)

# par_guarantee_cucktoose(16000000)
par_guarantee_carrot(66000000)
# par_guarantee_pumpkin(26000000)
# par_guarantee_wood(INF)

guarantee_treasure(INF)
# guarantee_wood(INF)

# guarantee_pumpkin_with_fertilizer(INF)

# guarantee_cucktoose(INF)
infstrat()
