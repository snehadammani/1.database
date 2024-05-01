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

    # Execute SQL query to check for a specific table name
    db_cursor.execute("SHOW TABLES LIKE 'category'")

    # Fetch the result
    result = db_cursor.fetchone()

    if result:
        print("Table 'category' exists in database 'Vendorvegetable'")
    else:
        print("Table 'category' does not exist in database 'Vendorvegetable'")

    # Close cursor and connection
    db_cursor.close()
    mydb.close()
except Exception as e:
    print("Error:", e)
