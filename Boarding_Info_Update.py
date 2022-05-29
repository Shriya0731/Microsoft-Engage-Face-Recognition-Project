import mysql.connector

# connecting python to mysql datbase
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="priyanka2240",
    database="Passenger_Info"
  )

# when passenger is verified following function is called to mark the status of passenger as boarded
def boarding(passenger_name):
  global mydb
  mycursor = mydb.cursor()

  sql = "UPDATE Passengers SET Boarding_time = CURRENT_TIMESTAMP, Status = %s WHERE Name = %s"
  val = ('Boarded',passenger_name)

  mycursor.execute(sql,val)

  mydb.commit()

# when passenger is verified following function is called to get passport number of passenger
def get_passportno(passenger_name):
  global mydb
  mycursor = mydb.cursor()
  sql = "SELECT Passportno from Passengers WHERE Name = %s"
  val = (passenger_name,)
  mycursor.execute(sql, val)
  return mycursor.fetchone()[0]

# when passenger books a flight , this function is called to add data in database
def add_new_booking(passenger_name,passportno,date,flight):
  global mydb
  mycursor = mydb.cursor()

  sql = "INSERT INTO Passengers (Name, Passportno, Status, Flightdate, Flightno) values (%s,%s,'Not Boarded',%s,%s);"
  val = (passenger_name,passportno,date,flight)

  mycursor.execute(sql, val)

  mydb.commit()
