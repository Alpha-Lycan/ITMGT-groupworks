# Filename: f_layout.py

"""Form layout example."""

import sys

from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QFrame
from capstone_project import *

#Horizontal line
class QHLine(QFrame):
    def __init__(self):
        super(QHLine, self).__init__()
        self.setFrameShape(QFrame.HLine)

#compute_values(scp_dictlist, cib_prevday)
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Statement of Cash Position')
layout = QGridLayout()
wanted_date='7/18/22'
wanted_date_entries=get_entries({"date":wanted_date})
res=compute_values(wanted_date_entries,wanted_date_entries[0]["cash_in_bank"])

#operating
op_in=False  
op_out=False 
net_op=op_in or op_out 
#investing
inv_in=False 
inv_out=False 
net_inv=inv_in or inv_out
#financing
fin_in=False 
fin_out=False 
net_fin=fin_in or fin_out 

for entry in wanted_date_entries: 
    if entry["category"]=="Operating":
        if entry["flow_type"]=="Inflow":
            op_in=True
        else:
            op_out=True
    elif entry["category"]=="Investing":
        if entry["flow_type"]=="Inflow":
            inv_in=True
        else:
            inv_out=True
    elif entry["category"]=="Financing":
        if entry["flow_type"]=="Inflow":
            fin_in=True
        else:
            fin_out=True 

current_row=0
def next_row(current_row,increment):
    current_row+=increment
    return(current_row)

current_row=0

layout.addWidget(QLabel('<b>Statement of Cash Position</b>'), current_row,0,1,4, Qt.AlignCenter)
current_row=next_row(current_row,2)
layout.addWidget(QLabel("<b>"+wanted_date+"</b>"), current_row,0,1,4, Qt.AlignCenter)

