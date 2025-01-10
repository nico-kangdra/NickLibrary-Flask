import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

def db_connection():
    conn = pymysql.connect(
        host=os.getenv('DB_HOST'),
        db=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    return conn