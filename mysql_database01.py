#CRUD operations

import mysql.connector as connector


#The password I'm mentioning here isn't the correct one since I don't wanna disclose my password.
connection = connector.connect(user = "root", password = "incorrect") 

cursor = connection.cursor()

#Create a database
create_database_query = """CREATE DATABASE little_lemon5"""
cursor.execute(create_database_query)

#create a table
use_database_query = """USE little_lemon5"""
cursor.execute(use_database_query)
create_bookings_table = """CREATE TABLE bookings(GuestFirstName VARCHAR(200), GuestLastName VARCHAR(200), TableNo VARCHAR(100), BookingSlot VARCHAR(100), EmployeeID INT, PRIMARY KEY(EmployeeID))"""
cursor.execute(create_bookings_table)

#Insert into table
mysql_insert_query = """INSERT INTO bookings(GuestFirstName, GuestLastName, TableNo, BookingSlot, EmployeeID) VALUES("Marcos", "LLorente", "2", "19:00", 5)"""
cursor.execute(mysql_insert_query)
connection.commit()

mysql_insert_query2 = """INSERT INTO bookings(GuestFirstName, GuestLastName, TableNo, BookingSlot, EmployeeID) VALUES("Tomiyu", "Nakamoto", "3", "19:15", 1)"""
cursor.execute(mysql_insert_query2)
connection.commit()

mysql_insert_query3 = """INSERT INTO bookings(GuestFirstName, GuestLastName, TableNo, bookingSlot, EmployeeID) VALUES("Sakura", "Nakamura", "1", "15:10", 2)"""
cursor.execute(mysql_insert_query3)
connection.commit()

mysql_insert_query4 = """INSERT INTO bookings(GuestFirstName, GuestLastName, TableNo, bookingSlot, EmployeeID) VALUES("Hiroshi", "Uzumaki", "4", "15:30", 3)"""
cursor.execute(mysql_insert_query4)
connection.commit()

mysql_insert_query5 = """INSERT INTO bookings(GuestFirstName, GuestLastName, TableNo, bookingSlot, EmployeeID) VALUES("Tamure", "Nakagawa", "5", "15:15", 4)"""
cursor.execute(mysql_insert_query5)
connection.commit()

#Fetch
read_data_query = """SELECT * FROM bookings"""
cursor.execute(read_data_query)
print(cursor.fetchall())

print(cursor.column_names)


first_name = ""
last_name = ""
table_no = ""
booking_slot = ""
employee_id = 0
read_data_query = """SELECT * FROM bookings"""
cursor.execute(read_data_query)
results = cursor.fetchall()
for result in results:
    first_name, last_name, table_no, booking_slot, employee_id = result
    print("Name: {} {}, Table: {}, Slot: {}, ID: {}".format(first_name, last_name, table_no, booking_slot, employee_id))


#Update
update_bookings = """UPDATE bookings SET TableNo = '10' WHERE EmployeeID = 5"""
cursor.execute(update_bookings)
connection.commit()

#Delete
delete_bookings = """DELETE FROM bookings WHERE EmployeeID = 1"""
cursor.execute(delete_bookings)
connection.commit()

#Fetch
cursor.execute("""SELECT * FROM bookings""")
result = cursor.fetchall()
for i in result:
    print(*i)

cursor.execute("""SELECT * FROM bookings""")
print(cursor.fetchmany(size = 1))





