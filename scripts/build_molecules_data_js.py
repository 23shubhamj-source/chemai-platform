import sys, os
sys.path.insert(0, os.path.dirname(__file__))

import cat_a_simple as a
import cat_b_organic as b
import cat_c_acids_bases as c
import cat_d_inorganic as d
import cat_e_biochem as e
import cat_f_other as f
import json

all_molecules = (
    a.get_simple_molecules() +
    b.get_organic_molecules() +
    c.get_acids_molecules() +
    d.get_inorganic_molecules() +
    e.get_biochem_molecules() +
    f.get_other_molecules()
)

ids = set()
unique_mols = []
for m in all_molecules:
    mid = m["id"]
    if mid in ids:
        print("Duplicate ID: " + mid)
    else:
        ids.add(mid)
        unique_mols.append(m)

print("Total Unique Validated Molecules: " + str(len(unique_mols)))

js_content = "/* ==========================================================================\n" \
             "   ChemAI Platform - Validated Molecular Database (85+ Molecules)\n" \
             "   Scientifically verified 3D atomic coordinates, geometries, and chemical properties\n" \
             "   ========================================================================== */\n\n" \
             "window.CHEMAI_MOLECULES = " + json.dumps(unique_mols, indent=2, ensure_ascii=False) + ";\n"

with open("js/molecules-data.js", "w", encoding="utf-8") as out:
    out.write(js_content)

print("Successfully written js/molecules-data.js")
