import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

from DirectoryIterator import iterate_through_files


class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(100, 100)

        btn = QPushButton('Quit', self)
        self.setCentralWidget(btn)

        btn.clicked.connect(self.clickHandler)


    # lets the user find a file
    def clickHandler(self):
        dialog = QFileDialog()
        dialog.exec()

        selectedFiles = dialog.selectedFiles()
        print(selectedFiles)


if __name__ == "__main__":
    iterate_through_files()
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    app.exec()
