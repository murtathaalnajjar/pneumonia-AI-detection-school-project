#########################
# API for the whole app 
#########################
# GET /main        -> HTML
# GET /popupClinic -> HTML
# GET /hospital    -> HTML
# GET /list        -> JSON data
# POST xray record to database
# POST prescription record to database
######################################
# # AI in the app? or in python?
#
#
#
# boilerplate start
from flask import Flask, jsonify, request, render_template, redirect
import sqlite3
app = Flask(__name__)
# boilerplate end
#
#
#
# create the database
conn = sqlite3.connect('database.db')
cursor = conn.cursor()
cursor.execute("""

CREATE TABLE IF NOT EXISTS patients (

    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    age INTEGER,
    symptoms TEXT,
    img BLOB,
    datetime_taken TEXT,
    Checked TEXT,
    algorithm_pneumonia_detected TEXT,
    actual_pneumonia_result TEXT,
    prescribed TEXT
)

""")
# # # # # # # # # # #
#
#
#



fakedata = [{"name": "John Doe", "age": 25, "symptoms": "Cough, Fever", "img": "image.jpg"},
{"name": "Jane Doe", "age": 30, "symptoms": "Cough, Fever", "img": "image.jpg"},
{"name": "Jim Doe", "age": 35, "symptoms": "Cough, Fever", "img": "image.jpg"}]



#
#
# main page route
@app.route('/')
def main(): return render_template('index.html')
# # # # # # # # #
#
#

#
#
# popup clinic route
@app.route('/field_clinic', methods=['GET', 'POST'])
def field_clinic(): 
    if request.method == "GET":
        # TODO: replace fakedata with actual data 
        return render_template('field_clinic.html', data=fakedata)

    if request.method == "POST":
        # TODO: 
        # get data from form
        # add patient to database
        return redirect('/field_clinic')
# # # # # # # # #
#
#

#
#
# hospital route
@app.route('/hospital', methods=['GET', 'POST'])
def hospital(): 
    if request.method == "GET":
        return render_template('hospital.html', data=fakedata)

    if request.method == "POST":
        # TODO: PRESCRIPTION to database
        return redirect('/field_clinic')
# # # # # # # # #
#
#

#
#
# end of file
if __name__ == '__main__':
    app.run(debug=True, port=5000)