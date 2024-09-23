from PyQt6 import QtWidgets, uic
from PyQt6.QtWidgets import QStackedWidget, QListWidget, QMainWindow, QListWidgetItem

# Import your view modules
from ui.views.geometry import Geometry


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi("ui/main_window.ui", self)

        self.menu = self.findChild(QListWidget, "moduleList")
        self.stacked_widget = self.findChild(QStackedWidget, "modules")

        # Initialize views
        self.views = [
            {"name": "Geometry", "widget": Geometry()},
        ]

        self.view_mapping = {}
        for view in self.views:
            self.stacked_widget.addWidget(view["widget"])
            self.view_mapping[view["name"]] = self.stacked_widget.indexOf(
                view["widget"]
            )

        self.add_menu_items()
        self.ensure_connection()

    def ensure_connection(self):
        try:
            self.menu.itemClicked.disconnect(self.display_view)
        except TypeError:
            pass
        self.menu.itemClicked.connect(self.display_view)

    def add_menu_items(self):
        self.menu.clear()
        for view in self.views:
            item = QListWidgetItem(view["name"])
            self.menu.addItem(item)

    def display_view(self, item):
        item_text = item.text()
        index = self.view_mapping.get(item_text, -1)
        if 0 <= index < self.stacked_widget.count():
            self.stacked_widget.setCurrentIndex(index)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
