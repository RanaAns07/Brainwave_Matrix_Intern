import tkinter as tk
from tkinter import messagebox
import signup
import temp_database



def login_win():
    global valid_username, valid_password, root
    
    root = tk.Tk()
    root.geometry("1100x500+120+100")
    root.title("Inventory Managment System by Ans Mustafa")
    root.config(bg="white")
    
    # variables
    valid_username = tk.StringVar()
    valid_password = tk.StringVar()
    
    
    # Title 
    title = tk.Label(root, text="Inventory Management System", font=("times new roman", 30, "bold"), fg="black", anchor="w", padx=20)
    title.place(x=0, y=0, relwidth=1, height=50)
    
    # Login Title 
    login_pg = tk.Label(root, text="Login Page", font=("times new roman", 15, "bold"), bg="#336699", fg="white", anchor="center")
    login_pg.place(x=50, y=70, width=1000, height= 30)
    
    # Login Content frame
    login_frame = tk.LabelFrame(root, text="Login Credentials", bg="white",bd=3,relief="ridge", font=("goudy old style", 12, "bold"))
    login_frame.place(x=250, y=120, width=600, height=270)
    
    #  Login Content
    username = tk.Label(text="Username", font=("goudy old style,", 12, "bold"), bg="white").place(x=350, y=200)
    password = tk.Label(text="Password", font=("goudy old style,", 12, "bold"),bg="white").place(x=350, y=250)
    
    # Login Content Entries
    username = tk.Entry(login_frame,textvariable=valid_username, font=("Ariel", 12), bg="lightyellow").place(x=210, y=60, width=200)
    password = tk.Entry(login_frame, textvariable= valid_password,show="*", font=("Ariel", 12), bg="lightyellow").place(x=210, y=110, width=200)
    
    # Login and Signup Buttons
    login_btn = tk.Button(login_frame,text="Login", font=("times new roman", 12, "bold"), bg="#009999", fg="white", bd=2, relief="ridge", cursor="hand2", command=lambda:[temp_database.login_validation(valid_username.get(), valid_password.get(), root)]).place(x=300, y=160, width=100)
    
    signup_btn = tk.Button(login_frame,text="Signup", font=("times new roman", 12, "bold"),command=lambda:[root.destroy(), signup.signup_win()], bg="#009999", fg="white", bd=2, relief="ridge", cursor="hand2").place(x=420, y=160, width=100)
    
    message_label = tk.Label(root, text="", font=("Arial", 12))
    message_label.pack(pady=10)
    
    # footer
    footer = tk.Label(root, text="Inventory Management System by Ans Mustafa\nContact: ranaans.pk@gmail.com",
    font=("times new roman", 10), bg="#43656d", fg="white")
    footer.pack(side="bottom", fill="x")
    root.mainloop()

   
if __name__ == "__main__":  
    login_win()