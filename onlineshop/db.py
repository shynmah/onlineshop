import sqlite3

connector = sqlite3.connect("data.db")
cursor = connector.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS users(user_id INTEGER PRIMARY KEY AUTOINCREMENT, username TEXT NOT NULL UNIQUE, password TEXT NOT NULL)")

cursor.execute("INSERT INTO users VALUES(1, 'admin', 'admin')")
cursor.execute("INSERT INTO users VALUES(2, 'AmirAndouhgin', 'amir')")
cursor.execute("INSERT INTO users VALUES(3, 'ShayanMahjoob', 'shayan')")
cursor.execute("INSERT INTO users VALUES(4, 'SaeedHashemi', 'saeed')")
cursor.execute("INSERT INTO users VALUES(5, 'RezaKaido', 'reza')")



cursor.execute("CREATE TABLE IF NOT EXISTS products(product_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, category TEXT NOT NULL, price INTEGER NOT NULL)")

cursor.execute("INSERT INTO products VALUES(1, 'Iphone 14', 'phones',  1000)")
cursor.execute("INSERT INTO products VALUES(2, 'Samsung S23', 'phones',  800)")
cursor.execute("INSERT INTO products VALUES(3, 'Google Pixel', 'phones',  960)")
cursor.execute("INSERT INTO products VALUES(4, 'Xiaomi 12 pro', 'phones',  740)")
cursor.execute("INSERT INTO products VALUES(5, 'Samsung Z Flip4', 'phones',  1000)")

cursor.execute("INSERT INTO products VALUES(6, 'Macbook pro', 'laptops', 1800)")
cursor.execute("INSERT INTO products VALUES(7, 'Asus Zephyrus', 'laptops', 1500)")
cursor.execute("INSERT INTO products VALUES(8, 'Acer Predator', 'laptops', 1300)")
cursor.execute("INSERT INTO products VALUES(9, 'HP Envy 13', 'laptops', 1400)")
cursor.execute("INSERT INTO products VALUES(10, 'Dell XPS 15', 'laptops', 2500)")

cursor.execute("INSERT INTO products VALUES(11, 'Razor Viper mini', 'accessories', 240)")
cursor.execute("INSERT INTO products VALUES(12, 'Sure SM7B', 'accessories', 800)")
cursor.execute("INSERT INTO products VALUES(13, 'Apple Airpod pro', 'accessories', 500)")
cursor.execute("INSERT INTO products VALUES(14, 'Western Digital 1Tr', 'accessories', 120)")
cursor.execute("INSERT INTO products VALUES(15, 'Mi Powerbank', 'accessories', 100)")


cursor.execute("""CREATE TABLE IF NOT EXISTS orders(user_id INTEGER, product_id INTEGER, quantity INTEGER NOT NULL, total_price INTEGER NOT NULL, created DATE DEFAULT (DATE(CURRENT_DATE)), 
                FOREIGN KEY(user_id) REFERENCES users(user_id), FOREIGN KEY(product_id) REFERENCES products(product_id))""")

connector.commit()


