from flask import Flask, request, jsonify
import os
import sqlite3
#from werkzeug.utils import cached_property
from flask_restplus import Api, Resource


# Configure application and Api
app = Flask(__name__)
api = Api(app)
#namespace = api.namespace('compounds', description = 'compounds operations')
#namespace=Namespace('hello_world','Hello World related operations')



@api.route('/compounds')
class Compounds(Resource):
    def get(self):

        """Returns the list of compounds"""

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

    def post(self):

        """Creates a compound"""

        compound_id = request.json['compound_id']
        smiles = request.json['smiles']
        molecular_weight = request.json['molecular_weight']
        ALogP = request.json['ALogP']
        molecular_formula = request.json['molecular_formula']
        num_rings = request.json['num_rings']
        image = request.json['image']

        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO compounds (compound_id, smiles, molecular_weight, ALogP, molecular_formula, num_rings, image) VALUES (?,?,?,?,?,?,?)", (compound_id, smiles, molecular_weight, ALogP, molecular_formula, num_rings, image))
        allCompounds = cursor.fetchall()
        conn.commit()
        print("New compound created")
        return jsonify("Insert done")


@api.route("/compound/<int:num>")
@api.doc(params = {'num': 'A compound id'})
class Compounds_id(Resource):
    def get(self, num):

        """Returns the details for the specified compound_id"""

        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM compounds WHERE compound_id = ?", (num,))
        compound_id = cursor.fetchall()
        result = []
        column = [desc[0] for desc in cursor.description]
        for compound in compound_id:
            compound = dict(zip(column, compound))
            result.append(compound)
        conn.close()
        print(result)
        return jsonify(result)


    def put(self, num):

        """Updates the details for the specified compound_id"""

        compound_id = num
        smiles = request.json['smiles']
        molecular_weight = request.json['molecular_weight']
        ALogP = request.json['ALogP']
        molecular_formula = request.json['molecular_formula']
        num_rings = request.json['num_rings']
        image = request.json['image']

        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("UPDATE compounds SET smiles=?, molecular_weight=?, ALogP=?, molecular_formula=?, num_rings=?, image=? WHERE compound_id=?", (smiles, molecular_weight, ALogP, molecular_formula, num_rings, image, num))
        conn.commit()
        conn.close()
        return jsonify("Update done")


    def delete(self, num):

        """DELETE the details for the specified compound_id"""

        compound_id = num
        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("DELETE FROM compounds WHERE compound_id=?", (compound_id,))
        cursor.execute("DELETE FROM assay_results WHERE compound_id=?", (compound_id,))
        conn.commit()
        conn.close()
        return jsonify("Deleted")


@api.route("/compound/<int:num>/assay_results")
@api.doc(params = {'num': 'A compound id'})
class Compounds_id(Resource):
    def get(self, num):

        """Returns the list of assay_results for the specified compound_id"""

        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("SELECT * FROM assay_results WHERE compound_id = ?", (num,))
        allAssayResults = cursor.fetchall()
        result = []
        column = [desc[0] for desc in cursor.description]
        for assay_result in allAssayResults:
            assay_result = dict(zip(column, assay_result))
            result.append(assay_result)
        conn.close()
        print(result)
        return jsonify(result)





