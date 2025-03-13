import sqlite3

# Define the database file
db_file = 'contacts.db'

# Connect to the database (it will be created if it doesn't exist)
conn = sqlite3.connect(db_file)
cursor = conn.cursor()

# Create the contacts table
cursor.execute('''
CREATE TABLE IF NOT EXISTS contacts (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL,
    phone TEXT
)
''')

# Function to add a contact to the database
def add_contact(first_name, last_name, email, phone=None):
    cursor.execute('''
    INSERT INTO contacts (first_name, last_name, email, phone)
    VALUES (?, ?, ?, ?)
    ''', (first_name, last_name, email, phone))
    conn.commit()

# Example usage
add_contact('John', 'Doe', 'john.doe@example.com', '123-456-7890')
add_contact('Jane', 'Smith', 'jane.smith@example.com')

# Query and print all contacts
cursor.execute('SELECT * FROM contacts')
for row in cursor.fetchall():
    print(row)

# Close the connection
conn.close()