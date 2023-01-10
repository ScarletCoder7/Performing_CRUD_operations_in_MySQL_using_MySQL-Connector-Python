import mysql.connector as connector

#The password I'm mentioning here isn't the correct one since I don't wanna disclose my password.
connection = connector.connect(user = "root", password = "incorrect") 
cursor = connection.cursor(buffered = True)

cursor.execute("""USE little_lemon5""")
sql_query = """DELETE FROM orders
WHERE 
Bill_amount IS NULL 
OR 
BookingID IS NULL;"""
cursor.execute(sql_query)
connection.commit()