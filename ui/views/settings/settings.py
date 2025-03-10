from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QMainWindow


class Settings(QMainWindow):
    settngs_changed = pyqtSignal()
    history_export = pyqtSignal()

    settings = {
        "history_path": "history.txt",
        "key": "mysecretkey12345",
        "theme": "light",
        "font_size": "small",
        "font": "Arial",
    }
    settings_cache = settings.copy()

    font_select = {
        0: "Arial",
        1: "Times New Roman",
        2: "DejaVu Sans",
    }

    font_size_select = {
        0: "medium",
        1: "small",
        2: "large",
    }

    theme_select = {
        0: "light",
        1: "dark",
    }

    FONT_SIZES = {
        "small": 10,
        "medium": 15,
        "large": 20,
        }

    def __init__(self, app, fileSettings=None):
        super().__init__()
        self.ui = uic.loadUi("ui/views/settings/settings.ui", self)

        self.app = app

        if fileSettings is not None:
            self.settings = fileSettings

        self.cb_font.currentIndexChanged.connect(self.change_font)
        self.cb_font_size.currentIndexChanged.connect(self.change_font_size)
        self.cb_theme.currentIndexChanged.connect(self.change_theme)
        self.ip_history.textChanged.connect(self.change_history_path)
        self.ip_secret_key.textChanged.connect(self.change_key)

        self.update_ui_from_settings()

    def apply_changes(self):
        self.settings = self.settings_cache.copy()

        size = self.FONT_SIZES[self.settings["font_size"]]
        self.app.setFont(QFont(self.settings["font"], size))

        self.settngs_changed.emit()
        self.close()

    def revert_settings(self):
        """Revert the settings cache and UI elements to match the original settings."""
        self.settings_cache = self.settings.copy()
        self.update_ui_from_settings()

    def discard_changes(self):
        self.revert_settings()
        self.close()

    def update_ui_from_settings(self):
        """Update the UI elements to match the current settings."""
        font_index = list(self.font_select.values()).index(self.settings["font"])
        self.cb_font.setCurrentIndex(font_index)

        # Set the font size combo box
        font_size_index = list(self.font_size_select.values()).index(
            self.settings["font_size"]
        )
        self.cb_font_size.setCurrentIndex(font_size_index)

        # Set the theme combo box
        theme_index = list(self.theme_select.values()).index(self.settings["theme"])
        self.cb_theme.setCurrentIndex(theme_index)

        # Set the history path text field
        self.ip_history.setText(self.settings["history_path"])

        # Set the key text field
        self.ip_secret_key.setText(
            self.settings["key"].decode()
            if isinstance(self.settings["key"], bytes)
            else self.settings["key"]
        )

    def get_settings(self):
        return self.settings

    def change_font(self):
        self.settings_cache["font"] = self.font_select[self.cb_font.currentIndex()]

    def change_font_size(self):
        self.settings_cache["font_size"] = self.font_size_select[
            self.cb_font_size.currentIndex()
        ]

    def change_theme(self):
        self.settings_cache["theme"] = self.theme_select[self.cb_theme.currentIndex()]

    def change_history_path(self):
        self.settings_cache["history_path"] = self.ip_history.toPlainText()

    def change_key(self):
        self.settings_cache["key"] = self.ip_secret_key.toPlainText()

    def export_history(self):
        self.history_export.emit()
