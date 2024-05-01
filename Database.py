import mysql.connector as MyCon

try:
    # Establish connection
    mydb = MyCon.connect(
        host="127.0.0.1",
        user="root",
        password="Sneha$29"
    )
    
    # Check if the database exists
    db_cursor = mydb.cursor()
    db_cursor.execute("SHOW DATABASES")
    databases = db_cursor.fetchall()
    
    database_exists = False
    for db in databases:
        if 'vegetable_vendor_db' in db:
            database_exists = True
            break
    
    # If the database doesn't exist, create it
    if not database_exists:
        db_cursor.execute("CREATE DATABASE vegetable_vendor_db")
        print("Database 'vegetable_vendor_db' Created !!")
    else:
        print("Database 'vegetable_vendor_db' already exists.")
    
    # Close cursor and connection
    db_cursor.close()
    mydb.close()

except Exception as e:
    print("Error:", e)

