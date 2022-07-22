import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QScrollArea,
    QGridLayout,
    QFrame
)
from PyQt5.QtCore import Qt

import capstone_functions

class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)

class SCP_Page(QScrollArea):
    def __init__(self, main_window, date, parent=None):
        super(SCP_Page, self).__init__()
        self.main_window = main_window
        
        self.containing_widget = QWidget()

        self.outerLayout = QGridLayout()

        self.separatorLine = QFrame()
        self.separatorLine.setFrameShape(QFrame.HLine)

        self.separatorLine.setStyleSheet("font: 3pt;")
        self.separatorLine.setLineWidth(0)
        self.separatorLine.setMidLineWidth(10)

        rect = self.separatorLine.frameRect()
        print("frameShape: %s" % rect)
        print("width: %s" % self.separatorLine.width())
        print("height: %s" % self.separatorLine.height())


        self.wanted_date = date

        self.entry_list = []
        
        self.wanted_date_entries = capstone_functions.get_entries({"date":self.wanted_date})
        self.results = capstone_functions.compute_values(self.wanted_date_entries, self.wanted_date_entries[0]["cash_in_bank"])

        #operating
        self.op_in=False  
        self.op_out=False 
    
        #investing
        self.inv_in=False 
        self.inv_out=False 
        
        #financing
        self.fin_in=False 
        self.fin_out=False 
        
        for entry in self.wanted_date_entries: 
            if entry["category"]=="Operating":
                if entry["flow_type"]=="Inflow":
                    self.op_in=True
                else:
                    self.op_out=True
            elif entry["category"]=="Investing":
                if entry["flow_type"]=="Inflow":
                    self.inv_in=True
                else:
                    self.inv_out=True
            elif entry["category"]=="Financing":
                if entry["flow_type"]=="Inflow":
                    self.fin_in=True
                else:
                    self.fin_out=True 

        current_row=0

        self.outerLayout.addWidget(QLabel('<b>Statement of Cash Position</b>'), current_row,0,1,4, Qt.AlignCenter)
        current_row+=1
        self.outerLayout.addWidget(QLabel("<b>"+self.wanted_date+"</b>"), current_row,0,1,4, Qt.AlignCenter)

        #operating
        if (self.op_in or self.op_out) == True:
            current_row+=1
            self.outerLayout.addWidget(QLabel("<b>Cash flows from operating activities</b>"),current_row,0,1,1)
            if self.op_in ==True: 
                current_row+=1
                self.outerLayout.addWidget(QLabel("Inflow"), current_row,0,1,1)
                for i in range(len(self.wanted_date_entries)): 
                    if self.wanted_date_entries[i]["category"]=='Operating' and self.wanted_date_entries[i]["flow_type"]=="Inflow": 
                        current_row+=1
                        self.outerLayout.addWidget(QLabel(self.wanted_date_entries[i]['entry_title']), current_row,1,1,1)
                        self.outerLayout.addWidget(QLabel(str(self.wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
                    if i == len(self.wanted_date_entries)-1:
                        self.outerLayout.addWidget(QLabel(str(self.results[0])), current_row,4, Qt.AlignRight)
                        self.outerLayout.addWidget(QHLine(), current_row,3, Qt.AlignBottom)
            if self.op_out==True: 
                current_row+=1
                self.outerLayout.addWidget(QLabel("Outflow"), current_row,0,1,1)
                for i in range(len(self.wanted_date_entries)):  
                    if self.wanted_date_entries[i]["category"]=='Operating' and self.wanted_date_entries[i]["flow_type"]=="Outflow":
                        current_row+=1 
                        self.outerLayout.addWidget(QLabel(self.wanted_date_entries[i]['entry_title']), current_row,1,1,1)
                        self.outerLayout.addWidget(QLabel(str(self.wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
                    if i == len(self.wanted_date_entries)-1:
                        self.outerLayout.addWidget(QLabel(str(self.results[1])), current_row, 4, Qt.AlignRight)
                        self.outerLayout.addWidget(QHLine(), current_row, 3,1,2, Qt.AlignBottom)
            current_row+=1
            self.outerLayout.addWidget(QLabel("Net cash from operating activities"), current_row,0,1,1)
            self.outerLayout.addWidget(QLabel(str(self.results[1])), current_row,4, Qt.AlignRight)
        #investing
        if (self.inv_in or self.inv_out)==True:
            current_row+=1
            self.outerLayout.addWidget(QLabel("<b> Cash flows from investing activities </b>"), current_row,0,1,1)
            if self.inv_in ==True: 
                current_row+=1
                self.outerLayout.addWidget(QLabel("Inflow"), current_row,0,1,1)
                for i in range(len(self.wanted_date_entries)): 
                    if self.wanted_date_entries[i]["category"]=='Investing' and self.wanted_date_entries[i]["flow_type"]=="Inflow": 
                        current_row+=1
                        self.outerLayout.addWidget(QLabel(self.wanted_date_entries[i]['entry_title']), current_row,1,1,1)
                        self.outerLayout.addWidget(QLabel(str(self.wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
                    if i == len(self.wanted_date_entries)-1:
                        self.outerLayout.addWidget(QLabel(str(self.results[3])), current_row,4, Qt.AlignRight)
                        self.outerLayout.addWidget(QHLine(), current_row, 3, Qt.AlignBottom)
            if self.inv_out==True: 
                current_row+=1
                self.outerLayout.addWidget(QLabel("Outflow"), current_row,0,1,1)
                for i in range(len(self.wanted_date_entries)): 
                    if self.wanted_date_entries[i]["category"]=='Investing' and self.wanted_date_entries[i]["flow_type"]=="Outflow": 
                        current_row+=1
                        self.outerLayout.addWidget(QLabel(self.wanted_date_entries[i]['entry_title']), current_row,1,1,1)
                        self.outerLayout.addWidget(QLabel(str(self.wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
                    if i == len(self.wanted_date_entries)-1:
                        self.outerLayout.addWidget(QLabel(str(self.results[4])), current_row,4, Qt.AlignRight)
                        self.outerLayout.addWidget(QHLine(), current_row, 3,1,2, Qt.AlignBottom)
            current_row+=1
            self.outerLayout.addWidget(QLabel("Net cash from investing activities"), current_row,0,1,1)
            self.outerLayout.addWidget(QLabel(str(self.results[5])), current_row,4, Qt.AlignRight)
        #financing
        if (self.fin_in or self.fin_out)==True:
            current_row+=1
            self.outerLayout.addWidget(QLabel("<b> Cash flows from financing activities </b>"), current_row,0,1,1)
            if self.fin_in ==True: 
                current_row+=1
                self.outerLayout.addWidget(QLabel("Inflow"), current_row,0,1,1)
                for i in range(len(self.wanted_date_entries)): 
                    if self.wanted_date_entries[i]["category"]=='Financing' and self.wanted_date_entries[i]["flow_type"]=="Inflow": 
                        current_row+=1
                        self.outerLayout.addWidget(QLabel(self.wanted_date_entries[i]['entry_title']), current_row,1,1,1)
                        self.outerLayout.addWidget(QLabel(str(self.wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
                    if i == len(self.wanted_date_entries)-1:
                        self.outerLayout.addWidget(QLabel(str(self.results[6])), current_row,4, Qt.AlignRight)
                        self.outerLayout.addWidget(QHLine(), current_row, 3, Qt.AlignBottom)
            if self.fin_out==True: 
                current_row+=1
                self.outerLayout.addWidget(QLabel("Outflow"), current_row,0,1,1)
                for i in range(len(self.wanted_date_entries)): 
                    if self.wanted_date_entries[i]["category"]=='Financing' and self.wanted_date_entries[i]["flow_type"]=="Outflow":
                        current_row+=1 
                        self.outerLayout.addWidget(QLabel(self.wanted_date_entries[i]['entry_title']), current_row,1,1,1)
                        self.outerLayout.addWidget(QLabel(str(self.wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
                    if i == len(self.wanted_date_entries)-1:
                        self.outerLayout.addWidget(QLabel(str(self.results[7])), current_row,4, Qt.AlignRight)
                        self.outerLayout.addWidget(QHLine(), current_row, 3,1,2, Qt.AlignBottom)
            current_row+=1
            self.outerLayout.addWidget(QLabel("Net cash from financing activities"), current_row,0,1,1)
            self.outerLayout.addWidget(QLabel(str(self.results[8])), current_row,4, Qt.AlignRight)

        current_row+=1
        self.outerLayout.addWidget(QLabel('Net Increase in Cash in Bank'), current_row,0,1,1)
        self.outerLayout.addWidget(QLabel(str(self.results[9])), current_row,4, Qt.AlignRight)
        current_row+=1
        self.outerLayout.addWidget(QLabel('Cash in Bank, Previous Day'), current_row,0,1,1)
        self.outerLayout.addWidget(QLabel(str(self.wanted_date_entries[0]["cash_in_bank"])), current_row,4, Qt.AlignRight)
        self.outerLayout.addWidget(QHLine(), current_row, 4, Qt.AlignBottom)
        current_row+=1
        self.outerLayout.addWidget(QLabel("Cash in Bank, Today"), current_row,0,1,1)
        self.outerLayout.addWidget(QLabel("<b> ₱ </b>"), current_row,4)
        self.outerLayout.addWidget(QLabel(str(self.results[10])), current_row,4, Qt.AlignRight)
        self.containing_widget.setLayout(self.outerLayout)
        self.outerLayout.addWidget(QHLine(), current_row, 4, Qt.AlignBottom)

        self.setWidgetResizable(True)
        self.setWidget(self.containing_widget)