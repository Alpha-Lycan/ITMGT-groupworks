
import pandas as pd
import numpy as np
scp_dictlist=[]

entry_title=""
date=""
amount=0
flow_type=""
category=""

for i in range(2):
    entry_title=input("Name of the activity:")
    date=input("Date:")
    amount=int(input("amount of cash used in the activity:"))
    flow_type=input("Inflow or outflow checkboxes:")
    category=input("Operating, Investing, or Financing checkboxes:") 
    scp_dictlist.append({"Entry Title":entry_title, "Date":date, "Amount of Cash":int(amount),"Inflow or Outflow":flow_type,"Category":category})

#cib=cash in bank from previous day
#return the scp 

def compute_values(scp_dictlist,cib_prevday):
    #operating
    op_in=0
    op_out=0
    net_op=0
    #investing
    inv_in=0
    inv_out=0
    net_inv=0
    #financing
    fin_in=0
    fin_out=0
    net_fin=0
    #cib computation
    net_in_cib=0
    cib_today=0

    for entry in scp_dictlist:
        if entry["Category"]=="Operating":
            if flow_type=="Inflow":
                op_in+=entry["Amount of Cash"]
            else:
                op_out+=entry["Amount of Cash"]
        elif entry["Category"]=="Investing":
            if flow_type=="Inflow":
                inv_in+=entry["Amount of Cash"]
            else:
                inv_out+=entry["Amount of Cash"]
        elif entry["Category"]=="Financing":
            if flow_type=="Inflow":
                fin_in+=entry["Amount of Cash"]
            else:
                fin_out+=entry["Amount of Cash"]
    net_op=op_in-op_out
    net_inv=inv_in-inv_out
    net_fin=fin_in-fin_out
    net_in_cib=net_op+net_inv+net_fin
    cib_today=cib_prevday+net_in_cib
    return(op_in,op_out,net_op,inv_in,inv_out,net_inv,fin_in,fin_out,net_fin,net_in_cib,cib_today)

res=compute_values(scp_dictlist,83275)
print(res)




