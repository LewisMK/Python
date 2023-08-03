import hashlib
import json

def save_credentials(username, password):
    
    #open the file in append mode

    with open('multipass.txt', 'a') as file:
        #sha256 hash for the password_hash
        password_hash = hashlib.sha256(password.encode())
        data = {'username': username, 'password': password_hash.hexdigest()}

        #write the data as a json file object

        json.dump(data, file)
        file.write('\n') #add a new line after every entry


# Main function to take inputs and save them to outfile

def main():
    while True:

        username = input("Enter your username (Enter 'q' to quit'): ")
        if username == 'q':
            break
        password = input("Enter the password: ")

        save_credentials(username, password)  # Call main function to start the program

        print("Creds Saved.")



if __name__ == '__main__':

    main()

#  the json format ensures that we can save multiple username/password entries at the same time 
#  also, new entries are simply added to the end of the list without deleting past entries

