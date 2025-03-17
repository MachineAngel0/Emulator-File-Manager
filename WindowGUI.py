from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QHBoxLayout, QVBoxLayout, QLabel, \
    QWidget, QFormLayout, QComboBox
from PyQt6.uic import loadUi
from PyQt6.uic.Compiler.qtproxies import QtCore
from PySide6.QtCore import QSize
from PyQt6 import QtCore, QtGui, QtWidgets

import DirectoryIterator


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        loadUi("EmulatorFileManager3.ui", self)

        # init the drop box

        self.add_emulators_to_drop_down()

        # TODO: read and write to save files
        for i in DirectoryIterator.emulators_names:
            self.generate_layout(i)



    def add_emulators_to_drop_down(self):
        emulator_drop_box = self.findChild(QComboBox, "EmulatorDropBox")

        emulator_drop_box.clear()

        for i in DirectoryIterator.emulators_names:
            emulator_drop_box.addItem(i)


    def generate_layout(self, EmulatorName):
        # TODO: extract out into a function call later
        # get the vertical layout
        self.VerticalLayout = self.findChild(QVBoxLayout, "VFileLayout")

        # needed for alignment
        _translate = QtCore.QCoreApplication.translate

        # make horizontal layout and set horizontal layout name
        self.HLayout = QHBoxLayout()
        self.HLayout.setObjectName("testLayout")

        self.Label_EmulatorName = QLabel(parent=self.centralwidget)
        self.Label_EmulatorName.setMinimumSize(64, 32)
        self.Label_EmulatorName.setScaledContents(False)
        self.Label_EmulatorName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Label_EmulatorName.setObjectName("Test_ds")
        self.Label_EmulatorName.setText("Test_ds")
        self.Label_EmulatorName.setText(_translate("MainWindow", EmulatorName))

        self.Label_exe = QLabel(parent=self.centralwidget)
        self.Label_exe.setObjectName("label_16")
        self.Label_exe.setText("Exe Location")

        self.Button_ExeLocation = QPushButton(parent=self.centralwidget)
        self.Button_ExeLocation.setObjectName("ExeLocation_FileDialogue_2")
        self.Button_ExeLocation.setText("C://")
        self.Button_ExeLocation.setMaximumSize(QtCore.QSize(256, 32))

        # button binding
        self.Button_ExeLocation.clicked.connect(lambda state, x = self.Button_ExeLocation: self.file_picker(x))

        self.Label_GameFolder = QLabel(parent=self.centralwidget)
        self.Label_GameFolder.setObjectName("label_17")
        self.Label_GameFolder.setText("Game Folder:")

        self.Button_GameFolder = QPushButton(parent=self.centralwidget)
        self.Button_GameFolder.setObjectName("pushButton_25")
        self.Button_GameFolder.setText("C://")
        self.Button_GameFolder.setMaximumSize(QtCore.QSize(256, 32))
        # button binding
        self.Button_GameFolder.clicked.connect(lambda state, x=self.Button_GameFolder: self.file_picker(x))

        self.Button_OpenExe = QPushButton(parent=self.centralwidget)
        self.Button_OpenExe.setObjectName("pushButton_38")
        self.Button_OpenExe.setText("Launch")
        # bind to open EXE file
        self.Button_OpenExe.clicked.connect(lambda state, x = self.Button_ExeLocation.text(): self.open_exe(x))


        # add labels and buttons to the horizontal layout
        self.HLayout.addWidget(self.Label_EmulatorName)
        self.HLayout.addWidget(self.Label_exe)
        self.HLayout.addWidget(self.Button_ExeLocation)
        self.HLayout.addWidget(self.Label_GameFolder)
        self.HLayout.addWidget(self.Button_GameFolder)
        self.HLayout.addWidget(self.Button_OpenExe)
        # add horizontal layout to the vertical layout
        self.VerticalLayout.addLayout(self.HLayout)


    def find_emulators_handler(self):
        print("insert directory searcher here")

    def file_picker(self, buttonRef):
        dialog = QFileDialog()
        dialog.exec()

        selectedFiles = dialog.selectedFiles()
        print(selectedFiles)
        buttonRef.setText(selectedFiles[0])

    def open_exe(self, file_path):
        print("Open Exe")
        print(file_path)


