import pyodbc

def make_connection():
    SERVER = 'LAPTOP-OP54VOF0'
    DATABASE = 'Hotel Reservation System'
    CONNECTION_STRING = f'DRIVER={{SQL Server}};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes'
    DRIVER = 'SQL Server'

    try:
        conn = pyodbc.connect(f'DRIVER={DRIVER};SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;')
        conn.autocommit = True
        print("Connection successful!")
        cursor = conn.cursor()
        return cursor
    except Exception as e:
        print(f"Error: {e}")
