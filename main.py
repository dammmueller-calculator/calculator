import json
import importlib
import datetime
from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import (
    QFrame,
    QMainWindow,
    QPushButton,
    QStackedWidget,
    QVBoxLayout,
)
import src.settings
from src.history import decrypt_file, encrypt_file

# Import your mandatory views directly.
from ui.views.startScreen.startScreen import StartScreen
from ui.views.BasicModule.BasicModule import BasicModule
from ui.views.settings.settings import (
    Settings,
)  # Adjust this if your settings view is named differently


class MainWindow(QMainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.ui = uic.loadUi("ui/main_window.ui", self)
        self.app = app

        # Initialize attributes early so that any view can safely call back.
        self.history = []
        self.views = []  # This will hold both mandatory and dynamic views.
        self.view_mapping = {}

        self.menu_frame = self.findChild(QFrame, "menuFrame")
        self.stacked_widget = self.findChild(QStackedWidget, "modules")

        # 1. Load mandatory views.
        self.views = self.load_mandatory_views()

        # 2. Load additional views dynamically from config.json.
        dynamic_views = self.load_dynamic_views("config.json")
        self.views.extend(dynamic_views)

        # Add all views to the stacked widget and build a mapping.
        for view in self.views:
            self.stacked_widget.addWidget(view["widget"])
            self.view_mapping[view["name"]] = self.stacked_widget.indexOf(
                view["widget"]
            )

        # Set default view to the first one.
        if self.views:
            self.stacked_widget.setCurrentWidget(self.views[0]["widget"])
        self.add_menu_buttons()
        self.ensure_connection()

        # Load settings window (if applicable).
        self.settings_window = self.loadSettings()
        self.settings_window.settings_changed.connect(self.apply_settings)
        self.settings = self.settings_window.get_settings()
        self.showHistory()
        self.settings_window.history_export.connect(self.export_history)

    def load_mandatory_views(self):
        """
        Hardcode the mandatory views.
        Change these imports and instantiations as needed.
        """
        mandatory = []
        # Create mandatory view instances.
        mandatory.append({"name": "Start Screen", "widget": StartScreen(self)})
        mandatory.append({"name": "Basic Module", "widget": BasicModule(self)})
        return mandatory

    def load_dynamic_views(self, config_path):
        """
        Load additional views from config.json.
        The config.json should have entries with a display name and a class name.
        For example:
        {
          "views": [
            { "name": "Geometry", "class": "Geometry" },
            { "name": "Percent", "class": "Percent" },
            { "name": "School", "class": "School" },
            { "name": "Math", "class": "MathematicalFunctions" },
            { "name": "Informatik", "class": "Informatik" }
          ]
        }
        """
        dynamic_views = []
        try:
            with open(config_path, "r") as file:
                config = json.load(file)
        except Exception as e:
            print(f"Failed to load config: {e}")
            return dynamic_views

        for view_data in config.get("views", []):
            display_name = view_data["name"]
            class_name = view_data["class"]

            view_class = self.load_view_class(class_name)
            if view_class:
                view_instance = view_class(self)
                dynamic_views.append({"name": display_name, "widget": view_instance})
            else:
                print(f"Failed to load view for class {class_name}")
        return dynamic_views

    def load_view_class(self, class_name):
        """
        Try to import a view class from ui/views/<folder>/<file>.
        We try several options to accommodate different naming conventions.
        For example, for "Informatik", if the folder is "Informatik" but the file is "informatik.py":
          Option A: ui.views.Informatik.Informatik
          Option B: ui.views.Informatik.informatik
          Option C: ui.views.informatik.Informatik
          Option D: ui.views.informatik.informatik
        """
        options = []
        # Option A: Folder and file exactly as given (e.g. Informatik/Informatik.py)
        options.append(f"ui.views.{class_name}.{class_name}")
        # Option B: Folder as given, file name lower-cased (e.g. Informatik/informatik.py)
        options.append(f"ui.views.{class_name}.{class_name.lower()}")
        # Option C: Folder lower-cased, file as given (e.g. informatik/Informatik.py)
        options.append(f"ui.views.{class_name.lower()}.{class_name}")
        # Option D: Folder and file lower-cased (e.g. informatik/informatik.py)
        options.append(f"ui.views.{class_name.lower()}.{class_name.lower()}")

        for module_path in options:
            try:
                module = importlib.import_module(module_path)
                return getattr(module, class_name)
            except (ModuleNotFoundError, AttributeError) as e:
                continue
        print(
            f"Error loading view {class_name}: could not find module in any expected path."
        )
        return None

    def add_menu_buttons(self):
        """Dynamically create and add buttons to the menu."""
        layout = QVBoxLayout(self.menu_frame)
        layout.setSpacing(1)
        layout.setContentsMargins(0, 0, 0, 0)

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
        """
        Load the settings window.
        This function expects src/settings.load_config and a SettingsView.
        Adjust as necessary for your application.
        """
        try:
            config = src.settings.load_config("settings.json")
            from ui.views.settings.settings import (
                Settings,
            )  # Adjust if your settings window is elsewhere.

            return Settings(app=self.app, fileSettings=config)
        except ValueError:
            from ui.views.settings.settings import Settings

            return Settings(app=self.app)

    def ensure_connection(self):
        """Placeholder for additional signal/slot connections."""
        pass

    def open_settings(self):
        self.settings_window.show()

    def apply_settings(self):
        self.settings = self.settings_window.get_settings()

    def showHistory(self):
        self.history = decrypt_file(self.settings["history_path"], self.settings["key"])
        # If the first view has update_history, update it.
        if self.views and hasattr(self.views[0]["widget"], "update_history"):
            self.views[0]["widget"].update_history(self.history)

    def appendHistory(self, expression):
        expr = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + ": " + expression
        self.history.append(expr)
        if self.views:
            widget = self.views[0]["widget"]
            if hasattr(widget, "update_history"):
                widget.update_history(self.history)

    def finalizeHistory(self):
        encrypt_file(self.history, self.settings["key"], self.settings["history_path"])

    def export_history(self):
        output = decrypt_file(self.settings["history_path"], self.settings["key"])
        with open("history_out.txt", "w") as file:
            file.write("\n".join(output))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow(app=app)
    window.show()
    app.exec()
    window.finalizeHistory()
