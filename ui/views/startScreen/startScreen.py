from PyQt6 import uic
from PyQt6.QtCore import QStringListModel
from PyQt6.QtWidgets import QListView, QWidget


class StartScreen(QWidget):
    def __init__(self, history, parent=None):
        super().__init__()
        self.parent = parent
        uic.loadUi("ui/views/startScreen/start_screen.ui", self)

        # Assuming you have a QListView named historyList in your UI
        self.historyList = self.findChild(QListView, "historyList")

        self.history_model = QStringListModel(history)
        self.historyList.setModel(self.history_model)

    def update_history(self, history):
        # Update the history in the model
        self.history_model.setStringList(history)
