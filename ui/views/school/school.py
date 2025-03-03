from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import pyqtSignal

from ui.views.InputModule import InputModule

class School(QWidget):    
    number_pressed = pyqtSignal(str)  
    sign_pressed = pyqtSignal(str)       
  
    def __init__(self):
        super().__init__() 
        uic.loadUi("ui/views/school/school.ui", self) 
        inputWidget = self.findChild(QWidget, "InputModul") 

        layout = QVBoxLayout()
        inputWidget.setLayout(layout)

        self.input_module = InputModule()
        layout.addWidget(self.input_module)

        self.input_module.number_pressed.connect(self.setText)
        self.input_module.sign_pressed.connect(self.setText)

    def setText(self, text):
        if text == '=':
            self.calculate()
            return
        valueText = self.inputString.text() + text
        self.inputString.setText(valueText)

    def calculate(self):

        inputString = self.inputString.text()       
        average = self.average_grade(inputString)

        self.gradesAVG.setText(str(average))  
        self.gradesSUM.setText(str(self.sum_grades(inputString))) 
        self.gradesRecommodation.setText(self.recommendation(average))

    def filter_valid_grades(self, grades_text):
        valid_grades = []
        for char in grades_text:
            if char in '123456':
                valid_grades.append(int(char))
        return valid_grades      
    
    def count_grades(self, grades_text):       
        valid_grades = self.filter_valid_grades(grades_text)
        return len(valid_grades)
    
    def sum_grades(self, grades_text):       
        valid_grades = self.filter_valid_grades(grades_text)
        return sum(valid_grades)
    
    def average_grade(self, grades_text):    
        total = self.sum_grades(grades_text)
        count = self.count_grades(grades_text)
        
        if count == 0:
            return 0.0
        
        average = round(total / count, 2)
        return average
    
    def recommendation(self, average):
        if average >= 5.5:
            return "Note 6"
        elif average >= 4.5:
            return "Note 5"
        elif average >= 3.5:
            return "Note 4"
        elif average >= 2.5:
            return "Note 3"
        elif average >= 1.5:
            return "Note 2"
        elif average >= 1.0:
            return "Note 1"
        else:
            return "Ungültiger Durchschnitt"