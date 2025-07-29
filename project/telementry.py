import time
import random
from datetime import datetime
import db
import alert

while(True):
    for x in db.ListVehicle():
        vid=x[0]
        lat=random.randint(-90, 90)
        long=random.randint(-180, 180)
        engine=random.randint(0,3)
        speed=0
        if(engine>1):
            speed=random.randint(1,150)
            engine="On"
        elif(engine==1):
            engine="Idle"
        else:
            engine="Off"
        

        fuel=random.randint(1,100)
        dist=random.randint(1,10000)
        diag=random.randint(0,1)
        now = datetime.now()
        date_time = now.strftime("%m/%d/%Y, %H:%M:%S")

        alert.speed_violations(80,speed)
        alert.fuel(fuel)
        db.InsertTelementary(vid, lat, long, engine, fuel, dist, diag, date_time, speed)

    time.sleep(3)

