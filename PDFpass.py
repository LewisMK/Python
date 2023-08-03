import pikepdf
from tqdm import tqdm

# load the password list from local storage

passwords = [ line.strip() for line in open("fasttrack.txt") ]

# iterate over passwords

for password in tqdm(passwords, "Decrypting PDF"):

    try:
        #open PDF file
        
        with pikepdf.open("hello", password=password) as pdf:
            # if the password is decrypted successfully, break out of the loop

            print("[+] Password found:", password)
            break

    except pikepdf._core.PasswordError as e:
        # wrong password, just continue the loop

        continue
    
