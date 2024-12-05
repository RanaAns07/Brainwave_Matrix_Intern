import tkinter as tk
import Login_window
import temp_database

def signup_win():

    global fullname,email,username,password,con_password, root
    
    
    root = tk.Tk()
    root.geometry("1100x500+120+100")
    root.title("Inventory Managment System by Ans Mustafa")
    root.config(bg="white")
    
    # variables
    db_fullname = tk.StringVar()
    db_email = tk.StringVar()
    db_username = tk.StringVar()
    db_password = tk.StringVar()
    db_con_password = tk.StringVar()
    
    # Title 
    title = tk.Label(root, text="Inventory Management System", font=("times new roman", 30, "bold"), fg="black", anchor="w", padx=20)
    title.place(x=0, y=0, relwidth=1, height=50)
    
    # Signup Title 
    signup_pg = tk.Label(root, text="Register Yourself", font=("times new roman", 15, "bold"), bg="#336699", fg="white", anchor="center")
    signup_pg.place(x=50, y=70, width=1000, height= 30)
    
    # Signup Content frame
    signup_frame = tk.LabelFrame(root, text="Signup Details", bg="white",bd=3,relief="ridge", font=("goudy old style", 12, "bold"))
    signup_frame.place(x=200, y=120, width=650, height=270)
    
    #  Signup Content
    name = tk.Label(text="Full Name", font=("times new roman,", 12), bg="white").place(x=220, y=150)
    email = tk.Label(text="Email", font=("times new roman,", 12),bg="white").place(x=220, y=190)
    username = tk.Label(text="username", font=("times new roman,", 12), bg="white").place(x=220, y=230)
    password = tk.Label(text="Password", font=("times new roman,", 12),bg="white").place(x=220, y=270)
    con_password = tk.Label(text="Confirm Password", font=("times new roman,", 12),bg="white").place(x=220, y=310)
    
    # signup Content Entries
    entry_name = tk.Entry(signup_frame,textvariable=db_fullname, font=("Ariel", 12), bg="lightyellow").place(x=170, y=10, width=200)
    entry_email = tk.Entry(signup_frame, textvariable= db_email, font=("Ariel", 12), bg="lightyellow").place(x=170, y=50, width=200)
    entry_username = tk.Entry(signup_frame, textvariable= db_username, font=("Ariel", 12), bg="lightyellow").place(x=170, y=90, width=200)
    entry_password = tk.Entry(signup_frame, textvariable= db_password,show="*", font=("Ariel", 12), bg="lightyellow").place(x=170, y=130, width=200)
    entry_con_password = tk.Entry(signup_frame, textvariable= db_con_password,show="*", font=("Ariel", 12), bg="lightyellow").place(x=170, y=170, width=200)
    
    # Login and Signup Buttons
    
    signup_btn = tk.Button(signup_frame,text="SIGN UP", font=("times new roman", 12, "bold"), bg="#009999", fg="white", bd=2, relief="ridge", cursor="hand2",command=lambda:temp_database.signup(db_fullname.get(), db_email.get(), db_username.get(), db_password.get(), db_con_password.get())).place(x=470, y=205, width=100)
    
    login_btn = tk.Button(signup_frame,text="Back to Login", font=("times new roman", 12, "bold"), bg="#cc6600", fg="white", bd=2, relief="ridge", cursor="hand2", command=lambda:[root.destroy(), Login_window.login_win()]).place(x=350, y=205, width=110)
    
    
    
    
    # footer
    footer = tk.Label(root, text="Inventory Management System by Ans Mustafa\nContact: ranaans.pk@gmail.com",
    font=("times new roman", 10), bg="#43656d", fg="white")
    footer.pack(side="bottom", fill="x")
    root.mainloop()
    

if __name__ == "__main__":  
    signup_win()