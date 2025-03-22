import sqlite3


class Xray_database:

    def __init__(self):
        pass

    def create_database_and_table(self):
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

    def fetch_list(self):
        # TODO: FETCH DATA FROM DATABASE AS A LIST OF OBJECTS
        return "list of objects"
    
    def add_record(self, full_name, age, symptoms, img): 
        pass # TODO:
    
    def prescribe_for_record(self,record, actual_pneumonia_result, prescribed):
        pass # TODO:


