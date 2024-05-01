import mysql.connector as MyCon

try:
    # Establish connection to the vegetable_vendor_db database
    mydb = MyCon.connect(
        host="127.0.0.1",
        user="root",
        password="Sneha$29",
        database="vegetable_vendor_db"
    )

    # Create a cursor object
    db_cursor = mydb.cursor()

    # Define the SQL query to truncate the Category table
    sql_query = "TRUNCATE TABLE Category"

    # Execute the SQL query to truncate the Category table
    db_cursor.execute(sql_query)

    # Commit the transaction
    mydb.commit()

    # Print success message
    print("Table 'Category' truncated successfully.")

    # Close cursor and connection
    db_cursor.close()
    mydb.close()

except Exception as e:
    print("Error:", e)
