from .Fields.boolean import Boolean
from .Fields.datetime import DateTime
from .Fields.string import String
from .entity import Entity
from .counter import Counter

class Document(Entity):
    def __init__(self):
        super().__init__()
        self._type = "doc"
        self.number = String() #TODO: додати в конструктор довжину. Або забрати у дарті
        self.number.len = 11
        self.datedoc = DateTime()
        self.deleted = Boolean()
        self.deleted.value = False
        self.recorded = Boolean()
        self.recorded.value = False

    def refreshCounter(self, counter: Counter):
        counter.entityName.value = self.objectName.value
        counter.lastNumber.value = self.number.value
        counter.save()

    def beforeSave(self):
        if self.number.value == '':
            counter = Counter.getCounterData(self.objectName)
            self.number.value = str(int(counter.lastNumber.value) + 1)
            self.refreshCounter(counter)