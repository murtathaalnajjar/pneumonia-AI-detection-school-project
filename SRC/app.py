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







# boilerplate start
from flask import Flask, jsonify, request
import sqlite3; from pages import *
app = Flask(__name__)
# boilerplate end







if __name__ == '__main__':
    app.run(debug=True, port=5000)