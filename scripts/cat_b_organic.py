# Category B: Organic Molecules (Part 1)
def get_organic_part1():
    return [
        {
            "id": "methanol", "name": "Methanol", "formula": "CH₃OH", "commonName": "Wood Alcohol",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "32.042 g/mol",
            "geometry": "Tetrahedral at C, Bent at O", "bondAngles": "C-O-H 108.9°, H-C-H 109.5°",
            "bondTypes": "Polar C-O and O-H σ bonds + 3 C-H σ bonds", "numAtoms": 6, "numBonds": 5,
            "hybridization": "sp³", "polarity": "Polar (μ = 1.70 D)",
            "physicalProps": "Colorless volatile liquid; mp -97.6°C, bp 64.7°C; density 0.792 g/cm³; miscible with water.",
            "chemicalProps": "Oxidized to toxic formaldehyde and formic acid in the liver by alcohol dehydrogenase.",
            "uses": "Feedstock for formaldehyde, acetic acid, biodiesel production, solvent, racing fuel.",
            "facts": "Methanol poisoning damages the optic nerve, causing irreversible blindness from formic acid accumulation.",
            "atoms": [{"el":"C","x":-0.05,"y":0.0,"z":0.0},{"el":"O","x":1.35,"y":0.0,"z":0.0},{"el":"H","x":1.70,"y":0.90,"z":0.0},{"el":"H","x":-0.45,"y":1.02,"z":0.0},{"el":"H","x":-0.45,"y":-0.51,"z":0.88},{"el":"H","x":-0.45,"y":-0.51,"z":-0.88}],
            "bonds": [[0,1,1],[1,2,1],[0,3,1],[0,4,1],[0,5,1]]
        },
        {
            "id": "ethanol", "name": "Ethanol", "formula": "C₂H₅OH", "commonName": "Grain Alcohol",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "46.069 g/mol",
            "geometry": "Tetrahedral at C, Bent at O", "bondAngles": "C-C-O 107.5°, C-O-H 104.8°",
            "bondTypes": "C-C, C-O, O-H, C-H σ bonds", "numAtoms": 9, "numBonds": 8,
            "hybridization": "sp³", "polarity": "Polar (μ = 1.69 D)",
            "physicalProps": "Clear colorless liquid; mp -114.1°C, bp 78.37°C; density 0.789 g/cm³; miscible with water.",
            "chemicalProps": "Dehydrates to ethylene with conc. H₂SO₄; oxidized to acetaldehyde and acetic acid.",
            "uses": "Biofuel (E10/E85), pharmaceutical solvent, alcoholic beverages, hand sanitizer antiseptic.",
            "facts": "Fermentation of ethanol by yeasts is one of the earliest chemical technologies harnessed by humanity.",
            "atoms": [{"el":"C","x":-0.75,"y":-0.2,"z":0.0},{"el":"C","x":0.75,"y":-0.2,"z":0.0},{"el":"O","x":1.4,"y":1.0,"z":0.0},{"el":"H","x":2.3,"y":0.8,"z":0.0},{"el":"H","x":-1.1,"y":-0.7,"z":0.89},{"el":"H","x":-1.1,"y":-0.7,"z":-0.89},{"el":"H","x":-1.1,"y":0.8,"z":0.0},{"el":"H","x":1.1,"y":-0.7,"z":0.89},{"el":"H","x":1.1,"y":-0.7,"z":-0.89}],
            "bonds": [[0,1,1],[1,2,1],[2,3,1],[0,4,1],[0,5,1],[0,6,1],[1,7,1],[1,8,1]]
        },
        {
            "id": "propanol", "name": "1-Propanol", "formula": "C₃H₇OH", "commonName": "n-Propyl Alcohol",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "60.096 g/mol",
            "geometry": "Tetrahedral chain", "bondAngles": "C-C-C ~112°, C-O-H ~109°",
            "bondTypes": "C-C, C-O, O-H, C-H σ bonds", "numAtoms": 12, "numBonds": 11,
            "hybridization": "sp³", "polarity": "Polar (μ = 1.68 D)",
            "physicalProps": "Colorless liquid with alcohol aroma; mp -126°C, bp 97.2°C; density 0.803 g/cm³.",
            "chemicalProps": "Primary alcohol; oxidized by PCC to propanal and by KMnO₄ to propionic acid.",
            "uses": "Printing ink solvent, flexographic printing, intermediate in pharmaceutical syntheses.",
            "facts": "Formed as a natural byproduct in fusel oil during the fermentation of grains and potatoes.",
            "atoms": [{"el":"C","x":-1.8,"y":0.2,"z":0.0},{"el":"C","x":-0.5,"y":-0.5,"z":0.0},{"el":"C","x":0.8,"y":0.3,"z":0.0},{"el":"O","x":1.9,"y":-0.5,"z":0.0},{"el":"H","x":2.7,"y":-0.1,"z":0.0},{"el":"H","x":-1.8,"y":0.8,"z":0.9},{"el":"H","x":-1.8,"y":0.8,"z":-0.9},{"el":"H","x":-2.7,"y":-0.4,"z":0.0},{"el":"H","x":-0.5,"y":-1.1,"z":0.9},{"el":"H","x":-0.5,"y":-1.1,"z":-0.9},{"el":"H","x":0.8,"y":0.9,"z":0.9},{"el":"H","x":0.8,"y":0.9,"z":-0.9}],
            "bonds": [[0,1,1],[1,2,1],[2,3,1],[3,4,1],[0,5,1],[0,6,1],[0,7,1],[1,8,1],[1,9,1],[2,10,1],[2,11,1]]
        },
        {
            "id": "acetone", "name": "Acetone", "formula": "CH₃COCH₃", "commonName": "Propan-2-one",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "58.080 g/mol",
            "geometry": "Trigonal planar at carbonyl", "bondAngles": "C-C(=O)-C 116.5°",
            "bondTypes": "C=O double bond, C-C and C-H σ bonds", "numAtoms": 10, "numBonds": 9,
            "hybridization": "sp² carbonyl, sp³ methyls", "polarity": "Polar aprotic (μ = 2.88 D)",
            "physicalProps": "Colorless volatile liquid; mp -94.7°C, bp 56.05°C; density 0.784 g/cm³.",
            "chemicalProps": "Gives positive iodoform test; undergoes aldol condensation; miscible with water and organic solvents.",
            "uses": "Laboratory cleaning solvent, nail polish remover, manufacturing polymethyl methacrylate (Plexiglas).",
            "facts": "Acetone is produced endogenously in the human body during ketosis and diabetic ketoacidosis.",
            "atoms": [{"el":"C","x":0.0,"y":0.2,"z":0.0},{"el":"O","x":0.0,"y":1.4,"z":0.0},{"el":"C","x":-1.3,"y":-0.6,"z":0.0},{"el":"C","x":1.3,"y":-0.6,"z":0.0},{"el":"H","x":-1.3,"y":-1.2,"z":0.9},{"el":"H","x":-1.3,"y":-1.2,"z":-0.9},{"el":"H","x":-2.1,"y":0.1,"z":0.0},{"el":"H","x":1.3,"y":-1.2,"z":0.9},{"el":"H","x":1.3,"y":-1.2,"z":-0.9},{"el":"H","x":2.1,"y":0.1,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1],[0,3,1],[2,4,1],[2,5,1],[2,6,1],[3,7,1],[3,8,1],[3,9,1]]
        },
        {
            "id": "formaldehyde", "name": "Formaldehyde", "formula": "HCHO", "commonName": "Methanal",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "30.026 g/mol",
            "geometry": "Trigonal Planar", "bondAngles": "H-C-H 116.5°, H-C=O 121.8°",
            "bondTypes": "C=O double bond + 2 C-H σ bonds", "numAtoms": 4, "numBonds": 3,
            "hybridization": "sp²", "polarity": "Polar (μ = 2.33 D)",
            "physicalProps": "Colorless pungent gas; mp -92°C, bp -19°C; 37% aqueous solution is formalin.",
            "chemicalProps": "Undergoes Cannizzaro reaction in alkali: 2HCHO + OH⁻ → HCOO⁻ + CH₃OH.",
            "uses": "Production of Bakelite and melamine resins, biological specimen preservation, adhesives.",
            "facts": "Formaldehyde was a key reactant in creating Bakelite in 1907, the world's first fully synthetic plastic.",
            "atoms": [{"el":"C","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.20,"z":0.0},{"el":"H","x":-0.94,"y":-0.58,"z":0.0},{"el":"H","x":0.94,"y":-0.58,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1],[0,3,1]]
        },
        {
            "id": "aceticacid", "name": "Acetic Acid", "formula": "CH₃COOH", "commonName": "Ethanoic Acid / Vinegar",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "60.052 g/mol",
            "geometry": "Trigonal planar at carboxyl", "bondAngles": "O=C-O 122.5°",
            "bondTypes": "C=O, C-O, O-H, C-C, C-H σ bonds", "numAtoms": 8, "numBonds": 7,
            "hybridization": "sp² carboxyl, sp³ methyl", "polarity": "Polar (μ = 1.74 D)",
            "physicalProps": "Colorless liquid with sharp vinegar smell; mp 16.6°C, bp 117.9°C; forms ice-like crystals when cold.",
            "chemicalProps": "Weak acid (Ka = 1.8 × 10⁻⁵, pKa = 4.76); forms cyclic hydrogen-bonded dimers in vapor.",
            "uses": "Household vinegar (5-8%), vinyl acetate monomer for PVA glue, cellulose acetate films.",
            "facts": "Pure water-free acetic acid is called glacial acetic acid because it freezes at a cool room temperature of 16.6°C.",
            "atoms": [{"el":"C","x":0.0,"y":0.1,"z":0.0},{"el":"O","x":0.0,"y":1.3,"z":0.0},{"el":"O","x":1.2,"y":-0.6,"z":0.0},{"el":"H","x":1.9,"y":-0.1,"z":0.0},{"el":"C","x":-1.2,"y":-0.8,"z":0.0},{"el":"H","x":-1.2,"y":-1.4,"z":0.9},{"el":"H","x":-1.2,"y":-1.4,"z":-0.9},{"el":"H","x":-2.1,"y":-0.2,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1],[2,3,1],[0,4,1],[4,5,1],[4,6,1],[4,7,1]]
        },
        {
            "id": "benzene", "name": "Benzene", "formula": "C₆H₆", "commonName": "[6]Annulene",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "78.114 g/mol",
            "geometry": "Planar Hexagon (D6h)", "bondAngles": "120.0°",
            "bondTypes": "Delocalized aromatic π system (order 1.5) + C-H σ bonds", "numAtoms": 12, "numBonds": 12,
            "hybridization": "sp²", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless volatile liquid; mp 5.5°C, bp 80.1°C; density 0.876 g/cm³; aromatic odor.",
            "chemicalProps": "Undergoes electrophilic aromatic substitution (nitration, halogenation) rather than addition.",
            "uses": "Feedstock for polystyrene, nylon, polyurethane, synthetic rubber, detergents, phenol.",
            "facts": "August Kekulé deduced the cyclic ring of benzene after having a reverie of an ouroboros snake eating its tail.",
            "atoms": [{"el":"C","x":1.39,"y":0.0,"z":0.0},{"el":"C","x":0.695,"y":1.204,"z":0.0},{"el":"C","x":-0.695,"y":1.204,"z":0.0},{"el":"C","x":-1.39,"y":0.0,"z":0.0},{"el":"C","x":-0.695,"y":-1.204,"z":0.0},{"el":"C","x":0.695,"y":-1.204,"z":0.0},{"el":"H","x":2.47,"y":0.0,"z":0.0},{"el":"H","x":1.235,"y":2.139,"z":0.0},{"el":"H","x":-1.235,"y":2.139,"z":0.0},{"el":"H","x":-2.47,"y":0.0,"z":0.0},{"el":"H","x":-1.235,"y":-2.139,"z":0.0},{"el":"H","x":1.235,"y":-2.139,"z":0.0}],
            "bonds": [[0,1,2],[1,2,1],[2,3,2],[3,4,1],[4,5,2],[5,0,1],[0,6,1],[1,7,1],[2,8,1],[3,9,1],[4,10,1],[5,11,1]]
        },
        {
            "id": "toluene", "name": "Toluene", "formula": "C₇H₈", "commonName": "Methylbenzene",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "92.141 g/mol",
            "geometry": "Planar ring with tetrahedral methyl", "bondAngles": "120° ring, 109.5° methyl",
            "bondTypes": "Aromatic π-ring + C-C, C-H σ bonds", "numAtoms": 15, "numBonds": 15,
            "hybridization": "sp² ring, sp³ methyl", "polarity": "Slightly polar (μ = 0.36 D)",
            "physicalProps": "Colorless liquid with paint-thinner smell; mp -95°C, bp 110.6°C.",
            "chemicalProps": "Electrophilic substitution occurs ortho/para; side-chain free radical chlorination yields benzyl chloride.",
            "uses": "Solvent in paints and adhesives, octane booster in gasoline, precursor to trinitrotoluene (TNT).",
            "facts": "Toluene was first isolated in 1837 by distilling the aromatic balsam of the Tolu tree in South America.",
            "atoms": [{"el":"C","x":0.0,"y":1.4,"z":0.0},{"el":"C","x":1.2,"y":0.7,"z":0.0},{"el":"C","x":1.2,"y":-0.7,"z":0.0},{"el":"C","x":0.0,"y":-1.4,"z":0.0},{"el":"C","x":-1.2,"y":-0.7,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"C","x":0.0,"y":2.9,"z":0.0},{"el":"H","x":2.1,"y":1.2,"z":0.0},{"el":"H","x":2.1,"y":-1.2,"z":0.0},{"el":"H","x":0.0,"y":-2.5,"z":0.0},{"el":"H","x":-2.1,"y":-1.2,"z":0.0},{"el":"H","x":-2.1,"y":1.2,"z":0.0},{"el":"H","x":0.0,"y":3.3,"z":1.0},{"el":"H","x":0.9,"y":3.3,"z":-0.5},{"el":"H","x":-0.9,"y":3.3,"z":-0.5}],
            "bonds": [[0,1,2],[1,2,1],[2,3,2],[3,4,1],[4,5,2],[5,0,1],[0,6,1],[1,7,1],[2,8,1],[3,9,1],[4,10,1],[5,11,1],[6,12,1],[6,13,1],[6,14,1]]
        },
        {
            "id": "phenol", "name": "Phenol", "formula": "C₆H₅OH", "commonName": "Carbolic Acid",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "94.113 g/mol",
            "geometry": "Planar ring with hydroxyl", "bondAngles": "120° ring, C-O-H 109°",
            "bondTypes": "Aromatic π system + polar C-O and O-H σ bonds", "numAtoms": 13, "numBonds": 13,
            "hybridization": "sp² ring, sp³ oxygen", "polarity": "Polar (μ = 1.22 D)",
            "physicalProps": "White crystalline solid turning pink in air; mp 40.5°C, bp 181.7°C; medicinal sweet odor.",
            "chemicalProps": "More acidic than aliphatic alcohols (pKa = 9.95) due to resonance stabilization of phenoxide anion.",
            "uses": "Polycarbonates, epoxy resins, synthesis of aspirin and antiseptic throat lozenges.",
            "facts": "Joseph Lister revolutionized modern surgery in 1865 by introducing carbolic acid (phenol) antiseptic spray.",
            "atoms": [{"el":"C","x":0.0,"y":1.4,"z":0.0},{"el":"C","x":1.2,"y":0.7,"z":0.0},{"el":"C","x":1.2,"y":-0.7,"z":0.0},{"el":"C","x":0.0,"y":-1.4,"z":0.0},{"el":"C","x":-1.2,"y":-0.7,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"O","x":0.0,"y":2.7,"z":0.0},{"el":"H","x":0.8,"y":3.1,"z":0.0},{"el":"H","x":2.1,"y":1.2,"z":0.0},{"el":"H","x":2.1,"y":-1.2,"z":0.0},{"el":"H","x":0.0,"y":-2.5,"z":0.0},{"el":"H","x":-2.1,"y":-1.2,"z":0.0},{"el":"H","x":-2.1,"y":1.2,"z":0.0}],
            "bonds": [[0,1,2],[1,2,1],[2,3,2],[3,4,1],[4,5,2],[5,0,1],[0,6,1],[6,7,1],[1,8,1],[2,9,1],[3,10,1],[4,11,1],[5,12,1]]
        }
    ]

# Category B: Organic Molecules (Part 2)
def get_organic_part2():
    return [
        {
            "id": "aniline", "name": "Aniline", "formula": "C₆H₅NH₂", "commonName": "Aminobenzene",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "93.129 g/mol",
            "geometry": "Planar ring with pyramidal amino", "bondAngles": "120° ring, H-N-H 113°",
            "bondTypes": "Aromatic π system, C-N σ bond, N-H σ bonds", "numAtoms": 14, "numBonds": 14,
            "hybridization": "sp² ring, sp³ nitrogen", "polarity": "Polar (μ = 1.53 D)",
            "physicalProps": "Colorless to brownish oily liquid; mp -6.3°C, bp 184.1°C; fishy odor.",
            "chemicalProps": "Weak base (pKb = 9.3); forms diazonium salts with HNO₂ at 0-5°C (diazotization).",
            "uses": "Azo textile dyes, MDI polyurethane precursors, paracetamol synthesis, rubber chemicals.",
            "facts": "William Henry Perkin accidentally created mauveine, the first synthetic dye, from aniline in 1856.",
            "atoms": [{"el":"C","x":0.0,"y":1.4,"z":0.0},{"el":"C","x":1.2,"y":0.7,"z":0.0},{"el":"C","x":1.2,"y":-0.7,"z":0.0},{"el":"C","x":0.0,"y":-1.4,"z":0.0},{"el":"C","x":-1.2,"y":-0.7,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"N","x":0.0,"y":2.8,"z":0.1},{"el":"H","x":0.8,"y":3.3,"z":-0.2},{"el":"H","x":-0.8,"y":3.3,"z":-0.2},{"el":"H","x":2.1,"y":1.2,"z":0.0},{"el":"H","x":2.1,"y":-1.2,"z":0.0},{"el":"H","x":0.0,"y":-2.5,"z":0.0},{"el":"H","x":-2.1,"y":-1.2,"z":0.0},{"el":"H","x":-2.1,"y":1.2,"z":0.0}],
            "bonds": [[0,1,2],[1,2,1],[2,3,2],[3,4,1],[4,5,2],[5,0,1],[0,6,1],[6,7,1],[6,8,1],[1,9,1],[2,10,1],[3,11,1],[4,12,1],[5,13,1]]
        },
        {
            "id": "glucose", "name": "D-Glucose", "formula": "C₆H₁₂O₆", "commonName": "Dextrose / Blood Sugar",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "180.156 g/mol",
            "geometry": "Pyranose chair conformation", "bondAngles": "C-C-C ~109.5°",
            "bondTypes": "C-C, C-O, O-H, C-H polar σ bonds", "numAtoms": 24, "numBonds": 24,
            "hybridization": "sp³", "polarity": "Highly polar",
            "physicalProps": "White crystalline sweet solid; mp 146°C; density 1.54 g/cm³; soluble in water.",
            "chemicalProps": "Aldohexose; reduces Tollens and Fehling reagents; fuels cellular glycolysis to yield ATP.",
            "uses": "Primary cellular energy source in biology, intravenous nutritional fluids, confectioneries.",
            "facts": "The adult human brain burns roughly 120 grams of pure glucose each day for neural firing.",
            "atoms": [{"el":"C","x":1.2,"y":-0.7,"z":0.2},{"el":"C","x":1.3,"y":0.8,"z":-0.2},{"el":"C","x":0.0,"y":1.5,"z":0.2},{"el":"C","x":-1.2,"y":0.7,"z":-0.2},{"el":"C","x":-1.2,"y":-0.8,"z":0.2},{"el":"O","x":0.0,"y":-1.4,"z":-0.2},{"el":"O","x":2.3,"y":-1.3,"z":-0.4},{"el":"O","x":2.4,"y":1.3,"z":0.4},{"el":"O","x":0.0,"y":2.8,"z":-0.4},{"el":"O","x":-2.3,"y":1.4,"z":0.4},{"el":"C","x":-2.4,"y":-1.6,"z":-0.2},{"el":"O","x":-2.3,"y":-2.9,"z":0.4},{"el":"H","x":1.2,"y":-0.8,"z":1.3},{"el":"H","x":1.4,"y":0.9,"z":-1.3},{"el":"H","x":0.0,"y":1.5,"z":1.3},{"el":"H","x":-1.2,"y":0.8,"z":-1.3},{"el":"H","x":-1.2,"y":-0.9,"z":1.3},{"el":"H","x":3.1,"y":-1.0,"z":0.0},{"el":"H","x":3.2,"y":1.1,"z":0.0},{"el":"H","x":0.8,"y":3.1,"z":-0.2},{"el":"H","x":-3.1,"y":1.1,"z":0.0},{"el":"H","x":-3.1,"y":-3.1,"z":0.0},{"el":"H","x":-3.3,"y":-1.2,"z":0.2},{"el":"H","x":-2.4,"y":-1.6,"z":-1.3}],
            "bonds": [[0,1,1],[1,2,1],[2,3,1],[3,4,1],[4,5,1],[5,0,1],[0,6,1],[1,7,1],[2,8,1],[3,9,1],[4,10,1],[10,11,1],[0,12,1],[1,13,1],[2,14,1],[3,15,1],[4,16,1],[6,17,1],[7,18,1],[8,19,1],[9,20,1],[11,21,1],[10,22,1],[10,23,1]]
        },
        {
            "id": "fructose", "name": "D-Fructose", "formula": "C₆H₁₂O₆", "commonName": "Fruit Sugar",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "180.156 g/mol",
            "geometry": "Furanose envelope ring", "bondAngles": "C-C-C ~108°",
            "bondTypes": "C-C, C-O, O-H, C-H polar σ bonds", "numAtoms": 24, "numBonds": 24,
            "hybridization": "sp³", "polarity": "Highly polar",
            "physicalProps": "White crystalline solid; mp 103°C; sweetest of natural carbohydrates.",
            "chemicalProps": "Ketohexose; isomerizes to glucose in base via enediol intermediate; reducing sugar.",
            "uses": "High-fructose corn syrup, honey, fruit food sweetener, baking browning enhancer.",
            "facts": "Fructose is the sweetest naturally occurring sugar, 1.7× sweeter than common table sugar.",
            "atoms": [{"el":"C","x":0.0,"y":1.1,"z":-0.1},{"el":"C","x":1.2,"y":0.2,"z":0.2},{"el":"C","x":0.7,"y":-1.2,"z":-0.1},{"el":"C","x":-0.8,"y":-1.1,"z":0.1},{"el":"O","x":-1.1,"y":0.3,"z":-0.2},{"el":"C","x":0.1,"y":2.3,"z":0.8},{"el":"O","x":0.0,"y":3.5,"z":0.1},{"el":"O","x":2.4,"y":0.6,"z":-0.3},{"el":"O","x":1.3,"y":-2.1,"z":0.7},{"el":"C","x":-1.8,"y":-2.0,"z":-0.5},{"el":"O","x":-3.1,"y":-1.6,"z":-0.1},{"el":"O","x":0.2,"y":1.4,"z":-1.4},{"el":"H","x":1.2,"y":0.2,"z":1.3},{"el":"H","x":0.8,"y":-1.5,"z":-1.1},{"el":"H","x":-0.9,"y":-1.1,"z":1.2},{"el":"H","x":-0.7,"y":2.3,"z":1.5},{"el":"H","x":1.0,"y":2.2,"z":1.4},{"el":"H","x":0.0,"y":4.2,"z":0.7},{"el":"H","x":3.1,"y":0.1,"z":0.0},{"el":"H","x":2.2,"y":-2.1,"z":0.5},{"el":"H","x":-3.6,"y":-2.2,"z":-0.5},{"el":"H","x":-1.7,"y":-3.0,"z":-0.2},{"el":"H","x":-1.7,"y":-1.9,"z":-1.6},{"el":"H","x":-0.6,"y":1.7,"z":-1.6}],
            "bonds": [[0,1,1],[1,2,1],[2,3,1],[3,4,1],[4,0,1],[0,5,1],[5,6,1],[1,7,1],[2,8,1],[3,9,1],[9,10,1],[0,11,1],[1,12,1],[2,13,1],[3,14,1],[5,15,1],[5,16,1],[6,17,1],[7,18,1],[8,19,1],[10,20,1],[9,21,1],[9,22,1],[11,23,1]]
        },
        {
            "id": "sucrose", "name": "Sucrose", "formula": "C₁₂H₂₂O₁₁", "commonName": "Table Sugar",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "342.30 g/mol",
            "geometry": "Disaccharide (glucose + fructose)", "bondAngles": "Glycosidic C-O-C ~116°",
            "bondTypes": "C-C, C-O, O-H, C-H polar σ bonds", "numAtoms": 26, "numBonds": 26,
            "hybridization": "sp³", "polarity": "Highly polar",
            "physicalProps": "White crystalline solid; mp 186°C (decomposes); density 1.587 g/cm³.",
            "chemicalProps": "Non-reducing disaccharide; hydrolyzed by sucrase enzyme into glucose and fructose.",
            "uses": "Universal dietary sweetener, confectionery, fermentation feedstock for bioethanol.",
            "facts": "Hydrolysis of sucrose produces invert sugar because the optical rotation flips from positive to negative.",
            "atoms": [{"el":"C","x":-2.5,"y":0.5,"z":0.0},{"el":"C","x":-3.5,"y":-0.6,"z":0.0},{"el":"C","x":-2.8,"y":-1.9,"z":0.0},{"el":"C","x":-1.3,"y":-1.8,"z":0.0},{"el":"C","x":-0.6,"y":-0.5,"z":0.0},{"el":"O","x":-1.3,"y":0.7,"z":0.0},{"el":"O","x":0.7,"y":-0.4,"z":0.0},{"el":"C","x":1.6,"y":0.6,"z":0.0},{"el":"C","x":3.0,"y":0.1,"z":0.0},{"el":"C","x":3.0,"y":-1.4,"z":0.0},{"el":"C","x":1.5,"y":-1.8,"z":0.0},{"el":"O","x":0.9,"y":-0.6,"z":0.8},{"el":"O","x":-4.8,"y":-0.6,"z":0.0},{"el":"O","x":-3.4,"y":-3.0,"z":0.0},{"el":"O","x":-0.7,"y":-2.9,"z":0.0},{"el":"O","x":4.1,"y":0.9,"z":0.0},{"el":"O","x":4.1,"y":-2.1,"z":0.0},{"el":"H","x":-2.6,"y":1.1,"z":0.9},{"el":"H","x":-3.5,"y":-0.7,"z":-1.1},{"el":"H","x":-2.8,"y":-2.0,"z":1.1},{"el":"H","x":-1.3,"y":-1.8,"z":-1.1},{"el":"H","x":-0.6,"y":-0.5,"z":-1.1},{"el":"H","x":1.5,"y":1.2,"z":0.9},{"el":"H","x":3.0,"y":0.2,"z":-1.1},{"el":"H","x":3.0,"y":-1.5,"z":1.1},{"el":"H","x":1.4,"y":-2.4,"z":-0.9}],
            "bonds": [[0,1,1],[1,2,1],[2,3,1],[3,4,1],[4,5,1],[5,0,1],[4,6,1],[6,7,1],[7,8,1],[8,9,1],[9,10,1],[10,11,1],[1,12,1],[2,13,1],[3,14,1],[8,15,1],[9,16,1],[0,17,1],[1,18,1],[2,19,1],[3,20,1],[4,21,1],[7,22,1],[8,23,1],[9,24,1],[10,25,1]]
        },
        {
            "id": "urea", "name": "Urea", "formula": "CH₄N₂O", "commonName": "Carbamide",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "60.056 g/mol",
            "geometry": "Planar due to resonance", "bondAngles": "N-C-N 118.0°, N-C=O 121.0°",
            "bondTypes": "C=O double bond, 2 C-N resonant bonds, 4 N-H bonds", "numAtoms": 8, "numBonds": 7,
            "hybridization": "sp²", "polarity": "Polar (μ = 4.56 D)",
            "physicalProps": "White crystalline solid; mp 133°C; highly water soluble (1079 g/L at 20°C).",
            "chemicalProps": "Hydrolyzed by urease to CO₂ and 2NH₃; high nitrogen content (46% by weight).",
            "uses": "Primary agricultural nitrogen fertilizer, diesel exhaust fluid (AdBlue), resin synthesis.",
            "facts": "Wöhler's 1828 synthesis of urea from inorganic ammonium cyanate disproved vitalism.",
            "atoms": [{"el":"C","x":0.0,"y":0.14,"z":0.0},{"el":"O","x":0.0,"y":1.36,"z":0.0},{"el":"N","x":-1.16,"y":-0.60,"z":0.0},{"el":"N","x":1.16,"y":-0.60,"z":0.0},{"el":"H","x":-2.05,"y":-0.13,"z":0.0},{"el":"H","x":-1.13,"y":-1.61,"z":0.0},{"el":"H","x":2.05,"y":-0.13,"z":0.0},{"el":"H","x":1.13,"y":-1.61,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1],[0,3,1],[2,4,1],[2,5,1],[3,6,1],[3,7,1]]
        },
        {
            "id": "glycerol", "name": "Glycerol", "formula": "C₃H₈O₃", "commonName": "Glycerin",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "92.094 g/mol",
            "geometry": "Tetrahedral chain", "bondAngles": "C-C-C 112°, C-O-H 108°",
            "bondTypes": "C-C, C-O, O-H, C-H polar σ bonds", "numAtoms": 14, "numBonds": 13,
            "hybridization": "sp³", "polarity": "Highly polar",
            "physicalProps": "Viscous, sweet colorless liquid; mp 17.8°C, bp 290°C; density 1.261 g/cm³.",
            "chemicalProps": "Reacts with HNO₃/H₂SO₄ to form explosive nitroglycerin; esterified into fats/oils.",
            "uses": "Cosmetic humectant, cough syrup, pharmaceutical solvent, food sweetener, dynamite precursor.",
            "facts": "Glycerol forms the chemical backbone of all triglycerides (fats and oils) in biology.",
            "atoms": [{"el":"C","x":-1.3,"y":0.0,"z":0.0},{"el":"C","x":0.0,"y":0.6,"z":0.0},{"el":"C","x":1.3,"y":-0.1,"z":0.0},{"el":"O","x":-2.3,"y":0.9,"z":0.0},{"el":"O","x":0.0,"y":2.0,"z":0.0},{"el":"O","x":2.3,"y":0.8,"z":0.0},{"el":"H","x":-3.1,"y":0.5,"z":0.0},{"el":"H","x":0.8,"y":2.4,"z":0.0},{"el":"H","x":3.1,"y":0.4,"z":0.0},{"el":"H","x":-1.3,"y":-0.6,"z":0.9},{"el":"H","x":-1.3,"y":-0.6,"z":-0.9},{"el":"H","x":0.0,"y":0.2,"z":1.0},{"el":"H","x":1.3,"y":-0.7,"z":0.9},{"el":"H","x":1.3,"y":-0.7,"z":-0.9}],
            "bonds": [[0,1,1],[1,2,1],[0,3,1],[1,4,1],[2,5,1],[3,6,1],[4,7,1],[5,8,1],[0,9,1],[0,10,1],[1,11,1],[2,12,1],[2,13,1]]
        },
        {
            "id": "chloroform", "name": "Chloroform", "formula": "CHCl₃", "commonName": "Trichloromethane",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "119.38 g/mol",
            "geometry": "Tetrahedral", "bondAngles": "Cl-C-Cl 110.5°",
            "bondTypes": "3 polar C-Cl σ bonds + 1 C-H σ bond", "numAtoms": 5, "numBonds": 4,
            "hybridization": "sp³", "polarity": "Polar (μ = 1.04 D)",
            "physicalProps": "Dense sweet-smelling liquid; mp -63.5°C, bp 61.2°C; density 1.489 g/cm³.",
            "chemicalProps": "Oxidizes in light to phosgene COCl₂; deprotonated to dichlorocarbene :CCl₂.",
            "uses": "Teflon PTFE precursor (via chlorodifluoromethane), NMR solvent (CDCl₃).",
            "facts": "James Simpson first used chloroform as an anesthetic in 1847 on Queen Victoria.",
            "atoms": [{"el":"C","x":0.0,"y":0.0,"z":0.35},{"el":"H","x":0.0,"y":0.0,"z":1.43},{"el":"Cl","x":1.45,"y":0.0,"z":-0.36},{"el":"Cl","x":-0.72,"y":1.25,"z":-0.36},{"el":"Cl","x":-0.72,"y":-1.25,"z":-0.36}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1],[0,4,1]]
        },
        {
            "id": "ethylacetate", "name": "Ethyl Acetate", "formula": "CH₃COOC₂H₅", "commonName": "Ethyl Ethanoate",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "88.106 g/mol",
            "geometry": "Planar ester group with tetrahedral carbons", "bondAngles": "C-C(=O)-O 123°",
            "bondTypes": "C=O double bond, C-O, C-C, C-H σ bonds", "numAtoms": 14, "numBonds": 13,
            "hybridization": "sp² carbonyl, sp³ carbons and alkoxy oxygen", "polarity": "Polar (μ = 1.78 D)",
            "physicalProps": "Colorless liquid with sweet fruity pear aroma; mp -83.6°C, bp 77.1°C.",
            "chemicalProps": "Saponified by base to acetate and ethanol; hydrolyzes in acid.",
            "uses": "Extraction solvent, decaffeination of coffee beans, non-acetone nail polish remover.",
            "facts": "Ethyl acetate provides the characteristic fruity aroma in wines and confectionery.",
            "atoms": [{"el":"C","x":0.0,"y":0.3,"z":0.0},{"el":"O","x":0.0,"y":1.5,"z":0.0},{"el":"O","x":1.1,"y":-0.4,"z":0.0},{"el":"C","x":-1.3,"y":-0.5,"z":0.0},{"el":"C","x":2.4,"y":0.3,"z":0.0},{"el":"C","x":3.5,"y":-0.7,"z":0.0},{"el":"H","x":-1.3,"y":-1.1,"z":0.9},{"el":"H","x":-1.3,"y":-1.1,"z":-0.9},{"el":"H","x":-2.1,"y":0.1,"z":0.0},{"el":"H","x":2.4,"y":0.9,"z":0.9},{"el":"H","x":2.4,"y":0.9,"z":-0.9},{"el":"H","x":4.5,"y":-0.2,"z":0.0},{"el":"H","x":3.5,"y":-1.3,"z":0.9},{"el":"H","x":3.5,"y":-1.3,"z":-0.9}],
            "bonds": [[0,1,2],[0,2,1],[0,3,1],[2,4,1],[4,5,1],[3,6,1],[3,7,1],[3,8,1],[4,9,1],[4,10,1],[5,11,1],[5,12,1],[5,13,1]]
        },
        {
            "id": "acetaldehyde", "name": "Acetaldehyde", "formula": "CH₃CHO", "commonName": "Ethanal",
            "category": "Organic Molecules", "categoryKey": "organic", "mw": "44.053 g/mol",
            "geometry": "Planar at carbonyl", "bondAngles": "C-C=O 124°",
            "bondTypes": "C=O double bond + C-C, C-H σ bonds", "numAtoms": 7, "numBonds": 6,
            "hybridization": "sp² carbonyl, sp³ methyl", "polarity": "Polar (μ = 2.7 D)",
            "physicalProps": "Colorless flammable volatile liquid; mp -123°C, bp 20.2°C; pungent fruity odor.",
            "chemicalProps": "Easily oxidized to acetic acid; reduces Tollens reagent; undergoes aldol condensation.",
            "uses": "Manufacture of acetic acid, pyridine, pentaerythritol, and synthetic perfumes.",
            "facts": "Acetaldehyde is the toxic breakdown intermediate of ethanol responsible for hangovers.",
            "atoms": [{"el":"C","x":0.4,"y":0.3,"z":0.0},{"el":"O","x":1.5,"y":-0.1,"z":0.0},{"el":"H","x":0.3,"y":1.4,"z":0.0},{"el":"C","x":-0.9,"y":-0.5,"z":0.0},{"el":"H","x":-1.7,"y":0.2,"z":0.0},{"el":"H","x":-0.9,"y":-1.1,"z":0.9},{"el":"H","x":-0.9,"y":-1.1,"z":-0.9}],
            "bonds": [[0,1,2],[0,2,1],[0,3,1],[3,4,1],[3,5,1],[3,6,1]]
        }
    ]

def get_organic_molecules():
    return get_organic_part1() + get_organic_part2()
