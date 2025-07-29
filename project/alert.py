import db
from datetime import datetime

def speed_violations(fetch,val1):
    if(fetch<val1):
        severity="Low"
        if(val1-fetch>20):
            severity="High"
        elif(val1-fetch>10):
            severity="Moderate"       
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        db.AlertInsert(val1,"speed",date_time,severity)
        print("SPEED EXCEEDS SPEED LIMIT")

def fuel(val1):
    if(val1<15):
        severity="Low"
        if(val1<5):
            severity="High"
        elif(val1<10):
            severity="Moderate"    
        
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
        db.AlertInsert(val1,"speed",date_time,severity)
        print("FUEL IS BELOW 15%")




    
