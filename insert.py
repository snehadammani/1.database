import mysql.connector as MyCon

try:
    # Establish connection to the vegetable_vendor_db database
    mydb = MyCon.connect(
        host="127.0.0.1",
        user="root",
        password="Sneha$29",
        database="vegetable_vendor_db"
    )

    # Print success message
    print("Connection to vegetable_vendor_db database established successfully.")

    # Close connection
    mydb.close()

except Exception as e:
    print("Error:", e)
