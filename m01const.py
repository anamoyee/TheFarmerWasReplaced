INF = 999999999  # infinity is a lie
NONE = None  # Alt none, in order to easily suppress ruff's '!= None'

WS = get_world_size()


DIRECTIONS = [North, East, West, South]

_DEBUG_SKIP_EXTENSIVE_RESET = False
# Skip (potentially breaking shit) the lengthy reset functions, for testing only!
