import mysql.connector as mysql 
import getpass

from tkinter import *

MY_HOST = 'localhost'
MY_DB = 'bank'

# Global variable to hold the database connection
db = None

def validate_login():
    global db 
    try:
        # save entered credentials as a string
        user_login = username_entry.get()
        user_pswd = password_entry.get()

        # Establish a connection
        db = mysql.connect(host=MY_HOST, user=user_login, password=user_pswd, database=MY_DB)

        # Check if the connection is open
        if db.is_connected():
            username_entry.pack_forget()
            username_label.pack_forget()
            password_entry.pack_forget()
            password_label.pack_forget()
            login_button.pack_forget()

            print("Successfully connected to DB.")
            def view_users(): 
                try:
                    cur = db.cursor(prepared=True)
                    #send query 
                    cur.execute("SELECT * FROM customer")
                    result = cur.fetchall()
                    
                    # Create a Text widget with height=12 and width=40
                    text_box = Text(window, height=20, width=50)
                    text_box.pack(expand=True)

                    text_box.insert('end', result)

                except mysql.Error as err:
                    print(f"Error: {err}")
                finally:
                    cur.close()

            # New customer button
            new_customer_button = Button(window, text="Add User")
            new_customer_button.pack()

            # New customer button
            existing_customer_button = Button(window, text="View Existing Users", command=view_users)
            existing_customer_button.pack()

        else:
            print("Connection failed.")

    except mysql.Error as err:
        print(f"Error: {err}")


# Create the main window
window = Tk()
window.title("Banking App")
window.geometry("300x200")  

# Username label and entry
username_label = Label(window, text="Username:")
username_label.pack()

username = StringVar()
username_entry = Entry(window, textvariable=username)
username_entry.pack()

# Password label and entry
password_label = Label(window, text="Password:")
password_label.pack()

password = StringVar()
password_entry = Entry(window, textvariable=password, show="*")
password_entry.pack()

# Login button
login_button = Button(window, text="Login", command=validate_login)
login_button.pack()

# Start the event loop
window.mainloop()

# Close the connection when the application window is closed
if db and db.is_connected():
    db.close()
