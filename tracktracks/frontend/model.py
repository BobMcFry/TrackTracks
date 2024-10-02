from enum import IntEnum


class TrackType(IntEnum):
    # ------
    STRAIGHT = 1
    # ----
    #     \
    #      |
    CURVE = 2
    #      /
    # ----+-
    SWITCH_LEFT = 3
    # ----+-
    #      \
    SWITCH_RIGHT = 4
    #     |
    # ----+-
    #     |
    CROSSING_4_WAY = 5


class SignalType(IntEnum):
    RAIL = 1
    CHAIN = 2


class TileType(IntEnum):
    TRACK = 1
    SIGNAL = 2


MAPPING_TILE_TYPE_ENUM = {TileType.TRACK: TrackType, TileType.SIGNAL: SignalType}
