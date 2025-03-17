import sys

from PyQt6.QtWidgets import QApplication

from WindowGUI import MainWindow




# File path to designer "C:\Users\Adams Humbert\AppData\Local\Programs\Python\Python313\Lib\site-packages\PySide6\designer.exe"


if __name__ == "__main__":
    app = QApplication(sys.argv)
    # window = Window()
    window = MainWindow()
    window.show()
    app.exec()


