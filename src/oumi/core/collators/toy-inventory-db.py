import sqlite3

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('toy_inventory.db')
cursor = conn.cursor()

# Create a table for the toy inventory
cursor.execute('''
CREATE TABLE IF NOT EXISTS toys (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL
)
''')

# Function to add a toy to the inventory
def add_toy(name, category, quantity, price):
    cursor.execute('''
    INSERT INTO toys (name, category, quantity, price)
    VALUES (?, ?, ?, ?)
    ''', (name, category, quantity, price))
    conn.commit()

# Function to get all toys from the inventory
def get_all_toys():
    cursor.execute('SELECT * FROM toys')
    return cursor.fetchall()

# Function to update the quantity of a toy
def update_toy_quantity(toy_id, quantity):
    cursor.execute('''
    UPDATE toys
    SET quantity = ?
    WHERE id = ?
    ''', (quantity, toy_id))
    conn.commit()

# Function to delete a toy from the inventory
def delete_toy(toy_id):
    cursor.execute('''
    DELETE FROM toys
    WHERE id = ?
    ''', (toy_id,))
    conn.commit()

# Example usage
add_toy('Toy Car', 'Vehicles', 100, 9.99)
add_toy('Doll', 'Figures', 50, 14.99)

toys = get_all_toys()
print("All toys in inventory:", toys)

update_toy_quantity(1, 120)
delete_toy(2)

toys = get_all_toys()
print("All toys in inventory after update and delete:", toys)

# Close the connection
conn.close()