# Filename: f_layout.py

"""Form layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from capstone_project import *


app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Statement of Cash Position')
layout = QFormLayout()

def hidebutton(but):
    layout.removeWidget(but)
    but.hide()
cash_in_bank=QLineEdit()
layout.addRow('Cash In Bank:', cash_in_bank) 
entry_list=[]
def new_entry(): 
    name= QLineEdit()
    date=QLineEdit()
    amount=QLineEdit()
    flow_type=QLineEdit()
    category=QLineEdit()
    layout.addRow('Entry Title:',name)
    layout.addRow('Date:', date)
    layout.addRow('Amount:', amount)
    layout.addRow('Flow Type:', flow_type)
    layout.addRow('Category:', category)
    save_2list = QPushButton('Save')
    save_2list.clicked.connect(lambda: entry_list.append({"entry_title":name.text(), "date":date.text(), "amount":int(amount.text()), "flow_type":flow_type.text(), "category":category.text(),"cash_in_bank":int(cash_in_bank.text())}))
    save_2list.clicked.connect(lambda: hidebutton(save_2list))
    addent = QPushButton('Add Entry')
    addent.clicked.connect(lambda: new_entry())
    addent.clicked.connect(lambda: hidebutton(addent))
    layout.addWidget(save_2list)
    layout.addWidget(addent)
new_entry()
def save_to_db():
    for element in entry_list: 
        add_entry(element)
addtodb = QPushButton('Done')
addtodb.clicked.connect(lambda: save_to_db()) 
layout.addWidget(addtodb)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())