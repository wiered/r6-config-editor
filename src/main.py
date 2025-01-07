import asyncio
import os
import re
import time


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

def get_players(path: str) -> list:
    """
    Возвращает список игроков в указанной директории.

    Args:
        path (str): Путь к директории.

    Returns:
        list: Список игроков.
    """
    players = []
    folders = get_folders(path)

    if not folders:
        return players


    for folder in folders:
        if is_valid_name(folder):
            players.append(folder)

    return players

def choose_player(players: list) -> str:
    """
    Возвращает выбранного игрока.

    Args:
        players (list): Список игроков.

    Returns:
        str: Выбранный игрок.
    """
    print("Выберите игрока:")
    for i, player in enumerate(players):
        print(f"{i + 1}. {player}")

    while True:
        choice = input("Введите номер игрока: ")
        if choice.isdigit() and 1 <= int(choice) <= len(players):
            return players[int(choice) - 1]
        if choice == "q":
            exit()
        print("Неверный ввод. Пожалуйста, попробуйте ещё раз.")

def get_config(player: str) -> list:
    """
    Возвращает список конфигов в указанной директории.

    Args:
        path (str): Путь к директории.

    Returns:
        list: Список конфигов.
    """

    player_config = PlayerConfig(f"{R6_PATH}/{player}/GameSettings.ini")

    return player_config

def read_section(player_config: PlayerConfig, section: str, settings: list):
    print(  )
    print(f"[{section}]")
    for setting in settings:
        print(f"{setting[0]} = {player_config.get_setting(section, setting[0])} ({setting[1]})")

def read_config(player_config: PlayerConfig):
    """
    Показывает конфиг

    Args:
        player_config (PlayerConfig): Конфиг игрока.
    """

    read_section(player_config, "DISPLAY", [("Brightness", "70 is ok")])
    read_section(
        player_config, "DISPLAY_SETTINGS",
        [
            ("RefreshRate", "Refresh Rate"),
            ("AspectRatio", "Aspect Ratio"),
            ("DefaultFOV", "Default FOV"),
        ]
        )
    read_section(player_config, "CUSTOM_QUALITY", [("Shadow", "1 is ok")])
    read_section(
        player_config, "INPUT",
        [
            ("RawInputMouseKeyboard", "1 is raw"),
            ("MouseSensitivity", "Mouse sensitivity"),
            ("MouseYawSensitivity", "Mouse yaw sensitivity"),
            ("MousePitchSensitivity", "Mouse pitch sensitivity"),
            ("MouseSensitivityMultiplierUnit", "0.02 default, 0.00223 kix"),
            ("XFactorAiming", "0.02 default"),
            ("AimDownSightsMouse", "ADS Mouse"),
            ("ADSMouseSensitivityGlobal", ""),
            ("ADSMouseSensitivity1x", ""),
            ("ADSMouseSensitivity1xHalf", ""),
            ("ADSMouseSensitivity2x", ""),
            ("ADSMouseSensitivity2xHalf", ""),
            ("ADSMouseMultiplierUnit", ""),
        ]
    )



def main():
    players = get_players(R6_PATH)
    player = choose_player(players)
    print(f"Выбран игрок: {player}")
    config = get_config(player)
    print("\n\nCONFIG:")
    read_config(config)

if __name__ == "__main__":
    main()
