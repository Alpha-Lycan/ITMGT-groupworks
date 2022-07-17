# Filename: f_layout.py

"""Form layout example."""

import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QFormLayout
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QGridLayout
from capstone_project import *

#compute_values(scp_dictlist, cib_prevday)

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle('Statement of Cash Position')
layout = QGridLayout()
wanted_date='07/17/2022'
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
layout.addWidget(QLabel('<b>Statement of Cash Position</b>'), 0,0,1,4)
layout.addWidget(QLabel("<b>"+wanted_date+"</b>"), 2,0,1,4)

#if net_op==True:
layout.addWidget(QLabel("<b> Cash flows from operating activities</b>"), 3,0,1,2)
#if net_inv==True:
layout.addWidget(QLabel("<b> Cash flows from investing activities </b>"), 5,0,1,2)
#if net_fin==True:
layout.addWidget(QLabel("<b> Cash flows from financing activities </b>"), 7,0,1,2)


# layout.addWidget(QPushButton('Button (0, 1)'), 0, 1)
# layout.addWidget(QPushButton('Button (0, 2)'), 0, 2)
# layout.addWidget(QPushButton('Button (1, 0)'), 1, 0)
# layout.addWidget(QPushButton('Button (1, 1)'), 1, 1)
# layout.addWidget(QPushButton('Button (1, 2)'), 1, 2)
# layout.addWidget(QPushButton('Button (2, 0)'), 2, 0)
# layout.addWidget(QPushButton('Button (2, 1) + 2 Columns Span'), 2, 1, 1, 2)
print(wanted_date_entries)
print(res)
window.setLayout(layout)
window.show()
sys.exit(app.exec_())