import sqlite3
from logo import logo
import datetime


def connection(path):
    connector = sqlite3.connect(path)
    cursor = connector.cursor()
    return connector, cursor


def login(connector, cursor):
    print("**type register if you are new**")
    username = input("enter your username: ")
    if username == "register":
        register(connector, cursor)
    else:
        password = input("enter your password: ")
        statement = f"SELECT username FROM users WHERE username='{username}' AND password = '{password}';"
        cursor.execute(statement)
        if not cursor.fetchone():
            print("**Username or password is wrong**")
            command = input("type login to try again or type register if you are new: ")
            if command == "register":
                register(connector, cursor)
            elif command == "login":
                login(connector, cursor)
            else:
                print("**command is wrong**")
                login(connector, cursor)
        else:
            statement = f"SELECT user_id FROM users WHERE username='{username}' AND password = '{password}';"
            cursor.execute(statement)
            tuple_user_id = cursor.fetchone()
            global str_user_id
            str_user_id = tuple_user_id[0]
            mainpage()



def register(connector, cursor):
    new_username = input("enter a username: ")
    statement = f"SELECT username FROM users WHERE username='{new_username}' ;"
    cursor.execute(statement)
    if not cursor.fetchone() and new_username != "register":
        new_password = input("enter a password: ")
        confirm_password = input("confirm your password: ")
        if new_password == confirm_password:
            data_tuple = (new_username, new_password)
            cursor.execute("INSERT INTO users VALUES(?, ?)", data_tuple)
            connector.commit()
            print("you registerd successfully")
            login(connector, cursor)
        else:
            print("**passwords are not matched**")
            register(connector, cursor)
    else:
        print("**username is not unique**")
        register(connector, cursor)



def mainpage():
    logo()
    print("avalible commands: products - orders - profile")
    command = input("type your command: ")
    if command == "products":
        products(connector, cursor)
    elif command == "cart":
        pass
    elif command == "profile":
        profile(connector, cursor)
    else:
        print("**command is wrong**")
        mainpage()



def products(connector, cursor):
    print("avalible categories: phones - laptops - accessories")
    category = input("choose a category: ")
    if category:
        statement = f"SELECT product_id, name, price FROM products WHERE category='{category}' "
        products = cursor.execute(statement)
        print(list(products))
        Q = input("type 1 if you want to add prooducts to your cart: ")
        if Q == "1":
            product_id = input("enter a product id: ")
            price = f"SELECT price FROM products WHERE product_id={product_id}"
            cursor.execute(price)
            price2 = price[0]
            quantity = input("quantity: ")
            cursor.execute(f"INSERT INTO products VALUES(1, product_id={product_id}, price={price2}, quantity={quantity})")
            connector.commit()
            print("priduct added successfully")
        else:
            print("**command is wrong**")
            mainpage()
    else:
        print("**command is wrong**")
        mainpage()



def profile(connector, cursor):
    statement = f"SELECT username, password FROM users WHERE user_id='{str_user_id}' "
    info = cursor.execute(statement)
    print("your information:", list(info))
    Q = input("type 1 you want to change your password: ")
    if Q == "1":
        new_password = input("enter your new password: ")
        statement = f"UPDATE users SET password='{new_password}' WHERE user_id={str_user_id} "
        cursor.execute(statement)
        connector.commit()
        print("your password changed successfully")
    else:
        print("**command is wrong**")
        mainpage()
 



if __name__ == "__main__":
    connector, cursor = connection('data.db')
    login(connector, cursor)

