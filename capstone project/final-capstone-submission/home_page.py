import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLabel
)

class Home_Page(QWidget):
    def __init__(self, main_window, parent=None):
        super(Home_Page, self).__init__()
        self.main_window = main_window

        self.outerLayout = QVBoxLayout()

        self.topLayout = QVBoxLayout()

        self.app_name_label = QLabel()
        self.app_name_label.setObjectName("app_name_label")
        self.app_name_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        font = QtGui.QFont()
        font.setFamily("Montserrat ExtraBold")
        font.setPointSize(30)
        font.setBold(True)
        self.app_name_label.setText("Statement of Cash Position Generator")
        self.app_name_label.setFont(font)
        
        self.topLayout.addWidget(self.app_name_label)

        self.bottomLayout = QVBoxLayout()
        
        # Button Basic Styling
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)

        self.data_entry_button = QPushButton("Create New Entries")
        self.data_entry_button.setFont(font)
        self.data_entry_button.clicked.connect(lambda: self.main_window.switch_page(1))

        self.view_scps_button = QPushButton("View Existing SCPs")
        self.view_scps_button.setFont(font)
        self.data_entry_button.clicked.connect(lambda: self.main_window.switch_page(3))
        
    
        self.bottomLayout.addWidget(self.data_entry_button)
        self.bottomLayout.addWidget(self.view_scps_button)

        self.outerLayout.addLayout(self.topLayout)
        self.outerLayout.addLayout(self.bottomLayout)
        self.setLayout(self.outerLayout)