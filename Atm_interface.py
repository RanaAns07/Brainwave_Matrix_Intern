import mysql.connector
# connect the database

db = mysql.connector.connect(
    host = '127.0.0.1',
    username = 'root',
    password = '101b5binary',
    database = 'atm_system'
)

cursor = db.cursor()

# Functionalities

# 1. Add user
def add_user():
    name = input("Please Enter Your Name: ")
    pin = int(input("Please Enter the only Numbers with Maximum of 6 digits: "))
    balance = float(input("Please Enter your Intial Amount: "))
    try:
        query = "INSERT INTO User (name, pin, balance) VALUES (%s, %s, %s)"
        values = (name, pin, balance)
        cursor.execute(query, values)
        db.commit()
        print("User added Successfully! ")
    except:
        print("An Error Occuried in add_user function! ")
    
    
# 2. User Authentication
def authenticate_user():
    name = input("Please Enter your Valid name: ")
    pin = int(input("Please Enter your valid 6-digit PIN: "))
    try:
        query = "SELECT id, balance FROM User WHERE name  = %s AND pin = %s"
        
        cursor.execute(query, (name, pin))
        result = cursor.fetchone()
        
        if (result):
            print("Login Successfull! ")
            return result[0]
        else:
            print("Invalid Credentials. ")
            return None
    except:
        print("An Error Occured in Authenticate Function! ")

# Atm Functionalities

def check_balance(user_id):
    try:
        query = "SELECT balance FROM User WHERE id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()[0]
        print(f"Your current Balance is: {result}")
        return result
    except:
        print("An Error Occuried in check_balance function! ")

# Deposit Money

def deposit_money(user_id):
    amount  = float(input("Please Enter the amount to deposit: "))
    try:
        query = "UPDATE User SET balance = balance + %s WHERE id = %s "
        cursor.execute(query, (amount, user_id))
        db.commit()
        log_transaction(user_id, 'deposit', amount)
        print("Deposit Successfully Done! ")
    except:
        print("An Error Occured in deposit Money function")
# withdraw Money

def withdraw_money(user_id):
    amount = float(input("Plesae Enter the Amount to Withdraw: "))
    current_balance = check_balance(user_id)
    
    if amount > current_balance:
        print("Insuffient Amount. Please Recharge Your Account.")
    else:
        try:
            query = "UPDATE User SET balance = balance - %s WHERE id = %s "
            cursor.execute(query, (amount, user_id))
            db.commit()
            log_transaction(user_id, 'withdraw', amount)
            print("Withdrwal Successfully Done! ")
        except:
            print("An Error Occured in withdraw money function! ")

def log_transaction(user_id, transaction_type, amount):
    try:
        query = "INSERT INTO transactions (user_id, transaction_type, amount) VALUES (%s, %s, %s)"
        values = user_id, transaction_type, amount
        cursor.execute(query, values)
        db.commit()
    except:
        print("An error Occured in Tranaction Function")
    
# Main Window
def main():
    while True:
        print("1. Add New User. ")
        print("2. Login. ")
        print("3. Exit. ")
        choice = input("Please any one Option from Above: ")
        if choice == "1":
            add_user()
        elif choice == "2":
            user_id = authenticate_user()
            if user_id:
                while True:
                    print("1. Check Balance. ")
                    print("2. Deposit Money. ")
                    print("3. Withdraw Money. ")
                    print("4. Logout. ")
                    action = input("Please Choose one from Above: ")
                    if action == "1":
                        check_balance(user_id)
                    elif action == '2':
                        deposit_money(user_id)
                    elif action == '3':
                        withdraw_money(user_id)
                    elif action == '4':
                        break
                    else:
                        print("Invalid Choice! ")
        elif choice == '3':
            print("Thanks For Using This ATM System! ")
            break
        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()
                    
                    
            
            