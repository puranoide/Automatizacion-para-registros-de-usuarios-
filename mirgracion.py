import mysql.connector
import pandas as pd

# Establecer la conexión a la base de datos MySQL
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="vitaemedbasededatos"
)

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Leer el archivo Excel
df_excel = pd.read_excel('basederetornos.xlsm')


for index, row in df_excel.iterrows():
    nombre = row['Nombre']
    fecha_columnas = row.index[6:]  # Obtener las columnas de fecha desde la séptima en adelante

    for fecha in fecha_columnas:
        if row[fecha] == 1:
            # Buscar el ID del miembro en la base de datos
            query = f"SELECT UUID FROM miembros WHERE nombre = '{nombre}'"
            cursor.execute(query)
            result = cursor.fetchall()  # Cambia aquí de fetchone a fetchall

            if result:
                id_miembro = result[0][0]  # Asegúrate de obtener el primer elemento del primer resultado
                # Insertar en la tabla "registros"
                query_insert = f"INSERT INTO registro (fecha, uuid_fk) VALUES ('{fecha}', {id_miembro})"
                cursor.execute(query_insert)
                conn.commit()

# Cierra el cursor y la conexión después de terminar
cursor.close()
conn.close()
