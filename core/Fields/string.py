from app.core.data_field import DataField

class String(DataField):

    def __init__(self):
        super().__init__()
        self._len = 10
        self._value = ""

    @DataField.value.setter
    def value(self,val):
        if not isinstance(val, str):
            raise ValueError("The 'value' property must be a string value.")
        self._value = val[:self._len] #Встановлюємо значення в межах заданої довжини

    @property
    def len(self):
         return self._len

    @len.setter
    def len(self,val):
        if not isinstance(val, int):
            raise ValueError("The 'value' property must be a integer value.")
        self._len = val