if (op_in or op_out) == True:
    current_row=next_row(current_row,1)
    layout.addWidget(QLabel("<b> Cash flows from operating activities</b>"),current_row,0,1,2)
    if op_in ==True: 
        current_row=next_row(current_row,1)
        layout.addWidget(QLabel("Inflow"), current_row,0,1,2)
        for i in range(len(wanted_date_entries)): 
            if wanted_date_entries[i]["category"]=='Operating' and wanted_date_entries[i]["flow_type"]=="Inflow": 
                current_row=next_row(current_row,1)
                layout.addWidget(QLabel(wanted_date_entries[i]['entry_title']), current_row,1,1,2)
                layout.addWidget(QLabel(str(wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
            if i == len(wanted_date_entries)-1:
                layout.addWidget(QLabel(str(res[0])), current_row,4, Qt.AlignRight)
                layout.addWidget(QHLine(), current_row,3, Qt.AlignBottom)
    if op_out==True: 
        current_row=next_row(current_row,1)
        layout.addWidget(QLabel("Outflow"), current_row,0,1,2)
        for i in range(len(wanted_date_entries)):  
            if wanted_date_entries[i]["category"]=='Operating' and wanted_date_entries[i]["flow_type"]=="Outflow":
                current_row=next_row(current_row,1) 
                layout.addWidget(QLabel(wanted_date_entries[i]['entry_title']), current_row,1,1,2)
                layout.addWidget(QLabel(str(wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
            if i == len(wanted_date_entries)-1:
                layout.addWidget(QLabel(str(res[1])), current_row,4, Qt.AlignRight)
                layout.addWidget(QHLine(), current_row, 3,1,2, Qt.AlignBottom)
    current_row=next_row(current_row,1)
    layout.addWidget(QLabel("Net cash from operating activities"), current_row,0,1,2)
    layout.addWidget(QLabel(str(res[2])), current_row,4, Qt.AlignRight)
if (inv_in or inv_out)==True:
    current_row=next_row(current_row,1)
    layout.addWidget(QLabel("<b> Cash flows from investing activities </b>"), current_row,0,1,2)
    if inv_in ==True: 
        current_row=next_row(current_row,1)
        layout.addWidget(QLabel("Inflow"), current_row,0,1,2)
        for i in range(len(wanted_date_entries)): 
            if wanted_date_entries[i]["category"]=='Investing' and wanted_date_entries[i]["flow_type"]=="Inflow": 
                current_row=next_row(current_row,1)
                layout.addWidget(QLabel(wanted_date_entries[i]['entry_title']), current_row,1,1,2)
                layout.addWidget(QLabel(str(wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
            if i == len(wanted_date_entries)-1:
                layout.addWidget(QLabel(str(res[3])), current_row,4, Qt.AlignRight)
                layout.addWidget(QHLine(), current_row,3, Qt.AlignBottom)
    if inv_out==True: 
        current_row=next_row(current_row,1)
        layout.addWidget(QLabel("Outflow"), current_row,0,1,2)
        for i in range(len(wanted_date_entries)): 
            if wanted_date_entries[i]["category"]=='Investing' and wanted_date_entries[i]["flow_type"]=="Outflow": 
                current_row=next_row(current_row,1)
                layout.addWidget(QLabel(wanted_date_entries[i]['entry_title']), current_row,1,1,2)
                layout.addWidget(QLabel(str(wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
            if i == len(wanted_date_entries)-1:
                layout.addWidget(QLabel(str(res[4])), current_row,4, Qt.AlignRight)
                layout.addWidget(QHLine(), current_row, 3,1,2, Qt.AlignBottom)
    current_row=next_row(current_row,1)
    layout.addWidget(QLabel("Net cash from investing activities"), current_row,0,1,2)
    layout.addWidget(QLabel(str(res[5])), current_row,4, Qt.AlignRight)
#financing
if (fin_in or fin_out)==True:
    current_row=next_row(current_row,1)
    layout.addWidget(QLabel("<b> Cash flows from financing activities </b>"), current_row,0,1,2)
    if fin_in ==True: 
        current_row=next_row(current_row,1)
        layout.addWidget(QLabel("Inflow"), current_row,0,1,2)
        for i in range(len(wanted_date_entries)): 
            if wanted_date_entries[i]["category"]=='Financing' and wanted_date_entries[i]["flow_type"]=="Inflow": 
                current_row=next_row(current_row,1)
                layout.addWidget(QLabel(wanted_date_entries[i]['entry_title']), current_row,1,1,2)
                layout.addWidget(QLabel(str(wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
            if i == len(wanted_date_entries)-1:
                layout.addWidget(QLabel(str(res[6])), current_row,4, Qt.AlignRight)
                layout.addWidget(QHLine(), current_row,3, Qt.AlignBottom)
    if fin_out==True: 
        current_row=next_row(current_row,1)
        layout.addWidget(QLabel("Outflow"), current_row,0,1,2)
        for i in range(len(wanted_date_entries)): 
            if wanted_date_entries[i]["category"]=='Financing' and wanted_date_entries[i]["flow_type"]=="Outflow":
                current_row=next_row(current_row,1) 
                layout.addWidget(QLabel(wanted_date_entries[i]['entry_title']), current_row,1,1,2)
                layout.addWidget(QLabel(str(wanted_date_entries[i]['amount'])), current_row,3, Qt.AlignRight)
            if i == len(wanted_date_entries)-1:
                layout.addWidget(QLabel(str(res[7])), current_row,4, Qt.AlignRight)
                layout.addWidget(QHLine(), current_row, 3,1,2, Qt.AlignBottom)
    current_row=next_row(current_row,1)
    layout.addWidget(QLabel("Net cash from financing activities"), current_row,0,1,2)
    layout.addWidget(QLabel(str(res[8])), current_row,4, Qt.AlignRight)

current_row=next_row(current_row,1)
layout.addWidget(QLabel('Net Increase in Cash in Bank'), current_row,0,1,2)
layout.addWidget(QLabel(str(res[9])), current_row,4, Qt.AlignRight)
current_row=next_row(current_row,1)
layout.addWidget(QLabel('Cash in Bank, Previous Day'), current_row,0,1,2)
layout.addWidget(QLabel(str(wanted_date_entries[0]["cash_in_bank"])), current_row,4, Qt.AlignRight)
layout.addWidget(QHLine(), current_row, 4, Qt.AlignBottom)
current_row=next_row(current_row,1)
layout.addWidget(QLabel('Cash in Bank, Today'), current_row,0,1,2)
layout.addWidget(QLabel("<b>₱</b>"), current_row,4)
layout.addWidget(QLabel(str(res[10])), current_row,4, Qt.AlignRight)
layout.addWidget(QHLine(), current_row, 4, Qt.AlignBottom)


# layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
# layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
# layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
# layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
# layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
# layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
# layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)

window.setLayout(layout)
window.show()
sys.exit(app.exec_())