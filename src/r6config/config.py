import os
import re

from r6config.player import PlayerConfig

R6_PATH = os.path.expanduser("~/documents/My Games/Rainbow Six - Siege")

def is_valid_name(name: str) -> bool:
        """
        Проверяет, соответствует ли строка регулярному выражению r"^\w*[-_]\w*[-_]\w*[-_]\w*[-_]\w*$"

        Args:
            name (str): Строка для проверки.

        Returns:
            bool: True, если соответствует, иначе False.
        """
        pattern = r"^\w*[-_]\w*[-_]\w*[-_]\w*[-_]\w*$"
        return bool(re.fullmatch(pattern, name))

def get_folders(path: str) -> list:
        """
        Возвращает список папок в указанной директории.

        Args:
            path (str): Путь к директории.

        Returns:
            list: Список папок.
        """

        if os.path.exists(path):
            return [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]

        return []

def get_configs():
        """
        Возвращает список игроков в указанной директории.

        Returns:
            list: Список игроков.
        """
        players = []
        folders = get_folders(R6_PATH)

        if not folders:
            return players


        for folder in folders:
            if is_valid_name(folder):
                players.append(folder)

        return players

def get_player_config(player_id: str) -> list:
    """
    Возвращает список конфигов в указанной директории.

    Args:
        player_id (str): Player ID.

    Returns:
        list: Список конфигов.
    """

    player_config = PlayerConfig(f"{R6_PATH}/{player_id}/GameSettings.ini")

    return player_config
