#########################
# API for the whole app 
#########################

# boilerplate
from flask import Flask, jsonify, request, render_template, redirect
from database_functions import Xray_database
import sqlite3
app = Flask(__name__)
db = Xray_database()
db.create_database_and_table()








## main page route
@app.route('/')
def main(): return render_template('index.html')








## clinic route
from ai_model import AI_pneumonia_check
@app.route('/field_clinic', methods=['GET', 'POST'])
def field_clinic(): 
    if request.method == "GET":
        data = db.fetch_list()
        return render_template('field_clinic.html', data=data)

    if request.method == "POST":
        data = request.form.to_dict()

        return redirect('/field_clinic')

        
        
        
        
        
        
        
## hospital route
@app.route('/hospital', methods=['GET', 'POST'])
def hospital(): 
    if request.method == "GET":
        data = db.fetch_list()
        return render_template('hospital.html', data=data)

    if request.method == "POST":
        data = request.form.to_dict()
        return redirect('/field_clinic')

        
        
        
        
        
        
        
## end of file
if __name__ == '__main__':
    app.run(debug=True, port=5000)