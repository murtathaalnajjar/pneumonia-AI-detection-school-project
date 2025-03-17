#################################   
#                               #
# data base schema thats all    # 
#                               #
#################################
# id	                        INTEGER PRIMARY KEY AUTOINCREMENT
# full_name                     TEXT
# age	                        INTEGER
# symptoms	                    TEXT
# img	                        BLOB (find how to convert img to blob)
# datetime_taken	            TEXT
# Checked	                    TEXT (yes/no) (sqlite dosnt have boolean)
# algorithm_pneumonia_detected	TEXT (yes/no)
# actual_pneumonia_result	    TEXT (yes/no)
# prescribed                    TEXT
#################################





#
#
# boilerplate start
import sqlite3
con = sqlite3.connect("database.db")
c = con.cursor()
# boilerplate end
#
#


table_name = "chest_xray"
schema = {
    "id": "INTEGER PRIMARY KEY AUTOINCREMENT",
    "full_name": "TEXT",
    "age": "INTEGER",
    # "symptoms TEXT",
    # "img BLOB",
    # "datetime_taken TEXT",
    # "Checked TEXT",
    # "algorithm_pneumonia_detected TEXT",
    # "actual_pneumonia_result TEXT",
    # "prescribed TEXT"
}
columns = ""
for column in schema:
    columns += f"{column} {schema[column]}, "
columns_values = ""
for column in schema:
    columns_values += f"{column}, "


print(columns_values)



def drop_table(): c.execute( f"DROP TABLE IF EXISTS {table_name}")
def create_the_only_table():
    c.execute( f"CREATE TABLE IF NOT EXISTS {table_name} ({values})" )




def insert_patient(list_of_values):
    values = ""
    for value in list_of_values:
        values += f"'{value}', "

    query_string = f"INSERT INTO {table_name} VALUES ({values})"
    c.execute(query_string)
    


# drop_table()
# create_the_only_table()

# c.execute(f"INSERT INTO {table_name} (full_name, age) VALUES ('John Doe', 23)")