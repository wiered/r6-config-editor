import os

import imgui
from imgui.integrations.pyglet import PygletRenderer
import pyglet
from pyglet.gl import glClearColor

from r6config import get_configs, get_player_config, PlayerConfig

VERSION = "2.0"
R6_PATH = os.path.expanduser("~/Documents/My Games/Rainbow Six - Siege")


class R6SConfigEditor:
    # --- Category definitions as class constants ---
    IMPORTANT_CATEGORIES = {
        "DISPLAY": ["brightness"],
        "DISPLAY_SETTINGS": ["refreshrate", "defaultfov"],
        "INPUT": [
            "rawinputmousekeyboard", "mousesensitivity", "mouseyawsensitivity",
            "mousepitchsensitivity", "mousesensitivitymultiplierunit",
            "xfactoraiming", "aimdownsightsmouse",
            "adsmousesensitivityglobal", "adsmousesensitivity1x",
            "adsmousesensitivity1xhalf", "adsmousesensitivity2x",
            "adsmousesensitivity2xhalf", "adsmousemultiplierunit",
        ],
    }

    ALL_CATEGORIES = {
        "DISPLAY": ["fpslimit", "nvreflex", "nvreflexindicator"],
        "DISPLAY_SETTINGS": [
            "monitor", "resolutionwidth", "resolutionheight", "windowmode",
            "aspectratio", "vsync", "useletterbox", "defaultfov",
        ],
        "CUSTOM_QUALITY": [
            "antialiasing", "atmospheric", "geometry", "lighting", "shadow",
            "sharpness", "texture", "vfx", "texturefiltering", "reflection",
            "ao", "lenseffects", "dof", "adaptiverenderscalingtargetfps",
            "renderscalingfactor", "dlssperfqual", "texturestreaming",
        ],
        "INPUT": [
            "invertaxisy", "invertmouseaxisy", "rumble", "aimassist",
            "yawsensitivity", "pitchsensitivity", "deadzoneleftstick",
            "deadzonerightstick", "deadzonetriggerleft", "deadzonetriggerright",
            "deadzoneswitchinputstick", "controllerstickrotationcurve",
            "mousescroll", "toggleaim", "toggleaimgamepad", "togglelean",
            "togglesprint", "togglecrouch", "toggleprone", "togglewalk",
            "toggledroneboost", "togglegadgetdeploymentgamepad",
            "togglegadgetdeploymentkeyboard", "aimdownsights",
            "adsmouseusespecific", "adsmousesensitivity3x",
            "adsmousesensitivity4x", "adsmousesensitivity5x",
            "adsmousesensitivity12x", "controlschemeindex",
            "controllerinputdevice",
        ],
        "AUDIO": [
            "subtitle", "mastervolume", "menumusicvolume", "ingamemusicvolume",
            "menusfxvolume", "ingamesfxvolume", "voicevolume", "dynamicrangemode",
            "monooutput", "voicechatplaybacklevel", "voicechatcapturethresholdv2",
            "voicechatcapturemode", "voicechatcapturelevel", "mute",
            "voicechatmuteall", "voicechatteamonly",
        ],
        "ONLINE": ["datacenterhint"],
    }

    def __init__(self):
        # --- Initialize window & ImGui ---
        imgui.create_context()
        self.window = pyglet.window.Window(
            width=800, height=750,
            caption=f"R6S Config Editor {VERSION}",
            resizable=True
        )
        self.impl = PygletRenderer(self.window)
        pyglet.clock.schedule_interval(self._update, 1/60.0)

        # --- State ---
        self.player_ids = get_configs()
        self.primary_index = 0
        self.secondary_index = 0
        self.show_all = False
        self.show_second = False

        # flat storage for settings
        self.primary_settings = self._make_empty_store()
        self.secondary_settings = self._make_empty_store()

        # load initial
        self._load(self.primary_index, self.primary_settings, all_keys=True)
        self._load(self.secondary_index, self.secondary_settings, all_keys=False)

        # event handlers
        @self.window.event
        def on_draw():
            self.render()

        @self.window.event
        def on_close():
            self.impl.shutdown()
            self.window.close()

        pyglet.app.run()

    def _make_empty_store(self):
        """Create a flat dict with all known keys initialized to empty str."""
        store = {}
        for cats in (self.IMPORTANT_CATEGORIES, self.ALL_CATEGORIES):
            for keys in cats.values():
                for k in keys:
                    store[k] = ""
        return store

    def _load(self, player_index, store, *, all_keys: bool):
        """Load either important only or all settings into store."""
        player_id = self.player_ids[player_index]
        cfg = get_player_config(player_id)
        # always load important first
        for section, keys in self.IMPORTANT_CATEGORIES.items():
            for key in keys:
                store[key] = self._safe_get(cfg, section, key)
        if all_keys:
            # load the rest
            for section, keys in self.ALL_CATEGORIES.items():
                for key in keys:
                    store[key] = self._safe_get(cfg, section, key)

    def _safe_get(self, cfg, section, key):
        """Try get_setting, fall back to get_int as str."""
        try:
            return cfg.get_setting(section, key)
        except Exception:
            return str(cfg.get_int(section, key))

    def _save(self, player_index, store, *, all_keys: bool):
        """Save either important only or all settings from store."""
        path = os.path.join(R6_PATH, self.player_ids[player_index], "GameSettings.ini")
        cfg = PlayerConfig(path)
        cats_to_save = [self.IMPORTANT_CATEGORIES]
        if all_keys:
            cats_to_save.append(self.ALL_CATEGORIES)

        for cats in cats_to_save:
            for section, keys in cats.items():
                for key in keys:
                    cfg.set_setting(section, key, store.get(key, ""))
        cfg.save()

    def _update(self, dt):
        pass  # nothing for now

    def render(self):
        glClearColor(0.1, 0.1, 0.1, 1)
        self.window.clear()
        imgui.new_frame()

        self._draw_main_panel()
        self._draw_primary_important()
        if self.show_all:
            self._draw_primary_all()
        if self.show_second:
            self._draw_secondary()

        imgui.render()
        self.impl.render(imgui.get_draw_data())

    # --- UI Panels ---

    def _draw_main_panel(self):
        imgui.set_next_window_position(10, 10, imgui.ONCE)
        imgui.set_next_window_size(300, 140, imgui.ONCE)
        imgui.begin("Config")

        imgui.text("Primary Profile:")
        changed, self.primary_index = imgui.combo(
            "##primary_combo", self.primary_index, self.player_ids
        )
        if changed:
            self._load(self.primary_index, self.primary_settings, all_keys=True)

        if imgui.button("Save Primary", width=120):
            self._save(self.primary_index, self.primary_settings, all_keys=self.show_all)

        imgui.separator()
        _, self.show_all = imgui.checkbox("Show All Settings", self.show_all)
        _, self.show_second = imgui.checkbox("Show Second Config", self.show_second)
        imgui.end()

    def _draw_primary_important(self):
        imgui.set_next_window_position(10, 160, imgui.ONCE)
        imgui.set_next_window_size(380, 580, imgui.ONCE)
        imgui.begin("Important Settings - Primary")
        self._render_group(self.primary_settings, self.IMPORTANT_CATEGORIES, prefix="pri")
        imgui.end()

    def _draw_primary_all(self):
        imgui.set_next_window_position(410, 10, imgui.ONCE)
        imgui.set_next_window_size(380, 710, imgui.ONCE)
        imgui.begin("All Settings - Primary")
        self._render_group(self.primary_settings, self.ALL_CATEGORIES, prefix="all")
        imgui.end()

    def _draw_secondary(self):
        imgui.set_next_window_position(410, 10, imgui.ONCE)
        imgui.set_next_window_size(380, 400, imgui.ONCE)
        imgui.begin("Second Config")

        imgui.text("Second Profile:")
        changed, self.secondary_index = imgui.combo(
            "##second_combo", self.secondary_index, self.player_ids
        )
        if changed:
            self._load(self.secondary_index, self.secondary_settings, all_keys=False)

        if imgui.button("Save Second", width=120):
            self._save(self.secondary_index, self.secondary_settings, all_keys=False)

        imgui.separator()
        self._render_group(self.secondary_settings, self.IMPORTANT_CATEGORIES, prefix="sec")
        imgui.end()

    def _render_group(self, store, categories, *, prefix):
        """Generic renderer for one or more categories of settings."""
        for section, keys in categories.items():
            opened, _ = imgui.collapsing_header(section, imgui.TREE_NODE_DEFAULT_OPEN)
            if not opened:
                continue
            imgui.columns(2, f"{prefix}_{section}", False)
            imgui.set_column_width(0, 160)
            for key in keys:
                imgui.text(key)
                imgui.next_column()
                imgui.push_item_width(-1)
                changed, val = imgui.input_text(f"##{prefix}_{section}_{key}", store[key], 512)
                if changed:
                    store[key] = val
                imgui.pop_item_width()
                imgui.next_column()
            imgui.columns(1)


if __name__ == "__main__":
    R6SConfigEditor()
