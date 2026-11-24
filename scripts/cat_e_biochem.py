# Category E: Biological and Biochemical Molecules (Part 1)
def get_biochem_part1():
    return [
        {
            "id": "glycine", "name": "Glycine", "formula": "C₂H₅NO₂", "commonName": "Aminoacetic Acid / Gly",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "75.067 g/mol",
            "geometry": "Planar carboxyl with tetrahedral alpha carbon", "bondAngles": "N-Cα-C 111°",
            "bondTypes": "C-C, C-N, C-O, O-H, N-H, C-H polar σ bonds", "numAtoms": 10, "numBonds": 9,
            "hybridization": "sp² carboxyl, sp³ alpha carbon and amine", "polarity": "Zwitterionic polar (μ = 15 D in water)",
            "physicalProps": "White sweet-tasting crystalline solid; decomposes at 233°C; isoelectric point pI = 5.97.",
            "chemicalProps": "Simplest proteinogenic amino acid; only amino acid without a chiral stereocenter; acts as inhibitory neurotransmitter.",
            "uses": "Primary component of structural collagen (every 3rd residue), inhibitory neurotransmitter in spinal cord, buffer.",
            "facts": "Glycine is the only standard amino acid that is achiral and does not exhibit optical isomerism (it has two hydrogen atoms on Cα).",
            "atoms": [{"el":"C","x":0.0,"y":0.2,"z":0.0},{"el":"O","x":0.0,"y":1.4,"z":0.0},{"el":"O","x":1.2,"y":-0.5,"z":0.0},{"el":"H","x":1.9,"y":0.0,"z":0.0},{"el":"C","x":-1.3,"y":-0.6,"z":0.0},{"el":"N","x":-2.4,"y":0.3,"z":0.0},{"el":"H","x":-3.3,"y":-0.1,"z":0.0},{"el":"H","x":-2.3,"y":1.3,"z":0.0},{"el":"H","x":-1.3,"y":-1.2,"z":0.9},{"el":"H","x":-1.3,"y":-1.2,"z":-0.9}],
            "bonds": [[0,1,2],[0,2,1],[2,3,1],[0,4,1],[4,5,1],[5,6,1],[5,7,1],[4,8,1],[4,9,1]]
        },
        {
            "id": "alanine", "name": "L-Alanine", "formula": "C₃H₇NO₂", "commonName": "2-Aminopropanoic Acid / Ala",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "89.093 g/mol",
            "geometry": "Tetrahedral chiral center at Cα", "bondAngles": "109.5° at Cα",
            "bondTypes": "C-C, C-N, C-O, O-H, N-H, C-H polar σ bonds", "numAtoms": 13, "numBonds": 12,
            "hybridization": "sp² carboxyl, sp³ carbons and amine", "polarity": "Zwitterionic polar",
            "physicalProps": "White crystalline odorless powder; decomposes at 297°C; dextrorotatory in acid.",
            "chemicalProps": "Aliphatic non-polar amino acid; key player in the glucose-alanine cycle between muscle and liver.",
            "uses": "Protein synthesis building block, gluconeogenic precursor during fasting, nutrition supplement.",
            "facts": "Alanine is the second most abundant amino acid in proteins after leucine, accounting for ~7.8% of primary protein structure.",
            "atoms": [{"el":"C","x":0.0,"y":0.3,"z":0.0},{"el":"O","x":0.0,"y":1.5,"z":0.0},{"el":"O","x":1.2,"y":-0.4,"z":0.0},{"el":"H","x":1.9,"y":0.1,"z":0.0},{"el":"C","x":-1.3,"y":-0.5,"z":0.0},{"el":"N","x":-1.3,"y":-1.9,"z":0.0},{"el":"C","x":-2.5,"y":0.3,"z":0.0},{"el":"H","x":-1.3,"y":-0.3,"z":1.0},{"el":"H","x":-2.2,"y":-2.3,"z":0.0},{"el":"H","x":-0.5,"y":-2.4,"z":0.0},{"el":"H","x":-3.4,"y":-0.3,"z":0.0},{"el":"H","x":-2.5,"y":0.9,"z":0.9},{"el":"H","x":-2.5,"y":0.9,"z":-0.9}],
            "bonds": [[0,1,2],[0,2,1],[2,3,1],[0,4,1],[4,5,1],[4,6,1],[4,7,1],[5,8,1],[5,9,1],[6,10,1],[6,11,1],[6,12,1]]
        },
        {
            "id": "atp", "name": "Adenosine Triphosphate", "formula": "C₁₀H₁₆N₅O₁₃P₃", "commonName": "ATP / Cellular Energy Currency",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "507.18 g/mol",
            "geometry": "Adenine purine + ribose furanose + triphosphate chain", "bondAngles": "P-O-P ~130°",
            "bondTypes": "Two phosphoanhydride high-energy bonds + phosphoester bond", "numAtoms": 35, "numBonds": 36,
            "hybridization": "sp² purine, sp³ ribose and phosphates", "polarity": "Highly polar tetra-anion (ATP⁴⁻ at pH 7)",
            "physicalProps": "White powder; highly soluble in water; unstable at high pH/temperature; coordinates Mg²⁺.",
            "chemicalProps": "Hydrolysis of terminal phosphoanhydride releases ΔG°' = -30.5 kJ/mol (-7.3 kcal/mol) to drive cellular work.",
            "uses": "Universal energy currency for muscle contraction, active membrane ion transport, RNA transcription.",
            "facts": "A typical resting human body recycles its own entire body weight in ATP every single day through ATP synthase rotation.",
            "atoms": [{"el":"P","x":3.5,"y":0.0,"z":0.0},{"el":"O","x":3.5,"y":1.5,"z":0.0},{"el":"O","x":2.2,"y":-0.5,"z":0.0},{"el":"P","x":0.9,"y":0.2,"z":0.0},{"el":"O","x":0.9,"y":1.7,"z":0.0},{"el":"O","x":-0.4,"y":-0.5,"z":0.0},{"el":"P","x":-1.7,"y":0.2,"z":0.0},{"el":"O","x":-1.7,"y":1.7,"z":0.0},{"el":"O","x":-2.9,"y":-0.7,"z":0.0},{"el":"C","x":-4.1,"y":0.0,"z":0.0},{"el":"C","x":-5.2,"y":-0.9,"z":0.0},{"el":"O","x":-4.9,"y":-2.2,"z":0.0},{"el":"C","x":-6.2,"y":-2.8,"z":0.0},{"el":"N","x":-7.0,"y":-1.8,"z":0.0},{"el":"C","x":-8.3,"y":-1.8,"z":0.0},{"el":"N","x":-8.9,"y":-0.7,"z":0.0},{"el":"C","x":-8.1,"y":0.4,"z":0.0},{"el":"C","x":-6.7,"y":0.3,"z":0.0},{"el":"N","x":-6.2,"y":-0.9,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1],[2,3,1],[3,4,2],[3,5,1],[5,6,1],[6,7,2],[6,8,1],[8,9,1],[9,10,1],[10,11,1],[11,12,1],[10,18,1],[12,13,1],[13,14,2],[14,15,1],[15,16,2],[16,17,1],[17,18,1],[17,13,1]]
        },
        {
            "id": "adenine", "name": "Adenine", "formula": "C₅H₅N₅", "commonName": "6-Aminopurine / A",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "135.13 g/mol",
            "geometry": "Planar fused bicyclic purine (pyrimidine + imidazole)", "bondAngles": "120° in 6-ring, 108° in 5-ring",
            "bondTypes": "Aromatic delocalized 10-π electron system + exocyclic C-NH₂", "numAtoms": 15, "numBonds": 16,
            "hybridization": "sp² at all ring atoms", "polarity": "Polar (μ = 2.5 D)",
            "physicalProps": "White to pale cream microcrystalline powder; mp 360-365°C (sublimes); UV absorbance peak at 260 nm.",
            "chemicalProps": "Forms two Watson-Crick hydrogen bonds with Thymine (DNA) or Uracil (RNA); constituent of ATP, NAD⁺, FAD.",
            "uses": "Genetic code informational alphabet, component of coenzymes (NAD, CoA), nucleic acid synthesis.",
            "facts": "In 1961, Joan Oró discovered that adenine can be synthesized abiotically simply by heating aqueous ammonium cyanide (HCN).",
            "atoms": [{"el":"N","x":-1.2,"y":1.3,"z":0.0},{"el":"C","x":0.0,"y":1.8,"z":0.0},{"el":"N","x":1.1,"y":1.1,"z":0.0},{"el":"C","x":1.0,"y":-0.2,"z":0.0},{"el":"C","x":-0.2,"y":-0.9,"z":0.0},{"el":"C","x":-1.3,"y":-0.1,"z":0.0},{"el":"N","x":-0.1,"y":-2.2,"z":0.0},{"el":"C","x":1.2,"y":-2.3,"z":0.0},{"el":"N","x":1.9,"y":-1.2,"z":0.0},{"el":"N","x":0.1,"y":3.1,"z":0.0},{"el":"H","x":-2.0,"y":1.8,"z":0.0},{"el":"H","x":-2.3,"y":-0.5,"z":0.0},{"el":"H","x":1.6,"y":-3.3,"z":0.0},{"el":"H","x":-0.7,"y":3.7,"z":0.0},{"el":"H","x":0.9,"y":3.6,"z":0.0}],
            "bonds": [[0,1,1],[1,2,2],[2,3,1],[3,4,2],[4,5,1],[5,0,2],[4,6,1],[6,7,1],[7,8,2],[8,3,1],[1,9,1],[0,10,1],[5,11,1],[7,12,1],[9,13,1],[9,14,1]]
        },
        {
            "id": "guanine", "name": "Guanine", "formula": "C₅H₅N₅O", "commonName": "2-Amino-6-oxypurine / G",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "151.13 g/mol",
            "geometry": "Planar purine bicyclic ring", "bondAngles": "120° in 6-ring, 108° in 5-ring",
            "bondTypes": "Aromatic π system, C=O carbonyl, C-NH₂ exocyclic", "numAtoms": 16, "numBonds": 17,
            "hybridization": "sp²", "polarity": "Polar (μ = 6.8 D)",
            "physicalProps": "White crystalline powder with pearlescent iridescence; mp > 300°C; low water solubility.",
            "chemicalProps": "Forms three Watson-Crick hydrogen bonds with Cytosine (providing high thermal stability to GC-rich DNA).",
            "uses": "DNA/RNA genetic base, GTP molecular switch signaling, pearlescent pigment in cosmetics.",
            "facts": "Guanine was first isolated in 1844 from sea bird excrement (guano), from which it derives its name.",
            "atoms": [{"el":"N","x":-1.2,"y":1.3,"z":0.0},{"el":"C","x":0.0,"y":1.8,"z":0.0},{"el":"O","x":0.1,"y":3.0,"z":0.0},{"el":"N","x":1.1,"y":1.0,"z":0.0},{"el":"C","x":1.0,"y":-0.3,"z":0.0},{"el":"C","x":-0.2,"y":-0.9,"z":0.0},{"el":"C","x":-1.3,"y":-0.1,"z":0.0},{"el":"N","x":-2.5,"y":-0.7,"z":0.0},{"el":"N","x":-0.1,"y":-2.2,"z":0.0},{"el":"C","x":1.2,"y":-2.3,"z":0.0},{"el":"N","x":1.9,"y":-1.2,"z":0.0},{"el":"H","x":-1.9,"y":1.9,"z":0.0},{"el":"H","x":-2.5,"y":-1.7,"z":0.0},{"el":"H","x":-3.4,"y":-0.2,"z":0.0},{"el":"H","x":1.6,"y":-3.3,"z":0.0}],
            "bonds": [[0,1,1],[1,2,2],[1,3,1],[3,4,1],[4,5,2],[5,6,1],[6,0,1],[6,7,1],[5,8,1],[8,9,1],[9,10,2],[10,4,1],[0,11,1],[7,12,1],[7,13,1],[9,14,1]]
        },
        {
            "id": "cytosine", "name": "Cytosine", "formula": "C₄H₅N₃O", "commonName": "4-Amino-2-oxypyrimidine / C",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "111.10 g/mol",
            "geometry": "Planar 6-membered pyrimidine ring", "bondAngles": "120°",
            "bondTypes": "Aromatic π system, C=O double bond, C-NH₂ amino", "numAtoms": 13, "numBonds": 13,
            "hybridization": "sp²", "polarity": "Polar (μ = 6.4 D)",
            "physicalProps": "White crystalline powder; decomposes at 320-325°C; UV absorption λmax = 267 nm.",
            "chemicalProps": "Forms 3 hydrogen bonds with Guanine; undergoes spontaneous deamination into Uracil (repaired by uracil-DNA glycosylase).",
            "uses": "Genetic code base pairing, DNA methylation epigenetic regulation (5-methylcytosine).",
            "facts": "Spontaneous deamination of cytosine into uracil occurs ~100 times daily in every human cell and is constantly repaired to prevent C→T mutations.",
            "atoms": [{"el":"N","x":0.0,"y":1.3,"z":0.0},{"el":"C","x":1.2,"y":0.6,"z":0.0},{"el":"N","x":1.2,"y":-0.8,"z":0.0},{"el":"C","x":0.0,"y":-1.4,"z":0.0},{"el":"O","x":0.0,"y":-2.6,"z":0.0},{"el":"C","x":-1.2,"y":-0.6,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"N","x":2.3,"y":1.3,"z":0.0},{"el":"H","x":0.0,"y":2.3,"z":0.0},{"el":"H","x":-2.1,"y":-1.1,"z":0.0},{"el":"H","x":-2.1,"y":1.3,"z":0.0},{"el":"H","x":2.3,"y":2.3,"z":0.0},{"el":"H","x":3.2,"y":0.8,"z":0.0}],
            "bonds": [[0,1,1],[1,2,2],[2,3,1],[3,4,2],[3,5,1],[5,6,2],[6,0,1],[1,7,1],[0,8,1],[5,9,1],[6,10,1],[7,11,1],[7,12,1]]
        },
        {
            "id": "thymine", "name": "Thymine", "formula": "C₅H₆N₂O₂", "commonName": "5-Methyluracil / T",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "126.11 g/mol",
            "geometry": "Planar pyrimidine ring with methyl group", "bondAngles": "120° ring",
            "bondTypes": "2 C=O carbonyls, aromatic ring, C-CH₃ σ bond", "numAtoms": 15, "numBonds": 15,
            "hybridization": "sp² ring, sp³ methyl", "polarity": "Polar (μ = 4.1 D)",
            "physicalProps": "White crystalline plates; mp 316-317°C; insoluble in ether, soluble in hot water.",
            "chemicalProps": "Pairs with Adenine via two hydrogen bonds; UV light induces adjacent thymines to form cyclobutane thymine dimers (DNA damage).",
            "uses": "Exclusive DNA pyrimidine base, target of anti-cancer chemotherapies like 5-fluorouracil.",
            "facts": "DNA uses thymine instead of uracil because the methyl tag allows DNA repair enzymes to distinguish normal thymine from deaminated cytosine.",
            "atoms": [{"el":"N","x":0.0,"y":1.3,"z":0.0},{"el":"C","x":1.2,"y":0.7,"z":0.0},{"el":"C","x":1.2,"y":-0.7,"z":0.0},{"el":"C","x":2.5,"y":-1.4,"z":0.0},{"el":"C","x":0.0,"y":-1.4,"z":0.0},{"el":"O","x":0.0,"y":-2.6,"z":0.0},{"el":"N","x":-1.2,"y":-0.7,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"O","x":-2.3,"y":1.3,"z":0.0},{"el":"H","x":0.0,"y":2.3,"z":0.0},{"el":"H","x":2.1,"y":1.3,"z":0.0},{"el":"H","x":-1.2,"y":-1.7,"z":0.0},{"el":"H","x":3.3,"y":-0.7,"z":0.0},{"el":"H","x":2.5,"y":-2.0,"z":0.9},{"el":"H","x":2.5,"y":-2.0,"z":-0.9}],
            "bonds": [[0,1,1],[1,2,2],[2,3,1],[2,4,1],[4,5,2],[4,6,1],[6,7,1],[7,8,2],[7,0,1],[0,9,1],[1,10,1],[6,11,1],[3,12,1],[3,13,1],[3,14,1]]
        }
    ]

