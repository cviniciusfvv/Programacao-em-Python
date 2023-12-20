name = input("Digite seu nome:")
address = input("Digite seu endereço:")

import mysql.connector as mydb

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_python"
);

mycursor = mydb.cursor()

sql = "INSERT INTO clientes (name, address) VALUES (%s, %s)"
val = (name, address)  # Fixing the typo in the variable name
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")