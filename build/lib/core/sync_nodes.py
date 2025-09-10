from .entity import Entity
from .Fields.string import String
from .Fields.boolean import Boolean


class SyncNode(Entity):
    def __init__(self):
        super().__init__()
        self._type = "repl"
        self.name = String()
        self.name.len = 100
        self.isActive = Boolean()
        self.address = String()
        self.address.len = 255
        self.port = String()
        self.port.len = 10
        self.entities = []  # список типів сутностей для реплікації
        
    def shouldSync(self, entity_type):
        #print("self.entities")
        #pprint.pprint(self.entities)
        """Перевіряє чи потрібно синхронізувати даний тип сутності"""
        return self.isActive.value and entity_type in self.entities