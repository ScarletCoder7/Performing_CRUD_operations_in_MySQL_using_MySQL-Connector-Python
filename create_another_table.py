import mysql.connector as connector

#The password I'm mentioning here isn't the correct one since I don't wanna disclose my password.
connection = connector.connect(user = "root", password = "incorrect") 
cursor = connection.cursor()

#Create table orders
cursor.execute("""USE little_lemon5""")
create_orders_query = """CREATE TABLE orders(BookingID INT, Bill_amount INT, TableNo VARCHAR(100))"""
cursor.execute(create_orders_query)

#Insert into table
insert_query1 = """INSERT INTO orders(BookingID, Bill_amount, TableNo) VALUES(0012, 50, "4")"""
cursor.execute(insert_query1)
connection.commit()

insert_query2 = """INSERT INTO orders(BookingID, Bill_amount, TableNo) VALUES(0032, 32, "5")"""
cursor.execute(insert_query2)
connection.commit()

insert_query3 = """INSERT INTO orders(BookingID, Bill_amount, TableNo) VALUES(0011, 10, "10")"""
cursor.execute(insert_query3)
connection.commit()

insert_query4 = """INSERT INTO orders(BookingID, Bill_amount, TableNo) VALUES(0022, 40, "1")"""
cursor.execute(insert_query4)
connection.commit()

#Filtering and Sorting
filtering_sorting_query = """SELECT BookingID, Bill_amount FROM orders WHERE Bill_amount >= 40 ORDER BY Bill_amount DESC"""
cursor.execute(filtering_sorting_query)
results = cursor.fetchall()
print(*results)

#Inner Join
join_query = """SELECT bookings.GuestFirstName, bookings.GuestLastName, bookings.employeeID, orders.BookingID FROM bookings INNER JOIN orders ON bookings.TableNo = orders.TableNo"""
cursor.execute(join_query)
results = cursor.fetchall()
for i in results:
    print(*i)


#Insert
insert_query5 = """INSERT INTO orders(BookingID, TableNo) VALUES(0062, "62")"""
cursor.execute(insert_query5)
connection.commit()

insert_query6 = """INSERT INTO orders(Bill_amount, TableNo) VALUES(80, "72")"""
cursor.execute(insert_query6)
connection.commit()
