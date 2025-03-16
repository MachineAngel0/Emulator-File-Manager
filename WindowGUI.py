

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, \
    QWidget, QFormLayout
from PyQt6.uic import loadUi
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi("EmulatorFileManager2.ui", self)
        #self.dialogueButton = self.findChild(QPushButton, "ExeLocation_FileDialogue")
        #self.dialogueButton.clicked.connect(self.ButtonTest)

        #self.FormLayout = self.findChild(QFormLayout, "EmulatorForm")
        #self.FormLayout.addWidget(QPushButton("hi"))

        self.FindEmulator_Button = self.findChild(QPushButton, "Button_FindEmulators")
        self.FindEmulator_Button.clicked.connect(self.FindEmulators_Handler)

    def FindEmulators_Handler(self):
        print("insert directory searcher here")


    def ButtonTest(self):
        print("Hello")