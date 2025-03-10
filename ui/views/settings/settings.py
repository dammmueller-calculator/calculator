from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from PyQt6.QtWidgets import QMainWindow


class Settings(QMainWindow):
    settngs_changed = pyqtSignal()

    settings = {
        "history_path": "history.txt",
        "key": "mysecretkey12345",
        "theme": "light",
        "font_size": "medium",
        "font": "arial",
    }
    settings_cache = settings.copy()

    font_select = {
        0: "arial",
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

    def __init__(self, fileSettings=None):
        super().__init__()
        uic.loadUi("ui/views/settings/settings.ui", self)

        if fileSettings is not None:
            self.settings = fileSettings

        self.fontSelect.currentIndexChanged.connect(self.change_font)
        self.fontSizeSelect.currentIndexChanged.connect(self.change_font_size)
        self.themeSelect.currentIndexChanged.connect(self.change_theme)
        self.historySelect.textChanged.connect(self.change_history_path)
        self.secretKeySelect.textChanged.connect(self.change_key)

        self.update_ui_from_settings()

    def apply_changes(self):
        self.settings = self.settings_cache.copy()
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
        self.fontSelect.setCurrentIndex(font_index)

        # Set the font size combo box
        font_size_index = list(self.font_size_select.values()).index(
            self.settings["font_size"]
        )
        self.fontSizeSelect.setCurrentIndex(font_size_index)

        # Set the theme combo box
        theme_index = list(self.theme_select.values()).index(self.settings["theme"])
        self.themeSelect.setCurrentIndex(theme_index)

        # Set the history path text field
        self.historySelect.setText(self.settings["history_path"])

        # Set the key text field
        self.secretKeySelect.setText(
            self.settings["key"].decode()
            if isinstance(self.settings["key"], bytes)
            else self.settings["key"]
        )

    def get_settings(self):
        return self.settings

    def change_font(self):
        self.settings_cache["font"] = self.font_select[self.fontSelect.currentIndex()]

    def change_font_size(self):
        self.settings_cache["font_size"] = self.font_size_select[
            self.fontSizeSelect.currentIndex()
        ]

    def change_theme(self):
        self.settings_cache["theme"] = self.theme_select[
            self.themeSelect.currentIndex()
        ]

    def change_history_path(self):
        self.settings_cache["history_path"] = self.historySelect.toPlainText()

    def change_key(self):
        self.settings_cache["key"] = self.secretKeySelect.toPlainText()
