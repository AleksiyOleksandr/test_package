from .Fields.datetime import DateTime
from .Record import Record


class InfoRecord(Record):
    def __init__(self):
        super().__init__()

        self._type = "infrec"
        self.period = DateTime()
        self.resources = []

