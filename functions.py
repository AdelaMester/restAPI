import json
import io

with io.open("compounds.json", 'r', encoding='utf-8-sig') as data:
    dictionary = json.load(data)

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
        field["image"],
        field["assay_results"]
    ))


print(rows)

