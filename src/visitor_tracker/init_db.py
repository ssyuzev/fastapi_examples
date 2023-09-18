import os
import psycopg2
from dotenv import load_dotenv


load_dotenv()
DB_USER = os.getenv("POSTGRES_USER")
DB_PAASWORD = os.getenv("POSTGRES_PASSWORD")
DB_SERVER = os.getenv("DATABASE_SERVER")
DB_PORT = os.getenv("DATABASE_PORT")
DB_NAME = os.getenv("DATABASE_NAME")


def get_db_connection():
    return psycopg2.connect(f"postgresql://{DB_USER}:{DB_PAASWORD}@{DB_SERVER}:{DB_PORT}/{DB_NAME}")


conn = get_db_connection()
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS logs;")
cur.execute(
    'CREATE TABLE logs (id serial PRIMARY KEY,'
    'ip_address varchar (150) NOT NULL,'
    'request_url varchar (50) NOT NULL,'
    'request_port integer NOT NULL,'
    'request_path varchar (50) NOT NULL,'
    'request_method varchar (50) NOT NULL,'
    'browser_type varchar (150) NOT NULL,'
    'request_time timestamp (50) NOT NULL,'
    'service_name varchar (150) NOT NULL,'
    'date_added date DEFAULT CURRENT_TIMESTAMP);'
)

cur.execute(
    'INSERT INTO logs (ip_address,'
    'request_url,'
    'request_port,'
    'request_path,'
    'request_method,'
    'browser_type,'
    'request_time,'
    'service_name)'
    'VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
    ('127.0.0.1', 'http://localhost:8000', 8000, "/", "GET", "Chrome", "2023-06-25T16:03:24.722256", "Test_data_service")
)

conn.commit()
cur.close()
conn.close()
