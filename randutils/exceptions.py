from typing import Any


class EmptyListError(Exception):
    def __init__(self) -> None:
        super().__init__(
            f"Can't take a random element from an empty list"
        )


class NoObjectsError(Exception):
    def __init__(self, model: Any) -> None:
        super().__init__(
            f"Can't pick a random instance from model: '{model}' since no objects exist"
        )
