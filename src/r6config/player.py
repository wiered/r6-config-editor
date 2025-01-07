import configparser

class PlayerConfig:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.config = configparser.ConfigParser()
        self.config.read(file_path)

    def get_setting(self, section: str, key: str, default=None):
        """Получает значение настройки, возвращая default, если ключ не найден."""
        return self.config.get(section, key, fallback=default)

    def get_float(self, section: str, key: str, default=0.0):
        """Получает значение настройки как float."""
        return self.config.getfloat(section, key, fallback=default)

    def get_int(self, section: str, key: str, default=0):
        """Получает значение настройки как int."""
        return self.config.getint(section, key, fallback=default)

    def get_bool(self, section: str, key: str, default=False):
        """Получает значение настройки как bool."""
        return self.config.getboolean(section, key, fallback=default)

    def set_setting(self, section: str, key: str, value):
        """Устанавливает значение настройки."""
        if not self.config.has_section(section):
            self.config.add_section(section)
        self.config.set(section, key, str(value))

    def save(self):
        """Сохраняет изменения обратно в файл."""
        with open(self.file_path, "w") as file:
            self.config.write(file)
