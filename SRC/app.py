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
# # # # # # # # # # #
#
#

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
def fetch_list():
    # TODO: FETCH DATA FROM DATABASE AS A LIST OF OBJECTS
    return "list of objects"
# # # # # # # # #
#
#

#
#
# popup clinic route
@app.route('/field_clinic', methods=['GET', 'POST'])
def field_clinic(): 
    if request.method == "GET":

        data = fetch_list()

        return render_template('field_clinic.html', data="non")

    if request.method == "POST":
        data = request.form.to_dict()

        # TODO: 
        # get the image from the form
        # run the image through the AI model
        # write an sql query to insert the data into the database
        # datetime(date.now), name, age, symptoms, image, pneumonia_detected(yes/no)


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
        data = fetch_list()
        return render_template('hospital.html', data="none")

    if request.method == "POST":
        data = request.form.to_dict()
        # TODO:
        # get row number
        # edit the row
        # add: Checked(yes), actual_pneumonia_result, prescribed
        return redirect('/field_clinic')
# # # # # # # # #
#
#

#
#
# end of file
if __name__ == '__main__':
    app.run(debug=True, port=5000)