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

#retrieving information 
some_name = '%' 
cur.execute("SELECT user_id, user_desc FROM user_name WHERE user_id like (?)", (some_name,)) 

for user_id, user_desc in cur: 
    print(f"User name: {user_id}, nickname: {user_desc}")

#retrieving confirmation of exist user
some_name = 'joaquin1'
#some_name = 'joaquin1'
cur.execute("Select count(row_id) as qty from user_name where user_id = ?", (some_name,))   

for qty in cur: 
    print(f"The user name: {some_name}, is active?: {qty}")

   
#insert information (for use getout triple quotes of paragraph complete )
"""
name = 'Alma Maria Silva de Alegria'
nickname = 'ASilva'
password = 'uaouser'
comment = 'first login'

try: 
    cur.execute("INSERT INTO `user_name`(`user_id`, `user_desc`, `encrypt_pw`, `last_edit_comment`) VALUES (?,?,PASSWORD(?),?)", (name, nickname, password, comment)) 
except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")
"""
"""
url = 'www.pornhub.com'
cat1 = 'Adult'
cat2 = 'Education'
cat3 = 'Commercial'
cat4 = 'Sports'
cat5 = 'Entertainment'
comment = 'Test'
name = 'Alma Maria Silva de Alegria'

try: 
    cur.execute("INSERT INTO `result`(`url_data`, `cat1`, `cat2`, `cat3`, `cat4`, `cat5`,`lat-edit_comment`, `user_id`) VALUES (?,?,?,?,?,?,?,?)", (url, cat1, cat2, cat3, cat4, cat5, comment, name)) 
except mariadb.Error as e: 
    print(f"Error: {e}")

conn.commit() 
print(f"Last Inserted ID: {cur.lastrowid}")

"""

conn.close()