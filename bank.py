import mysql.connector 
import getpass

print("-----------------------------------\nWelcome to the Banking System!\n-----------------------------------")
username = input("Enter your username: ")
db_connection_pw = getpass.getpass("Please enter the root password: ")

def view_db(table_name, selection):
    query = "SELECT " + selection + " FROM " + table_name
    return query

try:
    # Establish a connection
    db = mysql.connector.connect(
    host="localhost", 
    user= username,  
    passwd= db_connection_pw,
    database="bank"
    )

    # Check if the connection is open
    if db.is_connected():
        print("\nConnection is established.")
        mycursor = db.cursor()

        option = int(input("What would you like to do? (1)View (2)Update (3)Delete:  "))
        if option == 1:
            table = input("Enter table name: ")
            selection = input("--> Enter '*' to view the entire table or write a specific selection:  ")
            sql_command = view_db(table, selection)
            mycursor.execute(sql_command)
        elif option == 2: 
            print("Selection: Update Database")
        elif option == 3:
            print("Selection: Delete Database")

        print("-----------------------------------\nResults\n-----------------------------------")
        for x in mycursor:
            print(x)
    else:
        print("Connection failed.")

    # Close the connection
    db.close()

except mysql.connector.Error as err:
    print(f"Error: {err}")

