import sqlite3

conn = sqlite3.connect('db.sqlite3')
cursor = conn.cursor()

# # Compute average rating for menu item
# cursor.execute("UPDATE api_menu SET avg_rating = COALESCE((SELECT ROUND(AVG(stars)) FROM api_rating WHERE api_rating.menu_id_id = api_menu.id), 0)")

# # Compute average rating for canteen
# cursor.execute("UPDATE api_canteen SET avg_rating = COALESCE((SELECT ROUND(AVG(avg_rating)) FROM api_menu WHERE api_menu.canteen_id_id = api_canteen.id AND avg_rating!=0), 0)")

# Commit the changes
conn.commit()

# Close the connection
conn.close()
