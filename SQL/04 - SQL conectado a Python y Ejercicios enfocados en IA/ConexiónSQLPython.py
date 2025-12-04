# Con la librerias ya instaladas comenzamos primero con la conección Python a MySQL:
import mysql.connector
import pandas as pd

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="1234",
    database="santiago_IA"
)

cursor = conexion.cursor()
cursor.execute("SELECT * FROM santiago_cultivos")

for fila in cursor.fetchall():
    print(fila)

conexion.close()
