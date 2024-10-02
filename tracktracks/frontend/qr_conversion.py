from enum import IntEnum
from typing import Union

from tracktracks.frontend.model import (
    TileType,
    SignalType,
    TrackType,
    MAPPING_TILE_TYPE_ENUM,
)


def encode_qr_id(tile_type: TileType, enum_type: IntEnum) -> str:
    return f"{tile_type.value}-{enum_type.value}"


def decode_qr_id(qr_id: str) -> tuple[TileType, Union[SignalType, TrackType]]:
    tile_type_int, enum_type_int = qr_id.split("-")
    tile_type = TileType(tile_type_int)
    enum_type = MAPPING_TILE_TYPE_ENUM[tile_type]
    return tile_type, enum_type(enum_type_int)
