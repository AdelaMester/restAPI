import json
import io
import sqlite3

with io.open("compounds.json", 'r', encoding='utf-8-sig') as data:
    dictionary = json.load(data)

conn = sqlite3.connect('json.db')
print ("Opened database successfully")

rows = []
rows2 = []
for field in dictionary:
    rows.append((
        field["compound_id"],
        field["smiles"],
        field["molecular_weight"],
        field["ALogP"],
        field["molecular_formula"],
        field["num_rings"],
        field["image"]
    ))

    cursor = conn.cursor()
    cursor.execute("INSERT INTO compounds (compound_id, smiles, molecular_weight, ALogP, molecular_formula, num_rings, image) VALUES (?,?,?,?,?,?,?)", (field["compound_id"], field["smiles"], field["molecular_weight"], field["ALogP"], field["molecular_formula"], field["num_rings"], field["image"]))
    print("Insert done")
    conn.commit()

    for assay in range(len(field["assay_results"])):
        rows2.append((
            field["compound_id"],
            field["assay_results"][assay].get("result_id"),
            field["assay_results"][assay].get("target"),
            field["assay_results"][assay].get("result"),
            field["assay_results"][assay].get("operator"),
            field["assay_results"][assay].get("value"),
            field["assay_results"][assay].get("unit")
        ))

        cursor = conn.cursor()
        cursor.execute("INSERT INTO assay_results (compound_id, result_id, target, result, operator, value, unit) VALUES (?,?,?,?,?,?,?)", (field["compound_id"], field["assay_results"][assay].get("result_id"), field["assay_results"][assay].get("target"), field["assay_results"][assay].get("result"), field["assay_results"][assay].get("operator"), field["assay_results"][assay].get("value"), field["assay_results"][assay].get("unit")))
        print("Insert done")
        conn.commit()

#print(rows)
#print(rows2)






