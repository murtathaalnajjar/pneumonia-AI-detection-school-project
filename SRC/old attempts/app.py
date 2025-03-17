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
# boilerplate start
from flask import Flask, jsonify, request
app = Flask(__name__)
# boilerplate end
#
#
#
#
# API names
rout2 = "field_clinic"
rout3 = "hospital"
rout4 = "get_patient_list"
# # # # # #
#
#
#







# main page
@app.route('/')
def main():
    return """ \
        <a href="/field_clinic" target="_blank"><button>Field clinic / Pop-upclinic</button></a>
        <a href="hospital" target="_blank"><button>Hospital</button></a>
     """







# field clinic page
@app.route('/'+rout2)
def field_clinic():
    return """

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
    <form action="/submit-form" method="post" enctype="multipart/form-data">
        <label for="name">Name:</label><br>
        <input type="text" id="name" name="name" required><br><br>
        
        <label for="age">Age:</label><br>
        <input type="number" id="age" name="age" required><br><br>
        
        <label for="symptoms">Symptoms:</label><br>
        <textarea id="symptoms" name="symptoms" required></textarea><br><br>
        
        <label for="image">Upload Image:</label><br>
        <input type="file" id="image" name="image" accept="image/*" required><br><br>
        
        <input type="submit" value="Submit">
    </form>
    <script>
        fetch('/get_patiet_list')
        .then(response => response.json())
        .then(response => console.log(response))
    </script>
    <ul>
    </ul>
</body>
</html>



"""








# hospital page
@app.route('/+'+rout3)
def hospital():
    return """<h1>LIST</h1>"""







@app.route('/'+rout4)
def list(): # TODO: finish this
    return 
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






if __name__ == '__main__':
    app.run(debug=True, port=5000)