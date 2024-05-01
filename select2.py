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

    # Define the SQL query to select records from the Supplier table
    sql_query = "SELECT * FROM Supplier"

    # Execute the SQL query
    db_cursor.execute(sql_query)

    # Fetch all records
    records = db_cursor.fetchall()

    # Print the records
    for record in records:
        print(record)

    # Close cursor and connection
    db_cursor.close()
    mydb.close()

except Exception as e:
    print("Error:", e)

# Mentioning the Supplier table from the given entity and attribute list
# Supplier table:
# - supplier_id (Primary Key)
# - supplier_name
# - supplier_ph
# - email
