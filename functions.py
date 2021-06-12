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
        field["image"]
    ))

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

#print(rows)
print(rows2)


