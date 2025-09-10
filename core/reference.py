from app.core.Fields.boolean import Boolean
from app.core.entity import Entity
from app.core.counter import Counter

class Reference(Entity):
    def __init__(self):
        super().__init__()
        self.deleted = Boolean()
        self.deleted.value = False
        self._type = "ref"

    def refreshCounter(self, counter: Counter):
        counter.entityName.value = self.objectName.value
        counter.lastNumber.value = self.code.value
        counter.save()

    def beforeSave(self):
        if self.code.value == '':
            counter = Counter.getCounterData(self.objectName)
            self.code.value = str(int(counter.lastNumber.value) + 1)
            self.refreshCounter(counter)