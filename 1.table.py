import mysql.connector as MyCon

try:
    # Establish connection
    mydb = MyCon.connect(
        host="127.0.0.1",
        user="root",
        password="Sneha$29",
        database="Vendorvegetable"  # Specify the database
    )

    # Get the cursor
    db_cursor = mydb.cursor()

    # Execute SQL query to show tables
    db_cursor.execute("SHOW TABLES")

    # Fetch all table names
    tables = db_cursor.fetchall()

    # Print table names
    print("Tables in database 'Vendorvegetable':")
    for table in tables:
        print(table[0])

    # Close cursor and connection
    db_cursor.close()
    mydb.close()
except Exception as e:
    print("Error:", e)
