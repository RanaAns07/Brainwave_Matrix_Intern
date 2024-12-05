from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
import dashboard

database = {'ansmustafa': {'fullname': 'Ans Mustafa', 'email': 'ranaans.pk@gmail.com', 'password': '12321'}}
product_database = {
    "product_id_1": {"Product Name": "Product A","Product Vendor":"Manufacturer", "Product Price": 100, "Product Sales": 10},
    "product_id_2": {"Product Name": "Product B","Product Vendor":"Developer", "Product Price": 1200, "Product Sales": 40},
    "product_id_3": {"Product Name": "Product C","Product Vendor":"Ans Mustafa", "Product Price": 2100, "Product Sales": 90},

    
}
# function for extracting data of product from product table for chart

def get_sales_data():
    product_names = [product_database[pid]["Product Name"] for pid in product_database]
    sales = [product_database[pid]["Product Sales"] for pid in product_database]
    return product_names, sales

# function to display bar char in the application
def display_chart(chart_frame):
    
    for widget in chart_frame.winfo_children():
        widget.destroy()
    
    name, sales = get_sales_data()
    fig = Figure(figsize=(8, 4), dpi=100)
    ax = fig.add_subplot(111)
    ax.bar(name, sales, color= "skyblue")
    ax.set_title("Sales Chart")
    ax.set_xlabel("Products")
    ax.set_ylabel("Sales")
    
    canvas = FigureCanvasTkAgg(fig, master=chart_frame)
    canvas.draw()
    canvas.get_tk_widget().pack(fill="both")

    # interactive toolbar
    toolbar = NavigationToolbar2Tk(canvas, chart_frame)
    toolbar.update()
    toolbar.pack(side="bottom", fill="x")

def signup(fullname, email, username, password, con_password):
    if username in database:
        messagebox.showerror("Error", "User Already Exist")  # Fixed spelling of "Exist"
    elif fullname == "" or email == "" or username == "" or password == "" or con_password == "":
        messagebox.showerror("Error", "Please Fill all Fields")  # Simplified message for empty fields
    elif password != con_password:
        messagebox.showerror("Error!", "Password should be same")  # Clarified message
    else:
        # Save user details to the database (dictionary)
        database[username] = {
            "fullname": fullname,
            "email": email,
            "password": password
        }
        messagebox.showinfo("INFO", "Signup Successful!")

def login_validation(username, password, root):
    # Check for empty inputs
    if username == "" or password == "":
        messagebox.showerror("Error", "Please fill in all fields!")
    # Validate credentials against the database
    elif username in database and database[username]["password"] == password:
        messagebox.showinfo("Success", "Login successful!")
        # Ensure Login_window.root exists and is imported
        try:
            dashboard.dashboard_win(root)
        except AttributeError:
            messagebox.showerror("Error", "Unable to close the login window.")
    else:
        messagebox.showerror("Error", "Invalid username or password.")
    print(database)
    
def add_product(pid, pname, pvender, pprice, psales, chart_frame):
    if pid in product_database:
        messagebox.showerror("Error", "Product Already Exist")  # Fixed spelling of "Exist"
    elif pid == "" or pname == "" or pvender == "" or pprice == "" or psales == "":
        messagebox.showerror("Error", "Please Fill all Fields")  # Simplified message for empty fields
    else:
        # type conversion
        try:
            psales = float(psales)  # Convert to float if you expect decimal sales values
        except ValueError:
            print("Error: Sales value must be a number.")
            return
        # Save user details to the database (dictionary)
        product_database[pid] = {
            "Product Name": pname,
            "Product Vendor": pvender,
            "Product Price": pprice,
            "Product Sales": psales
        }
        messagebox.showinfo("INFO", "Product Added Successful!")
        display_chart(chart_frame)
        print(product_database)
def update_product(pid, pname, pvender, pprice, psales, chart_frame):
    if pid not in product_database:
        messagebox.showerror("Error", "Product Not Found")  # Error if product doesn't exist
    elif pname == "" or pvender == "" or pprice == "" or psales == "":
        messagebox.showerror("Error", "Please Fill all Fields")  # Check if fields are empty
    else:
        # type conversion
        try:
            psales = float(psales)  # Convert to float if you expect decimal sales values
        except ValueError:
            print("Error: Sales value must be a number.")
            return

        # Update product information
        product_database[pid] = {
            "Product Name": pname,
            "Product Vendor": pvender,
            "Product Price": pprice,
            "Product Sales": psales
        }
        messagebox.showinfo("INFO", "Product Updated Successfully!")
        display_chart(chart_frame)
        print(product_database)

def delete_product(pid, chart_frame):
    if pid not in product_database:
        messagebox.showerror("Error", "Product Not Found")  # Error if product doesn't exist
    else:
        del product_database[pid]  # Remove product from the database
        messagebox.showinfo("INFO", "Product Deleted Successfully!")
        display_chart(chart_frame)
        print(product_database)
