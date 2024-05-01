import mysql.connector as MyCon

try:
    # Establish connection
    mydb = MyCon.connect(
        host="127.0.0.1",
        user="root",
        password="Sneha$29",
        database="vegetable_vendor_db"  # Change the database name
    )

    # Check if the table exists
    db_cursor = mydb.cursor()
    db_cursor.execute("SHOW TABLES")
    tables = db_cursor.fetchall()

    table_exists = False
    for table in tables:
        if 'category' in table:
            table_exists = True
            break

    # If the table doesn't exist, create it
    if not table_exists:
        # Create the table
        db_cursor.execute("""
            CREATE TABLE category (
                category_id INT AUTO_INCREMENT PRIMARY KEY,
                category_name VARCHAR(255)
            )
        """)
        print("Table 'category' Created !!")
    else:
        print("Table 'category' already exists.")

    # Close cursor and connection
    db_cursor.close()
    mydb.close()

except Exception as e:
    print("Error:", e)
