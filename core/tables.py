from .Fields.string import String
from .entity import Entity

class Tables(Entity):
    def __init__(self):
        super().__init__()
        self._type = 'tb'

        self.entityName: String = String()
        self.entityName.len = 50
        self.entityName.value = ''

    @classmethod
    def addTable(cls, entityName: String):
        table = cls()
        table.entityName.value = entityName.value
        return table