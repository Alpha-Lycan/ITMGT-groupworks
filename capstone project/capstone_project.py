
from pymongo import MongoClient

#cib=cash in bank from previous day
#return the scp 

# get data from db
# parameters:
    # query - dictionary containing key-value pairs used for filtering data from db; can contain only 1 field at least
# filter/query options: by title or by date since same-date entries will be grouped together
def get_entries(query):
    client=MongoClient("mongodb+srv://Alpha_Lycan:Charing@cluster0.2tif2nh.mongodb.net/test")
    db=client["scp_database"]
    mycol=db["daily_cash_position"]

    #find() function: filter is the first paremater and the second parameter is the return. 0 means u dont return it, 1 means u return it.    
    entry_list=mycol.find(query,{"_id":0,"entry_title":1,"date":1,"amount":1,"flow_type":1,"category":1,"cash_in_bank":1})
    return(list(entry_list))

# add data from db
# parameters: 
    # entry_title, flow_type, category - string
    # date - date type
    # amount - integer
def add_entry(my_new_entry):
    client=MongoClient("mongodb+srv://Alpha_Lycan:Charing@cluster0.2tif2nh.mongodb.net/test")
    db=client["scp_database"]
    mycol=db["daily_cash_position"]
    
    # adding single entry to db
    # my_new_entry = {"entry_title":entry_title, "date":date, "amount":amount, "flow_type":flow_type, "category":category}
    mycol.insert_one(my_new_entry)
    
# update data from db
# parameters:
    # query - dictionary containing key-value pairs used for filtering data from db; can contain only 1 field at least
    # updated_fields - dictionary containing all the key-value pairs of an entry with the updated values
def update_entry(query, updated_fields):
    client=MongoClient("mongodb+srv://Alpha_Lycan:Charing@cluster0.2tif2nh.mongodb.net/test")
    db=client["scp_database"]
    mycol=db["daily_cash_position"]
    
    # updating current values to new values
    newvalues = {"$set":updated_fields}
    mycol.update_one(query, newvalues)
      
# delete data from db
# parameters:
    # query - dictionary containing key-value pairs used for filtering data from db; can contain only 1 field at least
def delete_entry(query):
    client=MongoClient("mongodb+srv://Alpha_Lycan:Charing@cluster0.2tif2nh.mongodb.net/test")
    db=client["scp_database"]
    mycol=db["daily_cash_position"]

    # delete an entry depending on query
    mycol.delete_one(query)

# computation of values for the SCP
# parameters:
    # scp_dictlist - list of entries (output of get_entries request) for a specific date
    # cib_prevday - integer
def compute_values(scp_dictlist, cib_prevday):
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

scp_dictlist=get_entries({"entry_title":"bank investment"})

scp_values=compute_values(scp_dictlist,83275)
