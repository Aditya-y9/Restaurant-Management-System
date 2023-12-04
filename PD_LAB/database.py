import sqlite3


def create_table():
    # Connect to database
    conn = sqlite3.connect('products.db')
    # Create cursor object
    cur = conn.cursor()
    # Execute SQL command
    cur.execute('''CREATE TABLE IF NOT EXISTS Products (id TEXT PRIMARY KEY, name TEXT, in_stock INTEGER)''')
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


def fetch_products():
    # Connect to database
    conn = sqlite3.connect('products.db')
    # Create cursor object
    cur = conn.cursor()
    # Execute SQL command
    cur.execute("SELECT * FROM Products")
    # Fetch data
    Products = cur.fetchall()
    # Close connection
    conn.close()
    return Products


def insert_product(id, name, in_stock):
    # Connect to database
    conn = sqlite3.connect('products.db')
    # Create cursor object
    cur = conn.cursor()
    # Execute SQL command
    cur.execute("INSERT INTO Products VALUES (?, ?, ?)", (id, name, in_stock))
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

def delete_product(id):
    # Connect to database
    conn = sqlite3.connect('products.db')
    # Create cursor object
    cur = conn.cursor()
    # Execute SQL command
    cur.execute("DELETE FROM Products WHERE id=?", (id,))
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()


def update_product(new_name, new_in_stock, id):
    # Connect to database
    conn = sqlite3.connect('products.db')
    # Create cursor object
    cur = conn.cursor()
    # Execute SQL command
    cur.execute("UPDATE Products SET name=?, in_stock=? WHERE id=?", (new_name, new_in_stock, id))
    # Commit changes
    conn.commit()
    # Close connection
    conn.close()

def id_exists(id):
    # Connect to database
    conn = sqlite3.connect('products.db')
    # Create cursor object
    cur = conn.cursor()
    # Execute SQL command
    cur.execute("SELECT COUNT(*) FROM Products WHERE id=?", (id,))
    # Fetch data
    Products = cur.fetchone()
    # Close connection
    conn.close()
    if len(Products) > 0:
        return True
    else:
        return False
    
create_table()
