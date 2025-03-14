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







# boilerplate start
import sqlite3
con = sqlite3.connect("database.db")
c = con.cursor()
# boilerplate end







c.execute (
"CREATE TABLE IF NOT EXISTS chest_xray "
"(id                              INTEGER PRIMARY KEY AUTOINCREMENT,"
" full_name                       TEXT,"
" age	                          INTEGER,"
" symptoms	                      TEXT,"
" img	                          BLOB,"
" datetime_taken 	              TEXT,"
" Checked	                      TEXT,"
" algorithm_pneumonia_detected	  TEXT,"
" actual_pneumonia_result	      TEXT,"
" prescribed                      TEXT)"
)







c.execute("select * from chest_xray")
print(c.fetchall())