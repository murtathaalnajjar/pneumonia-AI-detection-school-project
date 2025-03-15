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

#
#
# boilerplate start
from flask import Flask, jsonify, request
import sqlite3; from pages import *
app = Flask(__name__)
# boilerplate end
#
#







# main page
@app.route('/')
def main():
    return """ \
        <a href="/field_clinic" target="_blank"><button>Field clinic / Pop-upclinic</button></a>
        <a href="hospital" target="_blank"><button>Hospital</button></a>
     """







# field clinc page
@app.route('/field_clinic')
def field_clinic():
    return """<h1>LIST</h1>"""








# hospital page
@app.route('/hospital')
def hospital():
    return """<h1>LIST</h1>"""







@app.route('/list')
def list(): # TODO: finish this
    return jsonify({"data": "data"})







if __name__ == '__main__':
    app.run(debug=True, port=5000)