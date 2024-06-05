import mysql.connector as mysql 
import getpass

from tkinter import *

MY_HOST = 'localhost'
MY_DB = 'bank'

def validate_login():
    try:
        # save entered credentials as a string
        user_login = username_entry.get()
        user_pswd = password_entry.get()

        # Establish a connection
        db = mysql.connect(host=MY_HOST, user=user_login, password=user_pswd, database=MY_DB)
        cur = db.cursor(prepared=True)

        # Check if the connection is open
        if db.is_connected():
            username_entry.pack_forget()
            username_label.pack_forget()
            password_entry.pack_forget()
            password_label.pack_forget()
            login_button.pack_forget()
            mycursor = db.cursor()

            title = Label(window, text="You are connected!")
            title.pack()

            print("Successfully connected to DB.")
        else:
            print("Connection failed.")

        # Close the connection
        db.close()

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


