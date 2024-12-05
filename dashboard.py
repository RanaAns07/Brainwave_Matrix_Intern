import add_and_del_product
from tkinter import *
from PIL import Image, ImageTk
import temp_database


def dashboard_win(nroot):
    global valid_username, valid_password, root
    root = Toplevel(nroot)

    root.geometry("1920x1080+0+0")
    root.title("Inventory Managment System by Ans Mustafa")
    root.config(bg="white")
    
    # Title
    title = Label(root, text="Inventory Management System", font=("times new roman", 40, "bold"),bg="#010c48", fg="white", anchor="w", padx=20)
    title.place(x=0, y=0, relwidth=1, height=70)
    
    # Time and Clock Components
    label_clock = Label(root, text="Dashboard of Inventory Management System\t\t\t\t Date: DD-MM-YYYY\t\t\t\t Time: HH-MM-SS",font=("times new roman", 12,), bg="#43636d", fg="white")
    label_clock.place(x=0, y=70, relwidth=1, height=30)
    
    # Left Menu
    menu_logo = Image.open("menu_logo.png")
    menu_logo = menu_logo.resize((160, 160), Image.Resampling.LANCZOS)
    menu_logo = ImageTk.PhotoImage(menu_logo)
    left_menu = Frame(root, bd=2, relief="ridge", bg="#f0f0f0")
    left_menu.place(x=0, y=110, width=220, height=550)

    label_menu_logo = Label(left_menu, image=menu_logo, bg="#f0f0f0")
    label_menu_logo.pack(side=TOP, fill=X)
    
    # Menu Buttons
    menu_label = Label(left_menu, text="MENU", font=("times new roman", 18, "bold"),bg="#009688", fg="white", bd=3, relief="ridge")
    menu_label.pack(side=TOP, fill=X, pady=20)
    
    add_product_menu = Button(left_menu,command=lambda:[add_and_del_product.add_product_window(root, chart_frame)], text="Add Product", font=("times new roman", 17, "bold"),
    bg="white", cursor="hand2", bd=3, relief="ridge")
    add_product_menu.pack(side=TOP, fill=X)
    
    update_product_menu = Button(left_menu, text="Update Product", font=("times new roman", 17, "bold"),
    bg="white", cursor="hand2", bd=3,command=lambda:[add_and_del_product.upd_product_window(root, chart_frame)], relief="ridge")
    update_product_menu.pack(side=TOP, fill=X)
    
    generate_resport_menu = Button(left_menu, text="Generate Reports", font=("times new roman", 17, "bold"),
    bg="white", cursor="hand2", bd=3, relief="ridge")
    generate_resport_menu.pack(side=TOP, fill=X)

    exit_menu = Button(left_menu, text="Exit",command=lambda:root.destroy(), font=("times new roman", 17, "bold"),
    bg="white", cursor="hand2", bd=3, relief="ridge")
    exit_menu.pack(side=TOP, fill=X)
    
    # Bar chart placehoder frame for products
    
    chart_frame = Frame(root, bg="lightgrey", bd=2, relief="ridge")
    chart_frame.place(x=240, y=130, width=1000, height=510)
    
    
    chart_lable = Label(chart_frame, text="Product Sales", font=("times new roman", 20,"bold" ), bg="lightgrey", fg="black")
    chart_lable.pack(pady=10)
    
    temp_database.display_chart(chart_frame)
    
    # footer
    footer = Label(root, text="Inventory Management System by Ans Mustafa\nContact: ranaans.pk@gmail.com",
    font=("times new roman", 10), bg="#43656d", fg="white")
    footer.pack(side="bottom", fill="x")
    root.mainloop() 
    

if __name__ == "__main__":
    dashboard_win()