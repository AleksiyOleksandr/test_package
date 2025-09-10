from .reference import Reference
from .Fields import String


class Object(Reference):
    def __init__(self):
        super().__init__()
        self._hash = String()
        self._hash.len = 32

    @property
    def hash(self):
        return self._hash

