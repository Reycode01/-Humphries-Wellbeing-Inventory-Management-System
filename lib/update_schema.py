import sqlite3

def add_price_column():
    connection = sqlite3.connect('your_database_file.db') 
    cursor = connection.cursor()
    cursor.execute("ALTER TABLE product ADD COLUMN price REAL")
    connection.commit()
    connection.close()

if __name__ == "__main__":
    add_price_column()
