import pymysql
from dotenv import load_dotenv
import os

load_dotenv()

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
db = os.getenv("db")

try:
    connection = pymysql.connect(
        host=host,
        user=user,
        password=password,
        db=db,

    )
    print("Connection successful!")
    connection.close()
except Exception as e:
    print("Connection failed:", e)