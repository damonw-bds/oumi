import sqlite3
from datetime import date

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('employee_vacation_schedule.db')
cursor = conn.cursor()

# Create a table to store the vacation schedule
cursor.execute('''
CREATE TABLE IF NOT EXISTS vacation_schedule (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    employee_name TEXT NOT NULL,
    start_date TEXT NOT NULL,
    end_date TEXT NOT NULL
)
''')

# Function to add a vacation schedule
def add_vacation_schedule(employee_name: str, start_date: date, end_date: date):
    cursor.execute('''
    INSERT INTO vacation_schedule (employee_name, start_date, end_date)
    VALUES (?, ?, ?)
    ''', (employee_name, start_date.isoformat(), end_date.isoformat()))
    conn.commit()

# Example usage
add_vacation_schedule('John Doe', date(2025, 6, 1), date(2025, 6, 15))
add_vacation_schedule('Jane Smith', date(2025, 7, 10), date(2025, 7, 20))

# Query the database to verify the entries
cursor.execute('SELECT * FROM vacation_schedule')
rows = cursor.fetchall()
for row in rows:
    print(row)

# Close the connection
conn.close()