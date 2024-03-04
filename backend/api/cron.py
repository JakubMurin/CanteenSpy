import sqlite3
from datetime import datetime, timedelta

# Get the current date
today = datetime.now()

# Check if today is Saturday (assuming Monday is 0 and Sunday is 6)
if today.weekday() == 6:
    # Connect to your SQLite database
    conn = sqlite3.connect('db.sqlite3')
    cursor = conn.cursor()

    # Fetch data from the table
    cursor.execute("SELECT id, day FROM api_menu")
    rows = cursor.fetchall()

    # Add days to the date column
    for row in rows:
        date_value = datetime.strptime(row[1], '%Y-%m-%d')  # Assuming the date format is 'YYYY-MM-DD'
        new_date = date_value + timedelta(days=6)  # Add 5 days, modify as needed
        cursor.execute("UPDATE api_menu SET day = ? WHERE id = ?", (new_date.strftime('%Y-%m-%d'), row[0]))

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()
