import os

from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QFrame,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
)

# Import Source
from src.history import decrypt_file, encrypt_file
from ui.views.BasicModule import BasicModule
import src.settings

# Import your view modules
from ui.views.geometry import Geometry
from ui.views.percent import Percent
from ui.views.settings import Settings
from ui.views.startScreen import StartScreen
from ui.views.school import School
from ui.views.BasicModule import BasicModule
from ui.views.MathematicalFunctions import MathematicalFunctions
from ui.views.Informatik import Informatik


class MainWindow(QMainWindow):
    history = []

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/main_window.ui", self)

        self.menu_frame = self.findChild(QFrame, "menuFrame")
        self.stacked_widget = self.findChild(QStackedWidget, "modules")

        # Initialize the start screen widget (this will be the default screen)
        self.start_screen = StartScreen(self.history)  # Pass history to start screen
        self.stacked_widget.addWidget(
            self.start_screen
        )  # Add start screen as the first widget
        self.view_mapping = {"Start Screen": 0}

        # Add the start screen widget as one of the views
        self.views = [
            {"name": "Start Screen", "widget": self.start_screen},
            {"name": "Geometry", "widget": Geometry()},
            {"name": "Percent", "widget": Percent(self)},
            {"name": "Basic Module", "widget": BasicModule(self)},
            {"name": "School", "widget": School(self)},
            {"name": "Mathematical Functions", "widget": MathematicalFunctions(self)},
            {"name": "Informatik", "widget": Informatik(self)}
        ]

        self.view_mapping = {}
        for view in self.views:
            self.stacked_widget.addWidget(view["widget"])
            self.view_mapping[view["name"]] = self.stacked_widget.indexOf(
                view["widget"]
            )

        # Add menu buttons dynamically (to switch between views)
        self.stacked_widget.setCurrentWidget(self.start_screen)
        self.add_menu_buttons()
        self.ensure_connection()

        self.settings_window = self.loadSettings()
        self.settings_window.settngs_changed.connect(self.apply_settings)
        self.settings = self.settings_window.get_settings()
        self.showHistory()

        self.settings_window.history_export.connect(self.export_history)

    def add_menu_buttons(self):
        """Create buttons dynamically and add them to the menu frame with minimal spacing."""
        layout = QVBoxLayout(self.menu_frame)
        layout.setSpacing(1)  # Set small spacing between buttons
        layout.setContentsMargins(0, 0, 0, 0)  # Remove extra margins

        for view in self.views:
            button = QPushButton(view["name"], self)
            button.clicked.connect(self.create_view_switcher(view["name"]))
            layout.addWidget(button)

        self.menu_frame.setLayout(layout)

    def create_view_switcher(self, view_name):
        """Return a function to switch to a specific view."""

        def switch_view():
            index = self.view_mapping.get(view_name, -1)
            if 0 <= index < self.stacked_widget.count():
                self.stacked_widget.setCurrentIndex(index)

        return switch_view

    def loadSettings(self):
        try:
            config = src.settings.load_config("settings.json")
            return Settings(config)

        except ValueError:
            return Settings()

    def ensure_connection(self):
        """Method for ensuring connections if needed."""
        pass

    def open_settings(self):
        self.settings_window.show()

    def apply_settings(self):
        self.settings = self.settings_window.get_settings()

    def showHistory(self):
        self.history = decrypt_file(self.settings["history_path"], self.settings["key"])
        self.start_screen.update_history(self.history)  # Update history in start screen

    def appendHistory(self, expression):
        self.history.append(expression)
        self.start_screen.update_history(self.history)  # Update history in start screen

    def finalizeHistory(self):
        encrypt_file(self.history, self.settings["key"], self.settings["history_path"])

    def export_history(self):
        output = decrypt_file(self.settings["history_path"], self.settings["key"])
        with open("history_out.txt", "w") as file:
            file.write("\n".join(output))

if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    # Load and apply the QSS stylesheet
    with open("styles.qss", "r") as file:
        qss = file.read()
        app.setStyleSheet(qss)

    window = MainWindow()
    window.show()
    app.exec()
    window.finalizeHistory()
