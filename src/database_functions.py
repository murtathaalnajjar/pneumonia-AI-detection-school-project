import sqlite3


class Xray_database:

    def create_database_and_table():
        conn = sqlite3.connect('database.db'); cursor = conn.cursor()
        cursor.execute("""

            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                datetime_taken TEXT,

                full_name TEXT,
                age INTEGER,
                symptoms TEXT,
                img BLOB,

                Checked TEXT,
                algorithm_pneumonia_detected TEXT,
                actual_pneumonia_result TEXT,
                prescribed TEXT
            )

        """); conn.commit()

    def fetch_list():
        # TODO: FETCH DATA FROM DATABASE AS A LIST OF OBJECTS
        return "list of objects"
    
    def add_record(data): 
        pass # TODO:
    
    def prescribe_for_record(record, data):
        pass # TODO: