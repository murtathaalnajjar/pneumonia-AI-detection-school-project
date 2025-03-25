import sqlite3
from datetime import datetime


## datetime without milliseconds function taken from stackoverflow cuz i dont have time
def now(): return datetime.now().replace(microsecond=0, second=0)



class Xray_database:

    def __init__(self):
        self.conn = sqlite3.connect('database.db', check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.table_name = "patients"

    def create_database_and_table(self):
        self.cursor.execute(f"""

            CREATE TABLE IF NOT EXISTS {self.table_name} (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                datetime TEXT,

                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                symptoms TEXT NOT NULL,
                img BLOB NOT NULL,

                algorithm_result TEXT,
                actual_result TEXT,
                prescribed TEXT
            )

        """); 
        self.conn.commit()

    def fetch_list(self):
        rows = self.cursor.execute(f"SELECT * FROM {self.table_name}")
        data = rows.fetchall()
        return data
    
    def add_record(self, name, age, symptoms, img): 
        try:
            self.cursor.execute(f"INSERT INTO {self.table_name} (datetime, name, age, symptoms, img, algorithm_result) VALUES (?, ?, ?, ?, ?, ?)",
                                (now(), name, age, symptoms, img, 'no')) # TODO: change the 'no'
            self.conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Failed to add record: {e}")
    
    def prescribe_for_record(self, record_id, actual_result, prescribed):
        try:
            self.cursor.execute(f"UPDATE {self.table_name} SET actual_result = ?, prescribed = ? WHERE id = ?",
                                (actual_result, prescribed, record_id))
            self.conn.commit()
        except sqlite3.Error as e:
            raise Exception(f"Failed to update record: {e}")

