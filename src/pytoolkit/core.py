from collections.abc import Iterable
from typing import TypeVar
T=TypeVar("T")

def coalesce(*values:T|None) -> T|None:
    for value in values:
        if value is not None: return value
    return None

def ensure_list(value:T|Iterable[T]) -> list[T]:
    if isinstance(value,(str,bytes)): return [value]  # type: ignore[list-item]
    try: return list(value)  # type: ignore[arg-type]
    except TypeError: return [value]  # type: ignore[list-item]
