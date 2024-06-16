from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> bytes:
    tb: bytes = token_bytes(length)
    return int.from_bytes(tb, 'big')
