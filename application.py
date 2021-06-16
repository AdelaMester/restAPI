from flask import Flask, request, jsonify
import os
import sqlite3
from flask_restx import Api, Resource, reqparse

# Configure application and Api
app = Flask(__name__)
api = Api(app, version='1.0', title='Exscentia API',description="The v1.0 Compound API")

# Initialize RequestParser to create or update a new compound
parser = reqparse.RequestParser()
parser.add_argument('smiles', location='json', required=True, help='Rate cannot be converted')
parser.add_argument('molecular_weight', location='json', required=True, type= float)
parser.add_argument('ALogP', location='json', required=True,  type= float)
parser.add_argument('molecular_formula', location='json', required=True)
parser.add_argument('num_rings', location='json', required=True, type= int)
parser.add_argument('image', location='json', required=True)


# Initialize RequestParser to create or update a new assay_result
parserUpdate = reqparse.RequestParser()
parserUpdate.add_argument('result_id', location='json', required=True, help='Rate cannot be converted', type= int)
parserUpdate.add_argument('target', location='json', required=True)
parserUpdate.add_argument('result', location='json', required=True)
parserUpdate.add_argument('operator', location='json', required=True)
parserUpdate.add_argument('value', location='json', required=True, type= int)
parserUpdate.add_argument('unit', location='json', required=True)


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


    @api.expect(parser)
    def post(self, num):

        """Creates a compound"""

        args = parser.parse_args()
        print(args)
        compound_id = num
        smiles = args['smiles']
        molecular_weight = args['molecular_weight']
        ALogP = args['ALogP']
        molecular_formula = args['molecular_formula']
        num_rings = args['num_rings']
        image = args['image']

        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO compounds (compound_id, smiles, molecular_weight, ALogP, molecular_formula, num_rings, image) VALUES (?,?,?,?,?,?,?)", (compound_id, smiles, molecular_weight, ALogP, molecular_formula, num_rings, image))
        conn.commit()
        print("New compound created")
        return jsonify("Insert done")


    @api.expect(parser)
    def put(self, num):

        """Updates the details for the specified compound_id"""

        args = parser.parse_args()
        compound_id = num
        smiles = args['smiles']
        molecular_weight = args['molecular_weight']
        ALogP = args['ALogP']
        molecular_formula = args['molecular_formula']
        num_rings = args['num_rings']
        image = args['image']

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


    @api.expect(parserUpdate)
    def post(self,num):

        """Creates an assay_result for the specified compound_id"""

        args = parserUpdate.parse_args()
        print(args)
        compound_id = num
        result_id = args['result_id']
        target = args['target']
        result = args['result']
        operator = args['operator']
        value = args['value']
        unit = args['unit']

        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("INSERT INTO assay_results (compound_id, result_id, target, result, operator, value, unit) VALUES (?,?,?,?,?,?,?)", (compound_id, result_id, target, result, operator, value, unit))
        conn.commit()
        print("New compound created")
        return jsonify("Insert done")


    @api.expect(parserUpdate)
    def put(self, num):

        """Updates the details for assay_results of the specified compound_id"""


        args = parserUpdate.parse_args()
        print(args)
        compound_id = num
        result_id = args['result_id']
        target = args['target']
        result = args['result']
        operator = args['operator']
        value = args['value']
        unit = args['unit']

        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("UPDATE assay_results SET target=?, result=?, operator=?, value=?, unit=? WHERE compound_id=? AND result_id=?", (target, result, operator, value, unit, num, result_id))
        conn.commit()
        conn.close()
        return jsonify("Update done")

    def delete(self, num):

        """DELETE assay_result data for the specified compound_id"""

        compound_id = num
        conn = sqlite3.connect('json.db')
        print ("Opened database successfully")

        cursor = conn.cursor()
        cursor.execute("DELETE FROM compounds WHERE compound_id=?", (compound_id,))
        cursor.execute("DELETE FROM assay_results WHERE compound_id=?", (compound_id,))
        conn.commit()
        conn.close()
        return jsonify("Deleted")
