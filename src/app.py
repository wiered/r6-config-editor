import os

import customtkinter
import tkinter

from r6config import get_configs, get_player_config, PlayerConfig

R6_PATH = os.path.expanduser("~/documents/My Games/Rainbow Six - Siege")

class ConfigDropdownFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self._master = master

        # Dropdown with config list
        self.config_list_label = customtkinter.CTkLabel(self, text="Config List")
        self.config_list_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.config_optionmenu = customtkinter.CTkOptionMenu(self, values=[], command=self.optionmenu_callback)
        self.config_optionmenu.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="w")

    def optionmenu_callback(self, player_id):
        self._master.entry_frame.load_config(player_id)

    def load_configs(self):
        players = get_configs()

        self.config_optionmenu.configure(values=players)
        self.config_optionmenu.set(players[0])
        self._master.entry_frame.load_config(players[0])


class EntyrFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.player_id = None

        self.brightness_label = customtkinter.CTkLabel(self, text="Brightness(0-100)")
        self.brightness_label.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="w")
        self.brightness_edit = customtkinter.CTkEntry(self, placeholder_text="70 is ok")
        self.brightness_edit.grid(row=0, column=1, padx=10, pady=(10, 0), sticky="e")

        self.refresh_rate_label = customtkinter.CTkLabel(self, text="Refresh Rate(Hz.)")
        self.refresh_rate_label.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="w")
        self.refresh_rate_edit = customtkinter.CTkEntry(self, placeholder_text="RefreshRate")
        self.refresh_rate_edit.grid(row=1, column=1, padx=10, pady=(10, 0), sticky="e")

        self.default_fov_label = customtkinter.CTkLabel(self, text="FOV(60-90)")
        self.default_fov_label.grid(row=3, column=0, padx=10, pady=(10, 0), sticky="w")
        self.default_fov_edit = customtkinter.CTkEntry(self, placeholder_text="DefaultFOV")
        self.default_fov_edit.grid(row=3, column=1, padx=10, pady=(10, 0), sticky="e")

        self.raw_input_mouse_keyboard_label = customtkinter.CTkLabel(self, text="RawInputMouseKeyboard(0, 1)")
        self.raw_input_mouse_keyboard_label.grid(row=4, column=0, padx=10, pady=(10, 0), sticky="w")
        self.raw_input_mouse_keyboard_edit = customtkinter.CTkEntry(self, placeholder_text="1 is raw")
        self.raw_input_mouse_keyboard_edit.grid(row=4, column=1, padx=10, pady=(10, 0), sticky="e")

        self.mouse_sensitivity_label = customtkinter.CTkLabel(self, text="MouseSensitivity(1-100)")
        self.mouse_sensitivity_label.grid(row=5, column=0, padx=10, pady=(10, 0), sticky="w")
        self.mouse_sensitivity_edit = customtkinter.CTkEntry(self, placeholder_text="Mouse sensitivity")
        self.mouse_sensitivity_edit.grid(row=5, column=1, padx=10, pady=(10, 0), sticky="e")

        self.mouse_yaw_sensitivity_label = customtkinter.CTkLabel(self, text="MouseYawSensitivity(1-100)")
        self.mouse_yaw_sensitivity_label.grid(row=6, column=0, padx=10, pady=(10, 0), sticky="w")
        self.mouse_yaw_sensitivity_edit = customtkinter.CTkEntry(self, placeholder_text="Mouse yaw sensitivity")
        self.mouse_yaw_sensitivity_edit.grid(row=6, column=1, padx=10, pady=(10, 0), sticky="e")

        self.mouse_pitch_sensitivity_label = customtkinter.CTkLabel(self, text="MousePitchSensitivity(1-100)")
        self.mouse_pitch_sensitivity_label.grid(row=7, column=0, padx=10, pady=(10, 0), sticky="w")
        self.mouse_pitch_sensitivity_edit = customtkinter.CTkEntry(self, placeholder_text="Mouse pitch sensitivity")
        self.mouse_pitch_sensitivity_edit.grid(row=7, column=1, padx=10, pady=(10, 0), sticky="e")

        self.mouse_sensitivity_multiplier_unit_label = customtkinter.CTkLabel(self, text="MouseSensitivityMultiplierUnit(0-1)")
        self.mouse_sensitivity_multiplier_unit_label.grid(row=8, column=0, padx=10, pady=(10, 0), sticky="w")
        self.mouse_sensitivity_multiplier_unit_edit = customtkinter.CTkEntry(self, placeholder_text="0.02 default, 0.00223 kix")
        self.mouse_sensitivity_multiplier_unit_edit.grid(row=8, column=1, padx=10, pady=(10, 0), sticky="e")

        self.x_factor_aiming_label = customtkinter.CTkLabel(self, text="XFactorAiming(0-1)")
        self.x_factor_aiming_label.grid(row=9, column=0, padx=10, pady=(10, 0), sticky="w")
        self.x_factor_aiming_edit = customtkinter.CTkEntry(self, placeholder_text="0.02 default")
        self.x_factor_aiming_edit.grid(row=9, column=1, padx=10, pady=(10, 0), sticky="e")

        self.aim_down_sights_mouse_label = customtkinter.CTkLabel(self, text="AimDownSightsMouse(1-100)")
        self.aim_down_sights_mouse_label.grid(row=10, column=0, padx=10, pady=(10, 0), sticky="w")
        self.aim_down_sights_mouse_edit = customtkinter.CTkEntry(self, placeholder_text="ADS Mouse")
        self.aim_down_sights_mouse_edit.grid(row=10, column=1, padx=10, pady=(10, 0), sticky="e")

        self.adsmouse_sensitivity_global_label = customtkinter.CTkLabel(self, text="ADSMouseSensitivityGlobal(1-100)")
        self.adsmouse_sensitivity_global_label.grid(row=11, column=0, padx=10, pady=(10, 0), sticky="w")
        self.adsmouse_sensitivity_global_edit = customtkinter.CTkEntry(self, placeholder_text="")
        self.adsmouse_sensitivity_global_edit.grid(row=11, column=1, padx=10, pady=(10, 0), sticky="e")

        self.adsmouse_sensitivity_1x_label = customtkinter.CTkLabel(self, text="ADSMouseSensitivity1x(1-100)")
        self.adsmouse_sensitivity_1x_label.grid(row=12, column=0, padx=10, pady=(10, 0), sticky="w")
        self.adsmouse_sensitivity_1x_edit = customtkinter.CTkEntry(self, placeholder_text="")
        self.adsmouse_sensitivity_1x_edit.grid(row=12, column=1, padx=10, pady=(10, 0), sticky="e")

        self.adsmouse_sensitivity_1x_half_label = customtkinter.CTkLabel(self, text="ADSMouseSensitivity1xHalf(1-100)")
        self.adsmouse_sensitivity_1x_half_label.grid(row=13, column=0, padx=10, pady=(10, 0), sticky="w")
        self.adsmouse_sensitivity_1x_half_edit = customtkinter.CTkEntry(self, placeholder_text="")
        self.adsmouse_sensitivity_1x_half_edit.grid(row=13, column=1, padx=10, pady=(10, 0), sticky="e")

        self.adsmouse_sensitivity_2x_label = customtkinter.CTkLabel(self, text="ADSMouseSensitivity2x(1-100)")
        self.adsmouse_sensitivity_2x_label.grid(row=14, column=0, padx=10, pady=(10, 0), sticky="w")
        self.adsmouse_sensitivity_2x_edit = customtkinter.CTkEntry(self, placeholder_text="")
        self.adsmouse_sensitivity_2x_edit.grid(row=14, column=1, padx=10, pady=(10, 0), sticky="e")

        self.adsmouse_sensitivity_2x_half_label = customtkinter.CTkLabel(self, text="ADSMouseSensitivity2xHalf(1-100)")
        self.adsmouse_sensitivity_2x_half_label.grid(row=15, column=0, padx=10, pady=(10, 0), sticky="w")
        self.adsmouse_sensitivity_2x_half_edit = customtkinter.CTkEntry(self, placeholder_text="")
        self.adsmouse_sensitivity_2x_half_edit.grid(row=15, column=1, padx=10, pady=(10, 0), sticky="e")

        self.adsmouse_multiplier_unit_label = customtkinter.CTkLabel(self, text="ADSMouseMultiplierUnit(0-1)")
        self.adsmouse_multiplier_unit_label.grid(row=16, column=0, padx=10, pady=(10, 0), sticky="w")
        self.adsmouse_multiplier_unit_edit = customtkinter.CTkEntry(self, placeholder_text="")
        self.adsmouse_multiplier_unit_edit.grid(row=16, column=1, padx=10, pady=(10, 10), sticky="e")

    def load_config(self, player_id):
        self.player_id = player_id
        player_config = get_player_config(player_id)

        # DISPLAY
        self.brightness_edit.delete(0, "end")
        self.brightness_edit.insert(
            0, player_config.get_setting("DISPLAY", "Brightness")
            )

        # DISPLAY_SETTINGS

        self.refresh_rate_edit.delete(0, "end")
        self.refresh_rate_edit.insert(
            0, player_config.get_setting("DISPLAY_SETTINGS", "RefreshRate")
            )

        self.default_fov_edit.delete(0, "end")
        self.default_fov_edit.insert(
            0, player_config.get_setting("DISPLAY_SETTINGS", "DefaultFOV")
            )

        #INPUT

        self.raw_input_mouse_keyboard_edit.delete(0, "end")
        self.raw_input_mouse_keyboard_edit.insert(
            0, player_config.get_int("INPUT", "RawInputMouseKeyboard")
        )


        self.mouse_sensitivity_edit.delete(0, "end")
        self.mouse_sensitivity_edit.insert(
            0, player_config.get_setting("INPUT", "MouseSensitivity")
            )

        self.mouse_yaw_sensitivity_edit.delete(0, "end")
        self.mouse_yaw_sensitivity_edit.insert(
            0, player_config.get_setting("INPUT", "MouseYawSensitivity")
        )

        self.mouse_pitch_sensitivity_edit.delete(0, "end")
        self.mouse_pitch_sensitivity_edit.insert(
            0, player_config.get_setting("INPUT", "MousePitchSensitivity")
        )

        self.mouse_sensitivity_multiplier_unit_edit.delete(0, "end")
        self.mouse_sensitivity_multiplier_unit_edit.insert(
            0, player_config.get_setting("INPUT", "MouseSensitivityMultiplierUnit")
            )

        self.x_factor_aiming_edit.delete(0, "end")
        self.x_factor_aiming_edit.insert(
            0, player_config.get_setting("INPUT", "XFactorAiming")
            )

        self.aim_down_sights_mouse_edit.delete(0, "end")
        self.aim_down_sights_mouse_edit.insert(
            0, player_config.get_setting("INPUT", "AimDownSightsMouse")
        )

        self.adsmouse_sensitivity_global_edit.delete(0, "end")
        self.adsmouse_sensitivity_global_edit.insert(
            0, player_config.get_setting("INPUT", "ADSMouseSensitivityGlobal")
        )

        self.adsmouse_sensitivity_1x_edit.delete(0, "end")
        self.adsmouse_sensitivity_1x_edit.insert(
            0, player_config.get_setting("INPUT", "ADSMouseSensitivity1x")
        )

        self.adsmouse_sensitivity_1x_half_edit.delete(0, "end")
        self.adsmouse_sensitivity_1x_half_edit.insert(
            0, player_config.get_setting("INPUT", "ADSMouseSensitivity1xHalf")
        )

        self.adsmouse_sensitivity_2x_edit.delete(0, "end")
        self.adsmouse_sensitivity_2x_edit.insert(
            0, player_config.get_setting("INPUT", "ADSMouseSensitivity2x")
        )

        self.adsmouse_sensitivity_2x_half_edit.delete(0, "end")
        self.adsmouse_sensitivity_2x_half_edit.insert(
            0, player_config.get_setting("INPUT", "ADSMouseSensitivity2xHalf")
        )

        self.adsmouse_multiplier_unit_edit.delete(0, "end")
        self.adsmouse_multiplier_unit_edit.insert(
            0, player_config.get_setting("INPUT", "ADSMouseMultiplierUnit")
        )

    def get_settings(self) -> list:
        settings = []

        settings.append(("Brightness", self.brightness_edit.get()))
        settings.append(("RefreshRate", self.refresh_rate_edit.get()))
        settings.append(("DefaultFOV", self.default_fov_edit.get()))
        settings.append(("RawInputMouseKeyboard", self.raw_input_mouse_keyboard_edit.get()))
        settings.append(("MouseSensitivity", self.mouse_sensitivity_edit.get()))
        settings.append(("MouseYawSensitivity", self.mouse_yaw_sensitivity_edit.get()))
        settings.append(("MousePitchSensitivity", self.mouse_pitch_sensitivity_edit.get()))
        settings.append(("MouseSensitivityMultiplierUnit", self.mouse_sensitivity_multiplier_unit_edit.get()))
        settings.append(("XFactorAiming", self.x_factor_aiming_edit.get()))
        settings.append(("AimDownSightsMouse", self.aim_down_sights_mouse_edit.get()))
        settings.append(("ADSMouseSensitivityGlobal", self.adsmouse_sensitivity_global_edit.get()))
        settings.append(("ADSMouseSensitivity1x", self.adsmouse_sensitivity_1x_edit.get()))
        settings.append(("ADSMouseSensitivity1xHalf", self.adsmouse_sensitivity_1x_half_edit.get()))
        settings.append(("ADSMouseSensitivity2x", self.adsmouse_sensitivity_2x_edit.get()))
        settings.append(("ADSMouseSensitivity2xHalf", self.adsmouse_sensitivity_2x_half_edit.get()))
        settings.append(("ADSMouseMultiplierUnit", self.adsmouse_multiplier_unit_edit.get()))

        return settings

    def get_player_id(self) -> str:
        return self.player_id


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("R6S Config Editor")
        self.geometry("400x730")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.config_dropdown_frame = ConfigDropdownFrame(self)
        self.config_dropdown_frame.grid(row=0, column=0, padx=10, pady=(10, 0), sticky="nswe")

        self.entry_frame = EntyrFrame(self)
        self.entry_frame.grid(row=1, column=0, padx=10, pady=(10, 0), sticky="nswe")

        self.button = customtkinter.CTkButton(self, text="Save", command=self.button_callback)
        self.button.grid(row=2, column=0, columnspan=1, padx=10, pady=10, sticky="ew")

        self.config_dropdown_frame.load_configs()

    def button_callback(self):
        settings = self.entry_frame.get_settings()
        player_id = self.entry_frame.get_player_id()

        player_config = PlayerConfig(f"{R6_PATH}/{player_id}/GameSettings.ini")

        player_config.set_setting("DISPLAY", settings[0][0], settings[0][1])
        player_config.set_setting("DISPLAY_SETTINGS", settings[1][0], settings[1][1])
        player_config.set_setting("DISPLAY_SETTINGS", settings[2][0], settings[2][1])
        player_config.set_setting("INPUT", settings[3][0], settings[3][1])
        player_config.set_setting("INPUT", settings[4][0], settings[4][1])
        player_config.set_setting("INPUT", settings[5][0], settings[5][1])
        player_config.set_setting("INPUT", settings[6][0], settings[6][1])
        player_config.set_setting("INPUT", settings[7][0], settings[7][1])
        player_config.set_setting("INPUT", settings[8][0], settings[8][1])
        player_config.set_setting("INPUT", settings[9][0], settings[9][1])
        player_config.set_setting("INPUT", settings[10][0], settings[10][1])
        player_config.set_setting("INPUT", settings[11][0], settings[11][1])
        player_config.set_setting("INPUT", settings[12][0], settings[12][1])
        player_config.set_setting("INPUT", settings[13][0], settings[13][1])
        player_config.set_setting("INPUT", settings[14][0], settings[14][1])
        player_config.set_setting("INPUT", settings[15][0], settings[15][1])

        player_config.save()

app = App()
app.mainloop()
