import hashlib
import json

def save_credentials(username, password):
    #open the file in append modile

    with open('multipass.txt', 'a') as file:
        #sha256 hash for the password_hash
        password_hash = hashlib.sha256(password.encode())
        data = {'username': username, 'password': password_hash.hexdigest()}

        #write the data as a json file object

        json.dump(data, file)
        file.write('\n') #add a new line after every entry


#Main function to take inputs and save them to outfile

def main():
    while True:

        username = input("Enter your username (Enter 'q' to quit'): ")
        if username == 'q':
            break
        password = input("Enter the password: ")

        save_credentials(username, password)

        print("Creds Saved.")

#Call main function to start the program

if __name__ == '__main__':

    main()

