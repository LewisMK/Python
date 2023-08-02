import hashlib
import json
import tkinter as tk
from tkinter import messagebox


def save_credentials(username, password):
    #open the file in append modile

    with open('multipass.txt', 'a') as file:
        #sha256 hash for the password_hash
        password_hash = hashlib.sha256(password.encode())
        data = {'username': username, 'password': password_hash.hexdigest()}

        #write the data as a json file object

        json.dump(data, file)
        file.write('\n') #add a new line after every entry

#Callback function for the "Save" button to fetch the input from the entry fields

def on_save_button_click():

    #Get the values of the username and password fields
    username = username_entry.get()
    password = password_entry.get()

    #Save the credentials to the outfile

    save_credentials(username, password)
    messagebox.showinfo("Success", "Creds Saved Successfully")

    #Clear the input fieds after saving

    username_entry.delete(0,tk.END)
    password_entry.delete(0,tk.END)

#Main function to take inputs and save them to outfile

def main():

    global username_entry, password_entry
    
    # create a new tkinter window
    window = tk.Tk()
    window.title("Hash Password Saver")

    #create a label and entry field for the username
    username_label = tk.Label(window, text = "Username:")
    username_label.grid(column = 50, row = 100)
    username_entry = tk.Entry(window)
    username_entry.grid(column = 51, row = 100)

    #create a lable and entry for the password
    password_label = tk.Label(window, text = "Password:")
    password_label.grid(column = 50, row = 101)
    password_entry = tk.Entry(window, show='*')
    password_entry.grid(column =51, row = 101)

    #create a save button
    save_button = tk.Button(window, text="Save", command = on_save_button_click)
    save_button.grid(column = 80, row = 150, columnspan = 10)

    #Start the GUI event loop
    window.mainloop()


#Call main function to start the program

if __name__ == '__main__':

    main()
