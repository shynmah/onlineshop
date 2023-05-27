import sqlite3

def connection(path):
    connector = sqlite3.connect(path)
    cursor = connector.cursor()
    return connector, cursor


def login(connector, cursor):
    username = input("username: ")
    password = input("password: ")
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
        print("Welcome...")
        mainpage()


def register(connector, cursor):
    new_username = input("enter a username: ")
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


def mainpage():
    print("""
                        _..-'(                       )`-.._
                   ./'. '||\\.       (\_/)       .//||` .`\.
                ./'.|'.'||||\\|..    )O O(    ..|//||||`.`|.`\.
             ./'..|'.|| |||||\`````` '`"'` ''''''/||||| ||.`|..`\.
           ./'.||'.|||| ||||||||||||.     .|||||||||||| |||||.`||.`\.
          /'|||'.|||||| ||||||||||||{     }|||||||||||| ||||||.`|||`\
         '.|||'.||||||| ||||||||||||{     }|||||||||||| |||||||.`|||.`
        '.||| ||||||||| |/'   ``\||``     ''||/''   `\| ||||||||| |||.`
        |/' \./'     `\./         \!|\   /|!/         \./'     `\./ `\|
        V    V         V          }' `\ /' `{          V         V    V
        `    `         `               V               '         '    '
        """)
    print("avalible commands: products - orders - profile")
    command = input("type your command: ")
    if command == "products":
        products(connector, cursor)
    elif command == "cart":
        pass
    elif command == "profile":
        pass
    else:
        print("**command is wrong**")
        mainpage()


def products(connector, cursor):
    print("avalible categories: phones - laptops - accessories")
    category = input("choose a category: ")
    if category:
        statement = f"SELECT name, price FROM products WHERE category='{category}' "
        products = cursor.execute(statement)
        print(list(products))
    else:
        print("**command is wrong**")
        mainpage()

def profile(connector, cursor):
    statement = f"SELECT username, password FROM users WHERE category='{category}' "


    







if __name__ == "__main__":
    connector, cursor = connection('data.db')
    login(connector, cursor)

