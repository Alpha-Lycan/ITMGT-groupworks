
from turtle import position
from pymongo import MongoClient
scp_dictlist=[]

#mongodb connection thingy: mongodb+srv://Alpha_Lycan:<password>@cluster0.2tif2nh.mongodb.net/test


entry_title=""
date=""
amount_cib=0
flow_type=""
category=""

# for i in range(2):
#     entry_title=input("Name of the activity:")
#     date=input("Date:")
#     amount=int(input("amount of cash used in the activity:"))
#     flow_type=input("Inflow or outflow checkboxes:")
#     category=input("Operating, Investing, or Financing checkboxes:") 
#     scp_dictlist.append({"Entry Title":entry_title, "Date":date, "amount":int(amount_cib),"Inflow or Outflow":flow_type,"category":category})

#cib=cash in bank from previous day
#return the scp 

def add_entry():
    client=MongoClient("mongodb+srv://Alpha_Lycan:Charing@cluster0.2tif2nh.mongodb.net/test")
    db=client["scp_database"]
    mycol=db["daily_cash_position"]
    mydict = {"entry_title":"bank investment","date":"","amount":100,"flow_type":"Outflow","category":"Investing"}
    added_entry=mycol.insert_one(mydict)
    #filter by title 
    #filter is the first paremater and the second parameter is the return. 0 means u dont return it, 1 means u return it.
    # for entry in entry_list:
add_entry()

def update_entry():
    client=MongoClient("mongodb+srv://Alpha_Lycan:Charing@cluster0.2tif2nh.mongodb.net/test")
    db=client["scp_database"]
    mycol=db["daily_cash_position"]
    myquery = { "entry_title": "food" }
    newvalues = { "$set": { "flow_type": "Inflow" } }
    mycol.update_one(myquery, newvalues) 
    
update_entry()   

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
    #cash in bank computation
    net_in_cib=0
    cib_today=0

    for entry in scp_dictlist:
        if entry["category"]=="Operating":
            if entry["flow_type"]=="Inflow":
                op_in+=entry["amount"]
            else:
                op_out+=entry["amount"]
        elif entry["category"]=="Investing":
            if entry["flow_type"]=="Inflow":
                inv_in+=entry["amount"]
            else:
                inv_out+=entry["amount"]
        elif entry["category"]=="Financing":
            if entry["flow_type"]=="Inflow":
                fin_in+=entry["amount"]
            else:
                fin_out+=entry["amount"]
    net_op=op_in-op_out
    net_inv=inv_in-inv_out
    net_fin=fin_in-fin_out
    net_in_cib=net_op+net_inv+net_fin
    cib_today=cib_prevday+net_in_cib
    return(op_in,op_out,net_op,inv_in,inv_out,net_inv,fin_in,fin_out,net_fin,net_in_cib,cib_today)

#delete query

def delete_entry():
    client=MongoClient("mongodb+srv://Alpha_Lycan:Charing@cluster0.2tif2nh.mongodb.net/test")
    db=client["scp_database"]
    mycol=db["daily_cash_position"]
    myquery = { "entry_title": "bank investment" }
    mycol.delete_one(myquery)
delete_entry()


def get_entry():
    client=MongoClient("mongodb+srv://Alpha_Lycan:Charing@cluster0.2tif2nh.mongodb.net/test")
    db=client["scp_database"]
    mycol=db["daily_cash_position"]
    entry_list=mycol.find({},{"_id":0,"entry_title":1,"date":1,"amount":1,"flow_type":1,"category":1,})
    #filter by title 
    #filter is the first paremater and the second parameter is the return. 0 means u dont return it, 1 means u return it.
    # for entry in entry_list:
    return(entry_list)
scp_dictlist=get_entry()

res=compute_values(scp_dictlist,83275)
print(res)


