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

    # Define the SQL query to update records in the Category table
    sql_query = "UPDATE Category SET category_name = %s WHERE category_id = %s"

    # Specify the new category name and category ID to update
    new_category_name = "New Category Name"
    category_id_to_update = 1  # Replace with the actual category ID you want to update

    # Execute the SQL query with the new values
    db_cursor.execute(sql_query, (new_category_name, category_id_to_update))

    # Commit the transaction
    mydb.commit()

    # Print success message
    print("Records updated successfully.")

    # Close cursor and connection
    db_cursor.close()
    mydb.close()

except Exception as e:
    print("Error:", e)
