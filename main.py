from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QStackedWidget, QMainWindow, QPushButton, QVBoxLayout, QFrame
from PyQt6.QtCore import QStringListModel

# Import your view modules
from ui.views.geometry import Geometry
from ui.views.BasicModule import BasicModule

# Import Source
from src.history import encrypt_file, decrypt_file

class MainWindow(QMainWindow):
    key = b"mysecretkey12345"
    history = []

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/main_window.ui", self)
        self.showHistory()

        self.menu_frame = self.findChild(QFrame, "menuFrame")
        self.stacked_widget = self.findChild(QStackedWidget, "modules")

        # Initialize views
        self.views = [
            {"name": "Geometry", "widget": Geometry(self)},
            {"name": "Basic Module", "widget": BasicModule()},
        ]

        self.view_mapping = {}
        for view in self.views:
            self.stacked_widget.addWidget(view["widget"])
            self.view_mapping[view["name"]] = self.stacked_widget.indexOf(
                view["widget"]
            )

        self.add_menu_buttons()
        self.ensure_connection()

    def ensure_connection(self):
        """Method for ensuring connections if needed."""
        pass

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

    def showHistory(self):
        self.history = decrypt_file("history.txt", self.key)
        model = QStringListModel(self.history)
        self.historyList.setModel(model)

    def appendHistory(self, expression):
        self.history.append(expression)
        model = QStringListModel(self.history)
        self.historyList.setModel(model)


    def finalizeHistory(self):
        encrypt_file(self.history, self.key)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    window.finalizeHistory()
