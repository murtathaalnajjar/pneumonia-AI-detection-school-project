#########################
# API for the whole app 
#########################

# boilerplate
from flask import Flask, jsonify, request, render_template, redirect
from database_functions import Xray_database;
import sqlite3; app = Flask(__name__); db = Xray_database()
db.create_database_and_table()








## main page route
@app.route('/')
def main(): return render_template('index.html')








## clinic route
from ai_model import AI_pneumonia_check
@app.route('/clinic', methods=['GET', 'POST'])
def clinic(): 
    if request.method == "GET":
        data = db.fetch_list()
        return render_template('clinic.html', data=data)

    if request.method == "POST":
        request
        # TODO:
        # extract image from request
        # convert image to blob
        # add record to database
        db.add_record(...)
        return redirect('/clinic')

        
        
        
        
        
        
        
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

        
        
        
        
        
        
        
## end of file
if __name__ == '__main__':
    app.run(debug=True, port=5000)