# Category E: Biological and Biochemical Molecules (Part 2)
def get_biochem_part2():
    return [
        {
            "id": "uracil", "name": "Uracil", "formula": "C₄H₄N₂O₂", "commonName": "2,4-Dioxypyrimidine / U",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "112.09 g/mol",
            "geometry": "Planar 6-membered ring", "bondAngles": "120°",
            "bondTypes": "Aromatic π system with 2 C=O carbonyls and 2 N-H bonds", "numAtoms": 12, "numBonds": 12,
            "hybridization": "sp²", "polarity": "Polar (μ = 4.2 D)",
            "physicalProps": "White crystalline powder; mp 335°C (decomposes); soluble in hot water.",
            "chemicalProps": "RNA base; forms 2 hydrogen bonds with Adenine; demethylated analog of thymine.",
            "uses": "Ribonucleic acid (RNA) messenger transcription, protein synthesis, allosteric regulator.",
            "facts": "Uracil is used in RNA instead of thymine because it is energetically cheaper to synthesize for temporary messenger transcripts.",
            "atoms": [{"el":"N","x":0.0,"y":1.3,"z":0.0},{"el":"C","x":1.2,"y":0.7,"z":0.0},{"el":"C","x":1.2,"y":-0.7,"z":0.0},{"el":"C","x":0.0,"y":-1.4,"z":0.0},{"el":"O","x":0.0,"y":-2.6,"z":0.0},{"el":"N","x":-1.2,"y":-0.7,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"O","x":-2.3,"y":1.3,"z":0.0},{"el":"H","x":0.0,"y":2.3,"z":0.0},{"el":"H","x":2.1,"y":1.3,"z":0.0},{"el":"H","x":2.1,"y":-1.2,"z":0.0},{"el":"H","x":-1.2,"y":-1.7,"z":0.0}],
            "bonds": [[0,1,1],[1,2,2],[2,3,1],[3,4,2],[3,5,1],[5,6,1],[6,7,2],[6,0,1],[0,8,1],[1,9,1],[2,10,1],[5,11,1]]
        },
        {
            "id": "lacticacid", "name": "Lactic Acid", "formula": "C₃H₆O₃", "commonName": "2-Hydroxypropanoic Acid / Milk Acid",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "90.078 g/mol",
            "geometry": "Tetrahedral chiral Cα with planar carboxyl", "bondAngles": "109.5° at Cα",
            "bondTypes": "C-C, C-O, O-H, C=O polar covalent bonds", "numAtoms": 12, "numBonds": 11,
            "hybridization": "sp² carboxyl, sp³ carbons", "polarity": "Polar (μ = 2.6 D)",
            "physicalProps": "Colorless syrupy hygroscopic liquid or low-melting solid; mp 16.8°C, bp 122°C (at 15 mmHg).",
            "chemicalProps": "Alpha-hydroxy acid (pKa = 3.86); produced during anaerobic glycolysis by lactate dehydrogenase.",
            "uses": "Biodegradable polylactic acid (PLA) 3D printing filaments, skincare chemical exfoliant, food preservative.",
            "facts": "Carl Wilhelm Scheele first isolated lactic acid in 1780 from sour milk, while Pasteur proved in 1857 it was produced by microbial fermentation.",
            "atoms": [{"el":"C","x":0.0,"y":0.2,"z":0.0},{"el":"O","x":0.0,"y":1.4,"z":0.0},{"el":"O","x":1.2,"y":-0.5,"z":0.0},{"el":"H","x":1.9,"y":0.0,"z":0.0},{"el":"C","x":-1.3,"y":-0.6,"z":0.0},{"el":"O","x":-1.3,"y":-1.9,"z":0.0},{"el":"H","x":-2.1,"y":-2.3,"z":0.0},{"el":"C","x":-2.5,"y":0.2,"z":0.0},{"el":"H","x":-1.3,"y":-0.3,"z":1.0},{"el":"H","x":-3.4,"y":-0.4,"z":0.0},{"el":"H","x":-2.5,"y":0.8,"z":0.9},{"el":"H","x":-2.5,"y":0.8,"z":-0.9}],
            "bonds": [[0,1,2],[0,2,1],[2,3,1],[0,4,1],[4,5,1],[5,6,1],[4,7,1],[4,8,1],[7,9,1],[7,10,1],[7,11,1]]
        },
        {
            "id": "citricacid", "name": "Citric Acid", "formula": "C₆H₈O₇", "commonName": "2-Hydroxypropane-1,2,3-tricarboxylic Acid",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "192.124 g/mol",
            "geometry": "Branched aliphatic tricarboxylic acid", "bondAngles": "109.5° at central C",
            "bondTypes": "C-C, C-O, O-H, C=O polar covalent bonds", "numAtoms": 21, "numBonds": 20,
            "hybridization": "sp² carboxyls, sp³ chain", "polarity": "Highly polar",
            "physicalProps": "White crystalline sour solid; mp 153°C; density 1.665 g/cm³; highly soluble in water (59% at 20°C).",
            "chemicalProps": "Triprotic acid (pKa1 = 3.13, pKa2 = 4.76, pKa3 = 6.40); central metabolic intermediate of Krebs cycle.",
            "uses": "Sour flavoring agent in foods and soft drinks, metal chelating agent for limescale removal, buffer.",
            "facts": "Lemons and limes contain up to 8% citric acid by dry weight, giving citrus fruits their characteristic tart sourness.",
            "atoms": [{"el":"C","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.4,"z":0.0},{"el":"H","x":0.8,"y":1.8,"z":0.0},{"el":"C","x":0.0,"y":-0.6,"z":1.4},{"el":"C","x":0.0,"y":-2.1,"z":1.4},{"el":"O","x":1.0,"y":-2.8,"z":1.4},{"el":"O","x":-1.1,"y":-2.7,"z":1.4},{"el":"H","x":-1.0,"y":-3.7,"z":1.4},{"el":"C","x":0.0,"y":-0.6,"z":-1.4},{"el":"C","x":0.0,"y":-2.1,"z":-1.4},{"el":"O","x":1.0,"y":-2.8,"z":-1.4},{"el":"O","x":-1.1,"y":-2.7,"z":-1.4},{"el":"H","x":-1.0,"y":-3.7,"z":-1.4},{"el":"C","x":1.4,"y":-0.2,"z":0.0},{"el":"O","x":2.2,"y":0.7,"z":0.0},{"el":"O","x":1.9,"y":-1.4,"z":0.0},{"el":"H","x":2.8,"y":-1.3,"z":0.0}],
            "bonds": [[0,1,1],[1,2,1],[0,3,1],[3,4,1],[4,5,2],[4,6,1],[6,7,1],[0,8,1],[8,9,1],[9,10,2],[9,11,1],[11,12,1],[0,13,1],[13,14,2],[13,15,1],[15,16,1]]
        },
        {
            "id": "vitaminc", "name": "Vitamin C", "formula": "C₆H₈O₆", "commonName": "L-Ascorbic Acid",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "176.124 g/mol",
            "geometry": "Planar 5-membered furanone ring with dihydroxyethyl tail", "bondAngles": "108° in ring",
            "bondTypes": "Ester lactone, enediol system, C-C, C-O, O-H bonds", "numAtoms": 20, "numBonds": 20,
            "hybridization": "sp² enediol, sp³ tail", "polarity": "Highly polar (μ = 4.0 D)",
            "physicalProps": "White to light yellow crystalline solid; mp 190-192°C (decomposes); optically active [α]D = +21°.",
            "chemicalProps": "Potent water-soluble antioxidant; reversibly oxidizes to dehydroascorbic acid; essential cofactor for prolyl hydroxylase.",
            "uses": "Essential dietary vitamin (prevents scurvy), collagen synthesis, immune support, food antioxidant (E300).",
            "facts": "Humans, primates, and guinea pigs cannot synthesize their own Vitamin C due to a pseudogene mutation in the GULO enzyme gene.",
            "atoms": [{"el":"C","x":-0.7,"y":0.7,"z":0.0},{"el":"C","x":0.7,"y":0.7,"z":0.0},{"el":"C","x":1.1,"y":-0.7,"z":0.0},{"el":"O","x":-0.1,"y":-1.5,"z":0.0},{"el":"C","x":-1.2,"y":-0.7,"z":0.0},{"el":"O","x":-2.4,"y":-1.0,"z":0.0},{"el":"O","x":-1.2,"y":1.9,"z":0.0},{"el":"H","x":-2.1,"y":1.9,"z":0.0},{"el":"O","x":1.5,"y":1.7,"z":0.0},{"el":"H","x":2.4,"y":1.4,"z":0.0},{"el":"C","x":2.4,"y":-1.4,"z":0.0},{"el":"O","x":3.4,"y":-0.4,"z":0.0},{"el":"H","x":4.2,"y":-0.8,"z":0.0}],
            "bonds": [[0,1,2],[1,2,1],[2,3,1],[3,4,1],[4,0,1],[4,5,2],[0,6,1],[6,7,1],[1,8,1],[8,9,1],[2,10,1],[10,11,1],[11,12,1]]
        },
        {
            "id": "caffeine", "name": "Caffeine", "formula": "C₈H₁₀N₄O₂", "commonName": "1,3,7-Trimethylxanthine / Guaranine",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "194.19 g/mol",
            "geometry": "Planar fused bicyclic xanthine (purinedione)", "bondAngles": "120° in 6-ring, 108° in 5-ring",
            "bondTypes": "Delocalized aromatic π-cloud + 2 carbonyls + 3 methyl C-N bonds", "numAtoms": 24, "numBonds": 25,
            "hybridization": "sp² xanthine core, sp³ methyls", "polarity": "Polar (μ = 3.64 D)",
            "physicalProps": "White odorless needle crystals with bitter taste; mp 235-238°C; sublimes at 178°C at atmospheric pressure.",
            "chemicalProps": "Competitive antagonist of adenosine A1 and A2A receptors in the brain; stimulates central nervous system and cardiac muscle.",
            "uses": "World's most widely consumed psychoactive stimulant (coffee, tea, energy drinks), analgesic adjuvant in headache pills.",
            "facts": "Plants produce caffeine as a natural pesticide to paralyze and kill predatory insects chewing on their leaves and beans.",
            "atoms": [{"el":"C","x":0.0,"y":1.4,"z":0.0},{"el":"N","x":1.2,"y":0.7,"z":0.0},{"el":"C","x":1.2,"y":-0.7,"z":0.0},{"el":"O","x":2.3,"y":-1.3,"z":0.0},{"el":"N","x":0.0,"y":-1.4,"z":0.0},{"el":"C","x":-1.2,"y":-0.7,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"O","x":-2.3,"y":1.3,"z":0.0},{"el":"C","x":2.4,"y":1.4,"z":0.0},{"el":"C","x":0.0,"y":-2.8,"z":0.0},{"el":"N","x":-2.4,"y":-1.3,"z":0.0},{"el":"C","x":-3.2,"y":-0.3,"z":0.0},{"el":"N","x":-2.5,"y":0.9,"z":0.0},{"el":"C","x":-3.0,"y":2.2,"z":0.0}],
            "bonds": [[0,1,1],[1,2,1],[2,3,2],[2,4,1],[4,5,1],[5,6,2],[6,0,1],[6,7,2],[1,8,1],[4,9,1],[5,10,1],[10,11,1],[11,12,2],[12,6,1],[12,13,1]]
        },
        {
            "id": "serotonin", "name": "Serotonin", "formula": "C₁₀H₁₂N₂O", "commonName": "5-Hydroxytryptamine / 5-HT",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "176.215 g/mol",
            "geometry": "Planar indole bicyclic ring with aminoethyl side chain", "bondAngles": "120° 6-ring, 108° 5-ring",
            "bondTypes": "Aromatic π system, C-C, C-N, C-O, O-H, N-H σ bonds", "numAtoms": 25, "numBonds": 26,
            "hybridization": "sp² indole, sp³ side chain", "polarity": "Polar (μ = 2.9 D)",
            "physicalProps": "White to off-white crystalline solid; mp 215°C (decomposes); sensitive to light and oxidation.",
            "chemicalProps": "Monoamine neurotransmitter synthesized from L-tryptophan; oxidized by monoamine oxidase (MAO-A).",
            "uses": "Regulation of mood, cognition, reward, learning, memory, sleep, and bowel motility.",
            "facts": "Roughly 90% of the entire body's serotonin is synthesized and stored in the gastrointestinal tract, where it regulates bowel motility.",
            "atoms": [{"el":"C","x":-2.8,"y":0.7,"z":0.0},{"el":"C","x":-1.5,"y":1.3,"z":0.0},{"el":"C","x":-0.3,"y":0.6,"z":0.0},{"el":"C","x":-0.3,"y":-0.8,"z":0.0},{"el":"C","x":-1.6,"y":-1.4,"z":0.0},{"el":"C","x":-2.8,"y":-0.7,"z":0.0},{"el":"O","x":-4.0,"y":1.4,"z":0.0},{"el":"H","x":-4.8,"y":0.8,"z":0.0},{"el":"N","x":1.0,"y":-1.3,"z":0.0},{"el":"C","x":1.8,"y":-0.2,"z":0.0},{"el":"C","x":1.0,"y":0.9,"z":0.0},{"el":"C","x":1.6,"y":2.3,"z":0.0},{"el":"C","x":3.1,"y":2.2,"z":0.0},{"el":"N","x":3.8,"y":3.5,"z":0.0}],
            "bonds": [[0,1,1],[1,2,2],[2,3,1],[3,4,2],[4,5,1],[5,0,2],[0,6,1],[6,7,1],[3,8,1],[8,9,1],[9,10,2],[10,2,1],[10,11,1],[11,12,1],[12,13,1]]
        },
        {
            "id": "dopamine", "name": "Dopamine", "formula": "C₈H₁₁NO₂", "commonName": "4-(2-Aminoethyl)benzene-1,2-diol / DA",
            "category": "Biochemical Molecules", "categoryKey": "biochemical", "mw": "153.18 g/mol",
            "geometry": "Planar catechol ring with flexible aminoethyl chain", "bondAngles": "120° ring, 109.5° chain",
            "bondTypes": "Aromatic π system, phenolic C-O and O-H bonds, aliphatic C-C, C-N bonds", "numAtoms": 22, "numBonds": 22,
            "hybridization": "sp² ring, sp³ chain", "polarity": "Polar (μ = 2.9 D)",
            "physicalProps": "White crystalline solid; mp 128°C; readily oxidizes in air to dark dopachrome pigments.",
            "chemicalProps": "Catecholamine neurotransmitter synthesized from L-DOPA; precursor to norepinephrine and epinephrine.",
            "uses": "Neurological reward pathway, motivation, motor control coordination, intravenous treatment for septic shock.",
            "facts": "Parkinson's disease is caused by the progressive death of dopamine-generating neurons in the substantia nigra pars compacta region of the midbrain.",
            "atoms": [{"el":"C","x":-1.8,"y":1.2,"z":0.0},{"el":"C","x":-0.5,"y":1.2,"z":0.0},{"el":"C","x":0.2,"y":0.0,"z":0.0},{"el":"C","x":-0.5,"y":-1.2,"z":0.0},{"el":"C","x":-1.8,"y":-1.2,"z":0.0},{"el":"C","x":-2.5,"y":0.0,"z":0.0},{"el":"O","x":-2.5,"y":2.4,"z":0.0},{"el":"H","x":-3.4,"y":2.2,"z":0.0},{"el":"O","x":-0.2,"y":2.4,"z":0.0},{"el":"H","x":0.7,"y":2.2,"z":0.0},{"el":"C","x":1.7,"y":0.0,"z":0.0},{"el":"C","x":2.4,"y":-1.3,"z":0.0},{"el":"N","x":3.8,"y":-1.2,"z":0.0}],
            "bonds": [[0,1,2],[1,2,1],[2,3,2],[3,4,1],[4,5,2],[5,0,1],[0,6,1],[6,7,1],[1,8,1],[8,9,1],[2,10,1],[10,11,1],[11,12,1]]
        }
    ]

def get_biochem_molecules():
    return get_biochem_part1() + get_biochem_part2()
