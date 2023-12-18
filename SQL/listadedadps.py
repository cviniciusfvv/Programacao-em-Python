import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="",
    database="db_python"
)

mycursor = mydb.cursor()

query = "SELECT * FROM clientes"
mycursor.execute(query)
result = mycursor.fetchall()
for row in result:
    print (f"Cliente: {row}")