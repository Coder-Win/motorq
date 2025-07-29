import db
from datetime import datetime

def active(val1):
    active=0
    inactive=0
    for i in db.FleetVehicle(val1):
        if(i[5]=="active"):
            active+=1
        else:
            inactive+=1
    print("active: ", active, " inactive: ",inactive)

def avgfuel(val1):
    sum=0
    count=0
    for i in db.FleetVehicleJoin(val1):
        sum+=int(i[10])
        count+=1
    print(sum/count)



def totdist(val1):
    dist=0
    for i in db.FleetVehicleJoin(val1):
        time_data = i[13]
        format_data = "%m/%d/%Y, %H:%M:%S"
        date = datetime.strptime(time_data, format_data)
        difference=datetime.now()-date
        if difference.days ==0:
            dist+=int(i[11])
    print(dist)



def alertanalysis(val1):
    count=0
    severity={"High":0, "Moderate":0, "Low":0}
    for i in db.FleetVehicleAlert(val1):
        count+=1
        severity[i[3]]+=1
    print(count)
    for i in severity:
        print(i,":",severity[i])
alertanalysis("Corporate")

