import sqlite3
from typing import List

def bubble_sort(arr: List[int]) -> List[int]:
    """
    Perform bubble sort on the input array
    
    Args:
        arr: List of integers to sort
        
    Returns:
        Sorted list of integers
    """
    n = len(arr)
    # Create a copy of the array to avoid modifying the original
    result = arr.copy()
    
    for i in range(n):
        # Flag to optimize if no swaps occur in a pass
        swapped = False
        
        for j in range(0, n - i - 1):
            if result[j] > result[j + 1]:
                # Swap elements
                result[j], result[j + 1] = result[j + 1], result[j]
                swapped = True
        
        # If no swaps occurred in this pass, array is sorted
        if not swapped:
            break
            
    return result

def create_connection():
    """Create a connection to SQLite database"""
    conn = sqlite3.connect('sorted_arrays.db')
    return conn

def store_sorted_array(original: List[int], sorted_array: List[int]):
    """
    Store original and sorted arrays in database
    
    Args:
        original: Original unsorted array
        sorted_array: Array after bubble sort
    """
    conn = create_connection()
    cursor = conn.cursor()
    
    # Create table if it doesn't exist
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS sorting_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        original_array TEXT,
        sorted_array TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # Convert arrays to strings for storage
    original_str = ','.join(map(str, original))
    sorted_str = ','.join(map(str, sorted_array))
    
    # Insert into database
    cursor.execute(
        "INSERT INTO sorting_results (original_array, sorted_array) VALUES (?, ?)",
        (original_str, sorted_str)
    )
    
    conn.commit()
    print(f"Stored in database with ID: {cursor.lastrowid}")
    conn.close()

def main():
    # Example usage
    unsorted_array = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {unsorted_array}")
    
    sorted_array = bubble_sort(unsorted_array)
    print(f"Sorted array: {sorted_array}")
    
    # Store in database
    store_sorted_array(unsorted_array, sorted_array)
    
    # Retrieve and display stored data
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sorting_results ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    print(f"Retrieved from database: ID={row[0]}, Original={row[1]}, Sorted={row[2]}, Time={row[3]}")
    conn.close()

if __name__ == "__main__":
    main()