from enum import IntEnum

from tracktracks.frontend.model import (
    MAPPING_TILE_TYPE_ENUM,
    SignalType,
    TileType,
    TrackType,
)


def encode_qr_id(tile_type: TileType, enum_type: IntEnum) -> str:
    return f"{tile_type.value}-{enum_type.value}"


def decode_qr_id(qr_id: str) -> tuple[TileType, SignalType | TrackType]:
    tile_type_int, enum_type_int = qr_id.split("-")
    tile_type = TileType(int(tile_type_int))
    enum_type = MAPPING_TILE_TYPE_ENUM[tile_type]
    return tile_type, enum_type(int(enum_type_int))
