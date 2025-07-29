import mysql.connector

def InsertVehicle(val1,val2,val3,val4,val5,val6):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="motorq"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO vehicles (vin, manufacturer, model, fleetid, owner, registration) VALUES (%s, %s, %s, %s, %s, %s)"

    val=(val1,val2,val3,val4,val5,val6)

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")


def ListVehicle():
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="motorq"
    )

    mycursor = mydb.cursor()

    mycursor.execute("SELECT * FROM vehicles")

    myresult = mycursor.fetchall()

    return myresult

def FleetVehicle(val1):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="motorq"
    )

    mycursor = mydb.cursor()

    sql="SELECT * FROM vehicles WHERE fleetid = %s"
    val=(val1,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    return myresult

def DeleteVehicle(val1):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="motorq"
    )

    mycursor = mydb.cursor()

    sql = "DELETE FROM vehicles WHERE vin = %s"
    val=(val1,)
    mycursor.execute(sql, val)
    mydb.commit()

def UpdateVehicle(val1,val2):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="motorq"
    )

    mycursor = mydb.cursor()

    
    sql = "UPDATE vehicles SET registration = %s WHERE VIN = %s"
    val = (val1, val2)

    mycursor.execute(sql, val)
    mydb.commit()

def InsertTelementary(val1,val2,val3,val4,val5,val6,val7,val8,val9):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="motorq"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO telementary(vid, lat, longitude, engine, fuel, dist, err, timestamp, speed) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

    val=(str(val1),str(val2),str(val3),str(val4),str(val5),str(val6),str(val7),str(val8),str(val9))

    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")

def FleetVehicleJoin(val1):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="motorq"
    )

    mycursor = mydb.cursor()

    sql="SELECT * FROM vehicles NATURAL JOIN telementary WHERE fleetid = %s"
    val=(val1,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    return myresult

def FleetVehicleAlert(val1):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="motorq"
    )

    mycursor = mydb.cursor()

    sql="SELECT * FROM alerts NATURAL JOIN vehicles WHERE fleetid = %s"
    val=(val1,)
    mycursor.execute(sql, val)
    myresult = mycursor.fetchall()

    return myresult

def AlertInsert(val1,val2,val3,val4):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql",
    database="motorq"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO alerts (vid, type, timestamp, severity) VALUES (%s, %s, %s, %s)"

    val=(val1,val2,val3,val4)
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record inserted.")