from enum import IntEnum
from pathlib import Path

from qrcode import QRCode

from tracktracks.frontend.model import TileType, MAPPING_TILE_TYPE_ENUM
from tracktracks.frontend.qr_conversion import encode_qr_id


def _generate_qr_code(text: str, output_path: Path) -> None:
    qr = QRCode(version=1)
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image()
    img.save(output_path)


def _qr_code_filename(tile_type: TileType, enum_type: IntEnum, suffix: str) -> str:
    return f"{tile_type.name}-{enum_type.name}.{suffix}"


def generate_qr_codes() -> None:
    suffix = "png"
    output_directory = Path("./out")
    for tile_type in TileType:
        for e in MAPPING_TILE_TYPE_ENUM[tile_type]:
            track_id = encode_qr_id(tile_type, e)
            filename = _qr_code_filename(tile_type, e, suffix)
            _generate_qr_code(track_id, output_directory / filename)
