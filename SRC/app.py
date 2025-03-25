#########################
# API for the whole app 
#########################

# the following was done with AI
# converting a blob into base64

# boilerplate
from flask import Flask, jsonify, request, render_template, redirect
from database_functions import Xray_database;
import sqlite3; app = Flask(__name__); db = Xray_database()
db.create_database_and_table()
import base64

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## main page route
@app.route('/')
def main(): return render_template('index.html')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## clinic route
from ai_model import AI_pneumonia_check
@app.route('/clinic', methods=['GET', 'POST'])
def clinic():
    if request.method == "GET":
        fetch = db.fetch_list()
        data = []
        for record in fetch:
            img_data = base64.b64encode(record[5]).decode('utf-8') if record[5] else None
            data.append(record + (img_data,))
        return render_template('clinic.html', data=data)

    if request.method == "POST":
        name = request.form.get('name')
        age = request.form.get('age')
        symptoms = request.form.get('symptoms')
        img = request.files.get('xray')

        if img:
            img_data = img.read()
            db.add_record(name, age, symptoms, img_data)
        
        return redirect('/clinic')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## hospital route
@app.route('/hospital', methods=['GET', 'POST'])
def hospital(): 
    if request.method == "GET":
        data = db.fetch_list()
        return render_template('hospital.html', data=data)

    if request.method == "POST":
        data = request
        record_number = 0
        actual_pneumonia_result = '...' # 'yes' of True, 'no' if False
        prescribed = "..."
        db.prescribe_for_record(record_number, )
        return redirect('/clinic')

# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # #

## end of file
if __name__ == '__main__':
    app.run(debug=True, port=5000)