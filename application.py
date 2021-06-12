from flask import Flask, request, jsonify
import os
import sqlite3

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/compounds", methods = ["GET"])
def index():

    if request.method == "GET":

        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM compounds")
        allCompounds = cursor.fetchall()
        result = []
        column = [desc[0] for desc in cursor.description]
        for compound in allCompounds:
            compound = dict(zip(column, compound))
            result.append(compound)
        conn.close()
        print(result)
        return jsonify(result)


#@app.route("/getCompounds/<int:num>/", methods = ["GET"])
#def index():
