import sqlite3
class BaseModel:
    db_name = 'inventory.db'
    @classmethod
    def execute_query(cls, query, params=()):
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor
    @classmethod
    def fetch_query(cls, query, params=()):
        with sqlite3.connect(cls.db_name) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
# Initialize the database and create tables
def initialize_db():
    queries = [
        '''
        CREATE TABLE IF NOT EXISTS category (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS supplier (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            contact_info TEXT NOT NULL
        )
        ''',
        '''
        CREATE TABLE IF NOT EXISTS product (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            quantity INTEGER NOT NULL,
            category_id INTEGER,
            supplier_id INTEGER,
            FOREIGN KEY (category_id) REFERENCES category(id),
            FOREIGN KEY (supplier_id) REFERENCES supplier(id)
        )
        '''
    ]
    for query in queries:
        BaseModel.execute_query(query)
if __name__ == '__main__':
    initialize_db()

