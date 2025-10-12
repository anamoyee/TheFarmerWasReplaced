from m04prelude import *
from m10gather__0hay import guarantee_hay
from m10gather__2carrot import guarantee_carrot
from m10gather__3tree import guarantee_wood

reset()

while 1:
	bump = 2500
	guarantee_wood(num_items(Items.Wood) + bump)
	guarantee_hay(num_items(Items.Hay) + 3 * bump)
	guarantee_carrot(num_items(Items.Carrot) + bump)
