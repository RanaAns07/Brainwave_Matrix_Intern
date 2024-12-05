from tkinter import *
import temp_database


# ADD PRODUCTS


def add_product_window(root, update_chart_frame):
    # Create a new top-level window for adding a product
    add_product_window = Toplevel(root)
    add_product_window.geometry("1100x500+120+100")
    add_product_window.title("Inventory Management System by Ans Mustafa")
    add_product_window.focus_force()
    
    # Main Title 
    title = Label(add_product_window, text="Inventory Management System", font=("times new roman", 30, "bold"), fg="black", anchor="w", padx=20)
    title.place(x=0, y=0, relwidth=1, height=50)

    # Product Details Title
    emp_details = Label(add_product_window, text="Product Details", font=("times new roman", 15, "bold"), bg="#010c48", fg="white", anchor="center")
    emp_details.place(x=50, y=75, width=1000, height=30)
    
    # Product Info Variables
    pid = StringVar()
    pname = StringVar()
    pvendor = StringVar()
    pprice = StringVar()
    psales = StringVar()
    
    # Product Content frame
    product_frame = LabelFrame(add_product_window, text="ADD PRODUCT INFO", bg="white", bd=3, relief="ridge", font=("times new roman", 12, "bold"))
    product_frame.place(x=200, y=120, width=650, height=350)
    
    # Product Info Labels and Entry Fields
    Label(product_frame, text="Product ID", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=30)
    Entry(product_frame, font=("times new roman", 12), textvariable=pid, bd=2, relief="ridge").place(x=180, y=30, width=375)

    Label(product_frame, text="Product Name", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=70)
    Entry(product_frame, font=("times new roman", 12), textvariable=pname, bd=2, relief="ridge").place(x=180, y=70, width=375)

    Label(product_frame, text="Vendor", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=110)
    Entry(product_frame, font=("times new roman", 12), textvariable=pvendor, bd=2, relief="ridge").place(x=180, y=110, width=375)

    Label(product_frame, text="Price", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=150)
    Entry(product_frame, font=("times new roman", 12), textvariable=pprice, bd=2, relief="ridge").place(x=180, y=150, width=375)

    Label(product_frame, text="Sales", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=190)
    Entry(product_frame, font=("times new roman", 12), textvariable=psales, bd=2, relief="ridge").place(x=180, y=190, width=375)
    
    # Submit Button
    submit_button = Button(add_product_window, text="Add Product", font=("times new roman", 14, "bold"), bg="green", fg="white",command=lambda:[temp_database.add_product(pid.get(), pname.get(), pvendor.get(), pprice.get(), psales.get(), update_chart_frame), add_product_window.destroy()])
    submit_button.place(x=330, y=375, width=400, height=40)
    # Delete Product
    submit_button = Button(add_product_window, text="Delete Product", font=("times new roman", 14, "bold"), bg="red", fg="white",command=lambda:[temp_database.delete_product(pid.get(), update_chart_frame), add_product_window.destroy()])
    submit_button.place(x=330, y=420, width=400, height=40)


# UPDATE PRODUCTS INFO

    
def upd_product_window(root, update_chart_frame):
    # Create a new top-level window for adding a product
    upd_product_window = Toplevel(root)
    upd_product_window.geometry("1100x500+120+100")
    upd_product_window.title("Inventory Management System by Ans Mustafa")
    upd_product_window.focus_force()
    
    # Main Title 
    title = Label(upd_product_window, text="Inventory Management System", font=("times new roman", 30, "bold"), fg="black", anchor="w", padx=20)
    title.place(x=0, y=0, relwidth=1, height=50)

    # Product Details Title
    emp_details = Label(upd_product_window, text="Update Product Details", font=("times new roman", 15, "bold"), bg="#010c48", fg="white", anchor="center")
    emp_details.place(x=50, y=75, width=1000, height=30)
    
    # Product Info Variables
    upd_pid = StringVar()
    upd_pname = StringVar()
    upd_pvendor = StringVar()
    upd_pprice = StringVar()
    upd_psales = StringVar()
    
    # Product Content frame
    product_frame = LabelFrame(upd_product_window, text="UPDATE PRODUCT INFO", bg="white", bd=3, relief="ridge", font=("times new roman", 12, "bold"))
    product_frame.place(x=200, y=120, width=650, height=350)
    
    # Product Info Labels and Entry Fields
    Label(product_frame, text="Product ID", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=30)
    Entry(product_frame, font=("times new roman", 12), textvariable=upd_pid, bd=2, relief="ridge").place(x=180, y=30, width=375)

    Label(product_frame, text="Product Name", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=70)
    Entry(product_frame, font=("times new roman", 12), textvariable=upd_pname, bd=2, relief="ridge").place(x=180, y=70, width=375)

    Label(product_frame, text="Vendor", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=110)
    Entry(product_frame, font=("times new roman", 12), textvariable=upd_pvendor, bd=2, relief="ridge").place(x=180, y=110, width=375)

    Label(product_frame, text="Price", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=150)
    Entry(product_frame, font=("times new roman", 12), textvariable=upd_pprice, bd=2, relief="ridge").place(x=180, y=150, width=375)

    Label(product_frame, text="Sales", font=("times new roman", 12), bg="white", fg="black").place(x=20, y=190)
    Entry(product_frame, font=("times new roman", 12), textvariable=upd_psales, bd=2, relief="ridge").place(x=180, y=190, width=375)
    
    # Submit Button
    submit_button = Button(upd_product_window, text="Update Product Info", font=("times new roman", 14, "bold"), bg="Orange", fg="white",command=lambda:[temp_database.update_product(upd_pid.get(), upd_pname.get(), upd_pvendor.get(), upd_pprice.get(), upd_psales.get(), update_chart_frame), upd_product_window.destroy()])
    submit_button.place(x=330, y=400, width=400, height=40)



