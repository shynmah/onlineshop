import sqlite3

connector = sqlite3.connect("data.db")
cursor = connector.cursor()



cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")

cursor.execute("INSERT INTO users (username, password) VALUES('admin', 'admin')")
cursor.execute("INSERT INTO users (username, password) VALUES('AmirAndouhgin', 'amir')")
cursor.execute("INSERT INTO users (username, password) VALUES('ShayanMahjoob', 'shayan')")
cursor.execute("INSERT INTO users (username, password) VALUES('SaeedHashemi', 'saeed')")
cursor.execute("INSERT INTO users (username, password) VALUES('RezaKaido', 'reza')")



cursor.execute("CREATE TABLE IF NOT EXISTS products(product_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, category TEXT NOT NULL, price INTEGER NOT NULL)")

cursor.execute("INSERT INTO products (name, category, price) VALUES('Iphone 14', 'phones',  1000)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Samsung S23', 'phones',  800)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Google Pixel', 'phones',  960)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Xiaomi 12 pro', 'phones',  740)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Samsung Z Flip4', 'phones',  1000)")

cursor.execute("INSERT INTO products (name, category, price) VALUES('Macbook pro', 'laptops', 1800)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Asus Zephyrus', 'laptops', 1500)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Acer Predator', 'laptops', 1300)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('HP Envy 13', 'laptops', 1400)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Dell XPS 15', 'laptops', 2500)")

cursor.execute("INSERT INTO products (name, category, price) VALUES('Razor Viper mini', 'accessories', 240)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Sure SM7B', 'accessories', 800)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Apple Airpod pro', 'accessories', 500)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Western Digital 1Tr', 'accessories', 120)")
cursor.execute("INSERT INTO products (name, category, price) VALUES('Mi Powerbank', 'accessories', 100)")



# cursor.execute("""CREATE TABLE IF NOT EXISTS orders( order_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                                                      user_id INTEGER, 
#                                                      is_paid INTEGER NOT NULL DEFAULT 0 CHECK(is_paid IN (0,1)),
#                                                      created DATE DEFAULT (DATE(CURRENT_DATE)), 
#                                                      FOREIGN KEY(user_id) REFERENCES users(user_id) )""")

# cursor.execute("""CREATE TABLE IF NOT EXISTS cart(cart_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                                                   order_id INTEGER, 
#                                                   product_id INTEGER, 
#                                                   price REAL NOT NULL, 
#                                                   quantity INTEGER NOT NULL, 
#                                                   total_price REAL AS (price * quantity),
#                                                   FOREIGN KEY(order_id) REFERENCES orders(order_id), 
#                                                   FOREIGN KEY(product_id) REFERENCES products(product_id) )""")

cursor.execute("""CREATE TABLE IF NOT EXISTS cart(cart_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                   product_id INTEGER, 
                                                   price REAL NOT NULL, 
                                                   quantity INTEGER NOT NULL, 
                                                   total_price REAL AS (price * quantity),
                                                   FOREIGN KEY(product_id) REFERENCES products(product_id) )""")

connector.commit()


