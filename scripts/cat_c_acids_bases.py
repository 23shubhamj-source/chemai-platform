# Category C: Acids and Bases (Part 1)
def get_acids_part1():
    return [
        {
            "id": "hcl", "name": "Hydrochloric Acid", "formula": "HCl", "commonName": "Muriatic Acid",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "36.458 g/mol",
            "geometry": "Linear", "bondAngles": "180°", "bondTypes": "Polar covalent σ bond",
            "numAtoms": 2, "numBonds": 1, "hybridization": "Unhybridized", "polarity": "Polar (μ = 1.08 D)",
            "physicalProps": "Colorless pungent fuming solution; bp -85°C (pure gas); density 1.18 g/cm³ (37%).",
            "chemicalProps": "Strong monoprotic mineral acid (pKa = -6.3); completely dissociates in water: HCl → H⁺ + Cl⁻.",
            "uses": "Steel pickling, stomach gastric acid for digestion, PVC production, pH control in pools.",
            "facts": "Human stomach parietal cells secrete ~2 liters of gastric juice daily containing 0.5% hydrochloric acid.",
            "atoms": [{"el":"Cl","x":0.28,"y":0.0,"z":0.0},{"el":"H","x":-1.00,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1]]
        },
        {
            "id": "h2so4", "name": "Sulfuric Acid", "formula": "H₂SO₄", "commonName": "Oil of Vitriol",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "98.079 g/mol",
            "geometry": "Tetrahedral around Sulfur", "bondAngles": "O=S=O ~119°, O-S-O ~104°",
            "bondTypes": "2 S=O double bonds, 2 S-O single bonds, 2 O-H bonds", "numAtoms": 7, "numBonds": 6,
            "hybridization": "sp³ at Sulfur", "polarity": "Polar (μ = 2.7 D)",
            "physicalProps": "Dense, colorless oily liquid; mp 10.3°C, bp 337°C; density 1.84 g/cm³; highly exothermic hydration.",
            "chemicalProps": "Strong diprotic acid (pKa1 = -3, pKa2 = 1.99); powerful dehydrating and oxidizing agent.",
            "uses": "Phosphate fertilizer manufacturing, lead-acid car batteries, petroleum refining, chemical synthesis.",
            "facts": "Sulfuric acid production is so fundamental to modern manufacturing that it is considered a barometer of a nation's industrial strength.",
            "atoms": [{"el":"S","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.42,"z":0.0},{"el":"O","x":0.0,"y":-1.42,"z":0.0},{"el":"O","x":1.35,"y":0.0,"z":0.7},{"el":"O","x":-1.35,"y":0.0,"z":-0.7},{"el":"H","x":2.0,"y":0.0,"z":0.1},{"el":"H","x":-2.0,"y":0.0,"z":-0.1}],
            "bonds": [[0,1,2],[0,2,2],[0,3,1],[0,4,1],[3,5,1],[4,6,1]]
        },
        {
            "id": "hno3", "name": "Nitric Acid", "formula": "HNO₃", "commonName": "Aqua Fortis",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "63.012 g/mol",
            "geometry": "Planar around Nitrogen", "bondAngles": "O=N=O 130°, O-N-OH 115°",
            "bondTypes": "Resonant N=O and N-O bonds + O-H σ bond", "numAtoms": 5, "numBonds": 4,
            "hybridization": "sp² at Nitrogen", "polarity": "Polar (μ = 2.17 D)",
            "physicalProps": "Colorless to yellow-brown fuming liquid; mp -42°C, bp 83°C; turns yellow due to NO₂.",
            "chemicalProps": "Strong monoprotic acid (pKa = -1.4) and powerful oxidizer; oxidizes copper and silver.",
            "uses": "Ammonium nitrate fertilizer, explosives (TNT, nitroglycerin), rocket hypergolic propellant, etching.",
            "facts": "Nitric acid mixed 1:3 with hydrochloric acid forms aqua regia, one of the few mixtures capable of dissolving metallic gold and platinum.",
            "atoms": [{"el":"N","x":0.0,"y":0.2,"z":0.0},{"el":"O","x":-1.1,"y":-0.3,"z":0.0},{"el":"O","x":1.1,"y":-0.3,"z":0.0},{"el":"O","x":0.0,"y":1.4,"z":0.0},{"el":"H","x":-1.8,"y":0.3,"z":0.0}],
            "bonds": [[0,1,1],[0,2,2],[0,3,1],[1,4,1]]
        },
        {
            "id": "h3po4", "name": "Phosphoric Acid", "formula": "H₃PO₄", "commonName": "Orthophosphoric Acid",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "97.994 g/mol",
            "geometry": "Tetrahedral around Phosphorus", "bondAngles": "O=P-O 112°, O-P-O 106°",
            "bondTypes": "1 P=O bond, 3 P-O-H single bonds", "numAtoms": 8, "numBonds": 7,
            "hybridization": "sp³ at Phosphorus", "polarity": "Polar",
            "physicalProps": "White crystalline solid or 85% viscous aqueous syrup; mp 42.4°C, bp 158°C.",
            "chemicalProps": "Triprotic acid (pKa1 = 2.15, pKa2 = 7.20, pKa3 = 12.35); non-oxidizing acid.",
            "uses": "Cola beverage acidulant (tangy flavor), triple superphosphate fertilizer, rust removal.",
            "facts": "Phosphoric acid provides the distinctive tart bite in cola drinks and stops mold growth in syrups.",
            "atoms": [{"el":"P","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.5,"z":0.0},{"el":"O","x":1.4,"y":-0.5,"z":0.0},{"el":"O","x":-0.7,"y":-0.5,"z":1.2},{"el":"O","x":-0.7,"y":-0.5,"z":-1.2},{"el":"H","x":2.1,"y":0.0,"z":0.0},{"el":"H","x":-1.0,"y":0.0,"z":1.8},{"el":"H","x":-1.0,"y":0.0,"z":-1.8}],
            "bonds": [[0,1,2],[0,2,1],[0,3,1],[0,4,1],[2,5,1],[3,6,1],[4,7,1]]
        },
        {
            "id": "h2co3", "name": "Carbonic Acid", "formula": "H₂CO₃", "commonName": "Acid of Air",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "62.024 g/mol",
            "geometry": "Planar at Carbon", "bondAngles": "O=C-O 120°",
            "bondTypes": "1 C=O double bond, 2 C-O single bonds, 2 O-H bonds", "numAtoms": 6, "numBonds": 5,
            "hybridization": "sp² at Carbon", "polarity": "Polar (μ = 1.5 D)",
            "physicalProps": "Exists in aqueous equilibrium with CO₂; cannot be concentrated as a pure liquid at room temperature.",
            "chemicalProps": "Weak diprotic acid (pKa1 = 6.35, pKa2 = 10.33); essential physiological blood buffer.",
            "uses": "Human blood pH homeostasis (7.35-7.45 buffer system), effervescence in carbonated water.",
            "facts": "The carbonic acid - bicarbonate blood buffer maintains our blood pH strictly within 7.35 to 7.45; any shift outside 6.8 - 7.8 is fatal.",
            "atoms": [{"el":"C","x":0.0,"y":0.14,"z":0.0},{"el":"O","x":0.0,"y":1.36,"z":0.0},{"el":"O","x":-1.15,"y":-0.6,"z":0.0},{"el":"O","x":1.15,"y":-0.6,"z":0.0},{"el":"H","x":-1.8,"y":-0.1,"z":0.0},{"el":"H","x":1.8,"y":-0.1,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1],[0,3,1],[2,4,1],[3,5,1]]
        },
        {
            "id": "formicacid", "name": "Formic Acid", "formula": "HCOOH", "commonName": "Methanoic Acid",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "46.025 g/mol",
            "geometry": "Planar around Carbon", "bondAngles": "O=C-O 125°, H-C=O 122°",
            "bondTypes": "C=O, C-O, O-H, C-H σ bonds", "numAtoms": 5, "numBonds": 4,
            "hybridization": "sp²", "polarity": "Polar (μ = 1.41 D)",
            "physicalProps": "Colorless liquid with pungent vinegar-like odor; mp 8.4°C, bp 100.8°C; density 1.22 g/cm³.",
            "chemicalProps": "Simplest carboxylic acid (pKa = 3.75); reduces ammoniacal silver nitrate (has aldehyde character).",
            "uses": "Silage and animal feed antibacterial preservative, leather tanning, latex coagulation.",
            "facts": "Formic acid gets its name from Formica (Latin for ant) because it was first isolated in 1671 by distilling crushed red ants.",
            "atoms": [{"el":"C","x":0.0,"y":0.15,"z":0.0},{"el":"O","x":0.0,"y":1.35,"z":0.0},{"el":"O","x":1.1,"y":-0.6,"z":0.0},{"el":"H","x":1.8,"y":-0.1,"z":0.0},{"el":"H","x":-1.0,"y":-0.4,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1],[2,3,1],[0,4,1]]
        },
        {
            "id": "hf", "name": "Hydrofluoric Acid", "formula": "HF", "commonName": "Hydrogen Fluoride",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "20.006 g/mol",
            "geometry": "Linear", "bondAngles": "180°", "bondTypes": "Extremely polar covalent σ bond",
            "numAtoms": 2, "numBonds": 1, "hybridization": "Unhybridized", "polarity": "Highly polar (μ = 1.83 D)",
            "physicalProps": "Colorless volatile liquid or gas; mp -83.6°C, bp 19.5°C; forms strong hydrogen-bonded zig-zag chains.",
            "chemicalProps": "Weak acid in dilute aqueous solution (pKa = 3.17) due to high H-F bond strength (567 kJ/mol); dissolves silicate glass: SiO₂ + 4HF → SiF₄ + 2H₂O.",
            "uses": "Semiconductor silicon wafer etching, glass etching, uranium hexafluoride nuclear enrichment.",
            "facts": "HF penetrates human skin and leaches systemic calcium ions (Ca²⁺) from bones and cardiac tissue, causing fatal hypocalcemia.",
            "atoms": [{"el":"F","x":0.10,"y":0.0,"z":0.0},{"el":"H","x":-0.82,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1]]
        }
    ]

# Category C: Acids and Bases (Part 2)
def get_acids_part2():
    return [
        {
            "id": "hclo4", "name": "Perchloric Acid", "formula": "HClO₄", "commonName": "Perchloric Acid",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "100.46 g/mol",
            "geometry": "Tetrahedral around Chlorine", "bondAngles": "O=Cl=O ~112°",
            "bondTypes": "3 Cl=O bonds + 1 Cl-O-H single bond", "numAtoms": 6, "numBonds": 5,
            "hybridization": "sp³ at Chlorine", "polarity": "Polar (μ = 2.0 D)",
            "physicalProps": "Colorless fuming aqueous liquid; density 1.76 g/cm³; powerful oxidizer when heated.",
            "chemicalProps": "One of the strongest Brønsted-Lowry acids known (pKa ≈ -10); perchlorate ClO₄⁻ is a non-coordinating anion.",
            "uses": "Ammonium perchlorate solid rocket fuel oxidizer, etching chrome, chemical analysis.",
            "facts": "Anhydrous perchloric acid is so reactive that contact with paper, wood, or grease causes instantaneous violent explosion.",
            "atoms": [{"el":"Cl","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.45,"z":0.0},{"el":"O","x":1.4,"y":-0.5,"z":0.0},{"el":"O","x":-1.4,"y":-0.5,"z":0.0},{"el":"O","x":0.0,"y":0.0,"z":1.5},{"el":"H","x":0.0,"y":0.0,"z":2.4}],
            "bonds": [[0,1,2],[0,2,2],[0,3,2],[0,4,1],[4,5,1]]
        },
        {
            "id": "naoh", "name": "Sodium Hydroxide", "formula": "NaOH", "commonName": "Caustic Soda / Lye",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "39.997 g/mol",
            "geometry": "Linear ion pair / Crystal lattice", "bondAngles": "180°",
            "bondTypes": "Ionic bond Na⁺···⁻OH, covalent O-H bond", "numAtoms": 3, "numBonds": 2,
            "hybridization": "sp³ at Oxygen", "polarity": "Extremely polar (ionic salt)",
            "physicalProps": "White deliquescent waxy pellets or flakes; mp 323°C, bp 1388°C; highly exothermic dissolution.",
            "chemicalProps": "Strong monoprotic base (pKb = 0.2); attacks glass to form sodium silicate; absorbs atmospheric CO₂.",
            "uses": "Soap and detergent manufacture (saponification), paper pulping (Kraft process), drain cleaner.",
            "facts": "NaOH dissolves biological fats into water-soluble soap via alkaline ester hydrolysis (saponification).",
            "atoms": [{"el":"Na","x":-1.3,"y":0.0,"z":0.0},{"el":"O","x":0.8,"y":0.0,"z":0.0},{"el":"H","x":1.75,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1],[1,2,1]]
        },
        {
            "id": "koh", "name": "Potassium Hydroxide", "formula": "KOH", "commonName": "Caustic Potash",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "56.106 g/mol",
            "geometry": "Linear ion pair", "bondAngles": "180°",
            "bondTypes": "Ionic bond K⁺···⁻OH, covalent O-H bond", "numAtoms": 3, "numBonds": 2,
            "hybridization": "sp³ at Oxygen", "polarity": "Extremely polar (ionic)",
            "physicalProps": "White translucent solid pellets; mp 360°C, bp 1327°C; more soluble in alcohol than NaOH.",
            "chemicalProps": "Strong base (pKb = 0.5); hygroscopic; reacts with acids to form potassium salts.",
            "uses": "Electrolyte in alkaline batteries, soft liquid soap manufacturing, chemical etching of silicon.",
            "facts": "KOH is the preferred electrolyte in alkaline batteries because potassium ions conduct charge faster than sodium ions in water.",
            "atoms": [{"el":"K","x":-1.5,"y":0.0,"z":0.0},{"el":"O","x":0.9,"y":0.0,"z":0.0},{"el":"H","x":1.85,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1],[1,2,1]]
        },
        {
            "id": "caoh2", "name": "Calcium Hydroxide", "formula": "Ca(OH)₂", "commonName": "Slaked Lime / Pickling Lime",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "74.093 g/mol",
            "geometry": "Linear coordination Ca with two OH", "bondAngles": "180°",
            "bondTypes": "Ionic Ca²⁺ with two OH⁻ anions", "numAtoms": 5, "numBonds": 4,
            "hybridization": "Ionic lattice", "polarity": "Polar (ionic salt)",
            "physicalProps": "White odorless powder; decomposes at 580°C to CaO and H₂O; retro-grade solubility in water.",
            "chemicalProps": "Strong base (saturated solution pH ~ 12.4); reacts with CO₂ to precipitate white CaCO₃ (limewater test).",
            "uses": "Mortar in construction, municipal water flocculation, flue gas desulfurization, dental pulp capping.",
            "facts": "Calcium hydroxide displays retrograde solubility—unusually, it dissolves LESS in hot water than in cold water.",
            "atoms": [{"el":"Ca","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":-1.8,"y":0.0,"z":0.0},{"el":"H","x":-2.7,"y":0.0,"z":0.0},{"el":"O","x":1.8,"y":0.0,"z":0.0},{"el":"H","x":2.7,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1],[1,2,1],[0,3,1],[3,4,1]]
        },
        {
            "id": "mgoh2", "name": "Magnesium Hydroxide", "formula": "Mg(OH)₂", "commonName": "Milk of Magnesia",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "58.320 g/mol",
            "geometry": "Cadmium iodide crystal structure", "bondAngles": "180°",
            "bondTypes": "Ionic Mg²⁺···2OH⁻", "numAtoms": 5, "numBonds": 4,
            "hybridization": "Ionic lattice", "polarity": "Polar ionic",
            "physicalProps": "White crystalline powder or suspension; low water solubility (0.009 g/L at 18°C); mp 350°C (decomposes).",
            "chemicalProps": "Mild base; safely neutralizes excess stomach acid: Mg(OH)₂ + 2HCl → MgCl₂ + 2H₂O.",
            "uses": "Antacid and laxative (Milk of Magnesia), flame retardant in plastics and electrical cables.",
            "facts": "Because magnesium hydroxide is so poorly soluble in water, it creates a mild non-corrosive pH ~10 that can be ingested safely.",
            "atoms": [{"el":"Mg","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":-1.6,"y":0.0,"z":0.0},{"el":"H","x":-2.5,"y":0.0,"z":0.0},{"el":"O","x":1.6,"y":0.0,"z":0.0},{"el":"H","x":2.5,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1],[1,2,1],[0,3,1],[3,4,1]]
        },
        {
            "id": "nh4oh", "name": "Ammonium Hydroxide", "formula": "NH₄OH", "commonName": "Amonia Solution / Household Ammonia",
            "category": "Acids & Bases", "categoryKey": "acids-bases", "mw": "35.046 g/mol",
            "geometry": "Tetrahedral NH₄⁺ + OH⁻", "bondAngles": "109.5° around N",
            "bondTypes": "Coordinate covalent and ionic hydrogen bonded network", "numAtoms": 7, "numBonds": 5,
            "hybridization": "sp³ at N", "polarity": "Polar (μ = 1.47 D)",
            "physicalProps": "Colorless liquid with intense suffocating odor; bp 24.7°C (28% aqueous solution); density 0.90 g/cm³.",
            "chemicalProps": "Weak base in water (Kb = 1.8 × 10⁻⁵); dissolves insoluble metal hydroxides by forming coordination amine complexes.",
            "uses": "Household glass cleaner, textile processing, chemical fertilizer manufacture, darkroom chemistry.",
            "facts": "Pure isolated NH₄OH does not exist as an independent molecule in anhydrous form—it is a hydrated solution of NH₃ in water.",
            "atoms": [{"el":"N","x":-0.8,"y":0.0,"z":0.0},{"el":"H","x":-1.4,"y":0.8,"z":0.0},{"el":"H","x":-1.4,"y":-0.8,"z":0.0},{"el":"H","x":-0.8,"y":0.0,"z":1.0},{"el":"H","x":0.1,"y":0.0,"z":0.0},{"el":"O","x":1.5,"y":0.0,"z":0.0},{"el":"H","x":2.1,"y":0.7,"z":0.0}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1],[0,4,1],[5,6,1]]
        }
    ]

def get_acids_molecules():
    return get_acids_part1() + get_acids_part2()
