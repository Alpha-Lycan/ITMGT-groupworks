import sys

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QStackedLayout
)

from home_page import Home_Page
from data_entry_page import Data_Entry_Page
from scp_page import SCP_Page

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # set title and size of window
        self.setWindowTitle("Statement of Cash Position")
        self.resize(850,600)
        
        # set the main layout of the window
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # create a stacked layout for switching pages
        self.stackedLayout = QStackedLayout()

        # PAGE 1: Home Page
        self.page1 = Home_Page(self)        
        
        # PAGE 2: Data Entry Page
        self.page2 = Data_Entry_Page(self)

        # add the pages to the stackedLayout
        self.stackedLayout.addWidget(self.page1)
        self.stackedLayout.addWidget(self.page2)
        
        # add stackedLayout to the mainLayout
        self.main_layout.addLayout(self.stackedLayout)


    def switch_page(self, index):
        self.stackedLayout.setCurrentIndex(index)


    def go_to_SCP_page(self, date):
        # PAGE 3: View SCP for Entered Data Page
        self.page3 = SCP_Page(self, date)
        self.stackedLayout.addWidget(self.page3)
        self.stackedLayout.setCurrentIndex(2)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()   
    window.show()
    sys.exit(app.exec())