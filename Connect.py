import mysql.connector as MyCon
try:
    # Establish connection
    mydb = MyCon.connect(
        host="127.0.0.1",
        user="root",
        password="Sneha$29"
    )
    # Check if connection is successful
    if mydb.is_connected():
        print("Connection Established")
    else:
        print("Connection Failed")
    # Close connection
    mydb.close()
except Exception as e:
    print("Connection Error:", e)
