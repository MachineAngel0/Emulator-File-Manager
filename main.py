import sys

from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, \
    QWidget, QFormLayout

from WindowGUI import MainWindow

from PyQt6 import QtCore, QtGui, QtWidgets

from output import Ui_MainWindow


# File path to designer "C:\Users\Adams Humbert\AppData\Local\Programs\Python\Python313\Lib\site-packages\PySide6\designer.exe"

# setup
#

# utility




class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(100, 100)

        self.btn = QPushButton("EmulatorFileManager", self)

        self.btn.clicked.connect(self.clickHandler)

    # lets the user find a file
    def clickHandler(self):
        dialog = QFileDialog()
        dialog.exec()

        selectedFiles = dialog.selectedFiles()
        print(selectedFiles)
        self.btn.setText(selectedFiles[0])




if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = Window()
    window = MainWindow()
    window.show()
    app.exec()


    '''
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
    '''
