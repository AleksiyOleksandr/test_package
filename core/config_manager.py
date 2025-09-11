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

# Шлях до файлу в корені проєкту користувача
file_path = os.path.join(os.getcwd(), "config.json")

class NotConfigInFile(Exception):
    pass

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
                self.__createFile()
                print('Файл створено:)')
                raise NotConfigInFile(f"Файл {file_path} створено автоматично. "
                "Будь ласка, заповніть його і запустіть програму ще раз.")
            with open(file_path, 'r', encoding='utf-8') as file:
                self._config = json.load(file)
        return self._config

    @property
    def config(self):
        return self._config