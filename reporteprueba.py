import pandas as pd
import mysql.connector
from sqlalchemy import create_engine

# Configura la conexión a MySQL
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '',
    'database': 'vitaemedbasededatos'
}

# Ruta al archivo Excel
excel_file_path = 'data_en_excel.xlsx'

# Lee los datos desde la fila 2 en el archivo Excel
df = pd.read_excel(excel_file_path)
# Reemplaza espacios y paréntesis en los nombres de las columnas
df.columns = df.columns.str.replace(r'\s+|\(|\)', '_', regex=True)
# Convierte los tipos de datos a objetos SQLAlchemy
engine = create_engine(f"mysql+mysqlconnector://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}")

# Guarda los datos en la base de datos MySQL
df.to_sql(name='miembrosdesdeexcel', con=engine, if_exists='replace', index=False)
