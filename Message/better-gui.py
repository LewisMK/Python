from tkinter import *
from tkinter import messagebox
import base64
import os

def decrypt():
    password = code.get()                    # Decryption logic
    
    if password == "1234":
        screen2 = Toplevel(screen)            # Top level displays this screen above the main window
        screen2.title("decryption")
        screen2.geometry("400x200")
        screen2.configure(bg="#00bd56")
        
        message = text1.get(1.0, END)
        decode_message = message.encode("ascii")
        base64_bytes = base64.b64decode(decode_message)
        
        decrypt = base64_bytes.decode("ascii")
        
        Label(screen2, text="DECRYPT", font="arial", fg="white", bg="#00bd56").place(x=10, y= 0)
        text2 = Text(screen2, font = "Robote 10", bg="white", relief=GROOVE, wrap = WORD, bd=0)
        text2.place(x=10, y= 40, width=380, height=150)
        
        text2.insert(END, decrypt)
    
    elif password == "":
        messagebox.showerror("decryption", "Input a password") # Deal with empty password 
    
    elif password != "1234":
        messagebox.showerror("decryption", "Wrong password")    # Confirm correct password
    
def encrypt():                                                   # Encryption logic. Similar but opposite of the decryption logic
    password = code.get()
    
    if password == "1234":
        screen1 = Toplevel(screen)
        screen1.title("encryption")
        screen1.geometry("400x200")
        screen1.configure(bg="#ed3833")
        
        message = text1.get(1.0, END)
        encode_message = message.encode("ascii")
        base64_bytes = base64.b64encode(encode_message)
        
        encrypt = base64_bytes.decode("ascii")
        
        Label(screen1, text="ENCRYPT", font="arial", fg="white", bg="#ed3833").place(x=10, y= 0)
        text2 = Text(screen1, font = "Robote 10", bg="white", relief=GROOVE, wrap = WORD, bd=0)
        text2.place(x=10, y= 40, width=380, height=150)
        
        text2.insert(END, encrypt)
    
    elif password == "":
        messagebox.showerror("encryption", "Input a password")
    
    elif password != "1234":
        messagebox.showerror("encryption", "Wrong password")
        

def main_screen():
    
    global screen                # three global variables shared by the external functions.
    global code
    global text1
    
    screen = Tk()
    screen.geometry("375x398")
    
    # icon
    
    # Customize the window title and icon
    window_title = "The Crypt"
    window_icon_path = r"C:\Users\Elwiz\Desktop\PYTHON\Python\Message\encryption.png"
    screen.title(window_title)
    image_icon = PhotoImage(file=window_icon_path)
    screen.iconphoto(False, image_icon)

    
    def reset():
        code.set("")
        text1.delete(1.0, END)
    
    # Use a modern font for labels and text widgets
    font_style = ("Helvetica", 12)
    Label(text="Enter text to encrypt and decrypt:", fg="black", font=font_style).place(x=10, y=10)
    text1 = Text(font=("Helvetica", 20), bg="white", relief=GROOVE, wrap=WORD, bd=2)
    text1.place(x=10, y=50, width=355, height=100)

    
    Label(text = "Enter secret key to encrypt and decrypt: ", fg="black", font=("arial", 13)).place(x=10, y=170)
    
    code = StringVar()
    Entry(textvariable=code, width=19,bd=0,font=("arial", 25), show="*").place(x=10, y=200)
    
   # Change the color scheme to more modern colors
   
    bg_color = "#F0F0F0"  # Light gray background
    button_color1 = "#FF7070"  # Red for encrypt button
    button_color2 = "#70C870"  # Green for decrypt button
    button_color3 = "#7070FF"  # Blue for reset button
    
    Button(text="ENCRYPT", height="2",width=23,bg="#ed3833",fg="white",bd=0, command=encrypt).place(x=10, y=250)
    Button(text="DECRYPT", height="2",width=23,bg="#00bd56",fg="white",bd=0, command=decrypt).place(x=200, y=250)
    Button(text="RESET", height="2",width=50,bg="#1089ff",fg="white",bd=0, command=reset).place(x=10, y=300)

    
    
    screen.mainloop()

main_screen()
