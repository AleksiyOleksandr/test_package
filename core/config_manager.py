import json
import os

data = {
  "db": {
    "type": "",
    "name": "",
    "user": "",
    "pwd": "",
    "host": ""
  }
}

# Абсолютний шлях до кореня
root_dir = os.path.dirname(os.path.abspath(__file__))

# Шлях до файлу в корені
file_path = os.path.join(root_dir, "data.json")

class ConfigManager():
    _instance = None
    _config = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __createFile(self):
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file)

    def load(self):
        if self._config is None:
            if not os.path.isfile(file_path):
                print('Конфігураційний файл не створено!')
                print('Створюю файл config.json в корені проєкту)')
                print('Файл створено:) Заповніть будь-ласка файл!')
            with open(file_path, 'r', encoding='utf-8') as file:
                self._config = json.load(file)
        return self._config

    @property
    def config(self):
        return self._config