import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QPushButton,
    QWidget,
    QVBoxLayout,
    QLabel,
    QScrollArea,
    QLineEdit,
    QFormLayout,
    QComboBox
)

import capstone_functions

class Data_Entry_Page(QScrollArea):
    def __init__(self, main_window, parent=None):
        super(Data_Entry_Page, self).__init__()
        self.main_window = main_window
        
        self.containing_widget = QWidget()

        self.outerLayout = QVBoxLayout()

        self.entry_list = []

        self.cash_in_bank = QLineEdit()
        self.date=QLineEdit()
        self.cash_in_bank_layout = QFormLayout()
        self.cash_in_bank_layout.addRow('Cash In Bank (Required) [No commas]:', self.cash_in_bank) 
        self.cash_in_bank_layout.addRow('Date [Format: MM/DD/YYYY] (same date only):', self.date)

        # Button Basic Styling
        font = QtGui.QFont()
        font.setFamily("Montserrat")
        font.setPointSize(10)
        font.setBold(True)

        self.outerLayout.addLayout(self.cash_in_bank_layout)
        self.add_new_entry(font)

        self.containing_widget.setLayout(self.outerLayout)

        self.setWidgetResizable(True)
        self.setWidget(self.containing_widget)

        

    def hide_button(self, layout, button):
        layout.removeWidget(button)
        button.hide()

    def save_to_db(self):
        for element in self.entry_list: 
            capstone_functions.add_entry(element)
        self.main_window.switch_page(2)
        self.main_window.go_to_SCP_page(self.date.text())

    def add_new_entry(self, font):
        self.entry_layout = QVBoxLayout()
        self.entry_form_layout = QFormLayout()

        name= QLineEdit()
        amount=QLineEdit()
        flow_type=QComboBox()
        flow_type.addItems(["Inflow", "Outflow"])
        category=QComboBox()
        category.addItems(["Operating", "Investing", "Financing"])

        self.entry_form_layout.addRow('Entry Title:',name)
        self.entry_form_layout.addRow('Amount [Format: No Commas] (Required):', amount)
        self.entry_form_layout.addRow('Flow Type:', flow_type)
        self.entry_form_layout.addRow('Category:', category)
    
        self.save_2list_button = QPushButton('Save')
        self.save_2list_button.setFont(font)
        self.save_2list_button.clicked.connect(lambda: self.entry_list.append({"entry_title":name.text(), "date":self.date.text(), "amount":int(amount.text()), "flow_type":flow_type.currentText(), "category":category.currentText(),"cash_in_bank":int(self.cash_in_bank.text())}))
        self.save_2list_button.clicked.connect(lambda: self.hide_button(self.entry_form_layout, self.save_2list_button))
        
        self.add_entry_button = QPushButton('Add Entry')
        self.add_entry_button.setFont(font)
        
        self.done_button = QPushButton("Done")
        self.done_button.setFont(font)

        self.add_entry_button.clicked.connect(lambda: self.hide_button(self.entry_form_layout, self.done_button))
        self.done_button.clicked.connect(lambda: self.save_to_db())

        self.add_entry_button.clicked.connect(lambda: self.hide_button(self.entry_form_layout, self.add_entry_button))
        self.add_entry_button.clicked.connect(lambda: self.add_new_entry(font))

        self.entry_form_layout.addWidget(self.save_2list_button)
        self.entry_form_layout.addWidget(self.add_entry_button)
        self.entry_form_layout.addWidget(self.done_button)
        
        self.spacer_label = QLabel()
        self.spacer_label.setText("")
        self.spacer_label.setFont(font)
        self.entry_layout.addWidget(self.spacer_label)

        self.entry_layout.addLayout(self.entry_form_layout)
        self.entry_layout.addStretch()
        self.outerLayout.addLayout(self.entry_layout)