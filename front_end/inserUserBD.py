# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
try:
    conn = mariadb.connect(
        user = "user", # MARIADB_USER
        password = "user", # MARIADB_PASSWORD
        host = "127.0.0.1", # service name of the database container
        port = 7706, # MARIADB EXPOSED PORT
        database = "wsdb" # MARIADB_DATABASE

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
cur1 = conn.cursor()
cur2 = conn.cursor()

name = 'Joaquin Alarcon'
nickname = 'jalarcon'
password = 'uaouser'
comment = 'first login'

try: 
    cur.execute("INSERT INTO `user_name`(`user_id`, `user_desc`, `encrypt_pw`, `last_edit_comment`) VALUES (?,?,PASSWORD(?),?)", (name, nickname, password, comment)) 
except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
# print(f"Last Inserted ID: {cur.lastrowid}")
if cur.lastrowid:
    print(f"Welcome {nickname}")
else:
    print(f"USER ALREADY EXIST: {name} - {nickname}")

conn.close()