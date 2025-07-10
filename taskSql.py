import os
import sys
import mysql.connector

# Try to load .env manually 
if os.path.exists(".env"):
    with open(".env") as f:
        for line in f:
            if line.strip() and not line.startswith('#'):
                key, sep, value = line.strip().partition("=")
                if sep:
                    os.environ.setdefault(key, value)

def get_connection():
    host = os.getenv("DB_HOST", "localhost")
    port = int(os.getenv("DB_PORT", 3306))
    database = os.getenv("DB_NAME", "task_manager")
    user = os.getenv("DB_USER", "root")
    password = os.getenv("DB_PASSWORD", "root")

    try:
        return mysql.connector.connect(
            host=host,
            port=port,
            database=database,
            user=user,
            password=password
        )
    except mysql.connector.Error as e:
        print("Database connection failed: ", e)
        sys.exit(1)  # Exit the program with a failure code
