name=input("Digite seu nome:")
adress=input("Digite seu endereço:")

import mysql.connector

mydb = mssql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python"
)

mycursor = mydb.cursor()

sql = "INSERT INTO clientes (name, address) VALUES (%s, %s)"
val = (name, adress)
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")