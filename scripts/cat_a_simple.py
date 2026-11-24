# Category A: Simple Molecules (12)
def get_simple_molecules():
    return [
        {
            "id": "water", "name": "Water", "formula": "H₂O", "commonName": "Dihydrogen Monoxide",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "18.015 g/mol",
            "geometry": "Bent (~104.5°)", "bondAngles": "104.45°", "bondTypes": "Polar covalent σ bonds",
            "numAtoms": 3, "numBonds": 2, "hybridization": "sp³", "polarity": "Polar (μ = 1.85 D)",
            "physicalProps": "Colorless liquid; mp 0°C, bp 100°C; density 1.00 g/cm³; specific heat 4.184 J/g·K.",
            "chemicalProps": "Amphoteric; autoionizes Kw = 1.0 × 10⁻¹⁴; forms extensive hydrogen-bonding network.",
            "uses": "Universal solvent in biology and chemical syntheses, industrial coolant, density standard.",
            "facts": "Solid ice is less dense than liquid water due to hexagonal open lattice hydrogen bonding.",
            "atoms": [{"el":"O","x":0.0,"y":0.0,"z":0.0},{"el":"H","x":-0.757,"y":0.586,"z":0.0},{"el":"H","x":0.757,"y":0.586,"z":0.0}],
            "bonds": [[0,1,1],[0,2,1]]
        },
        {
            "id": "hydrogen", "name": "Hydrogen Gas", "formula": "H₂", "commonName": "Molecular Hydrogen",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "2.016 g/mol",
            "geometry": "Linear", "bondAngles": "180°", "bondTypes": "Non-polar covalent σ bond",
            "numAtoms": 2, "numBonds": 1, "hybridization": "1s-1s overlap", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless, odorless gas; mp -259.16°C, bp -252.87°C; density 0.089 g/L at STP.",
            "chemicalProps": "Highly flammable; burns in oxygen: 2H₂ + O₂ → 2H₂O; strong reducing agent.",
            "uses": "Haber-Bosch ammonia synthesis, fuel cells, petroleum hydrotreating, rocket fuel.",
            "facts": "Accounts for 75% of all normal matter in the universe and was formed right after the Big Bang.",
            "atoms": [{"el":"H","x":-0.37,"y":0.0,"z":0.0},{"el":"H","x":0.37,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1]]
        },
        {
            "id": "oxygen", "name": "Oxygen Gas", "formula": "O₂", "commonName": "Dioxygen",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "31.998 g/mol",
            "geometry": "Linear", "bondAngles": "180°", "bondTypes": "Covalent double bond (1 σ + 1 π)",
            "numAtoms": 2, "numBonds": 1, "hybridization": "sp²", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless gas, pale blue cryogenic liquid; mp -218.79°C, bp -182.96°C; density 1.429 g/L.",
            "chemicalProps": "Paramagnetic ground state with 2 unpaired electrons in π* orbitals; powerful oxidizer.",
            "uses": "Aerobic respiration, hospital oxygen therapy, steelmaking basic oxygen furnace, rocket propulsion.",
            "facts": "Liquid oxygen is visibly magnetic and will stick between the poles of a strong neodymium magnet.",
            "atoms": [{"el":"O","x":-0.605,"y":0.0,"z":0.0},{"el":"O","x":0.605,"y":0.0,"z":0.0}],
            "bonds": [[0,1,2]]
        },
        {
            "id": "nitrogen", "name": "Nitrogen Gas", "formula": "N₂", "commonName": "Dinitrogen",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "28.014 g/mol",
            "geometry": "Linear", "bondAngles": "180°", "bondTypes": "Covalent triple bond (1 σ + 2 π)",
            "numAtoms": 2, "numBonds": 1, "hybridization": "sp", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless, odorless gas; mp -210.0°C, bp -195.79°C; density 1.251 g/L.",
            "chemicalProps": "Chemically inert at room temperature due to huge triple bond energy (945 kJ/mol).",
            "uses": "Inert blanket in food packaging, cryogenic preservation, ammonia manufacturing.",
            "facts": "Makes up 78.08% of Earth's atmosphere, moderating combustion and oxidation on our planet.",
            "atoms": [{"el":"N","x":-0.55,"y":0.0,"z":0.0},{"el":"N","x":0.55,"y":0.0,"z":0.0}],
            "bonds": [[0,1,3]]
        },
        {
            "id": "carbondioxide", "name": "Carbon Dioxide", "formula": "CO₂", "commonName": "Dry Ice (solid)",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "44.009 g/mol",
            "geometry": "Linear", "bondAngles": "180°", "bondTypes": "Two polar covalent double bonds",
            "numAtoms": 3, "numBonds": 2, "hybridization": "sp", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless odorless gas; sublimes directly at -78.5°C at 1 atm without melting; density 1.977 g/L.",
            "chemicalProps": "Acidic oxide; dissolves in water producing carbonic acid; turns lime water milky.",
            "uses": "Photosynthesis substrate, carbonated drinks, fire extinguishers, supercritical extraction.",
            "facts": "Supercritical CO₂ is widely used as a non-toxic green solvent to decaffeinate coffee beans.",
            "atoms": [{"el":"C","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":-1.16,"y":0.0,"z":0.0},{"el":"O","x":1.16,"y":0.0,"z":0.0}],
            "bonds": [[0,1,2],[0,2,2]]
        },
        {
            "id": "carbonmonoxide", "name": "Carbon Monoxide", "formula": "CO", "commonName": "Carbon Oxide",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "28.010 g/mol",
            "geometry": "Linear", "bondAngles": "180°", "bondTypes": "Triple bond with coordinate covalent bond",
            "numAtoms": 2, "numBonds": 1, "hybridization": "sp", "polarity": "Slightly polar (μ = 0.122 D)",
            "physicalProps": "Colorless, odorless, highly toxic gas; mp -205.0°C, bp -191.5°C.",
            "chemicalProps": "Strong field ligand forming metal carbonyls; binds hemoglobin with 200× affinity of O₂.",
            "uses": "Syngas production (Fischer-Tropsch), blast furnace iron reduction, industrial acetic acid synthesis.",
            "facts": "Carbon monoxide toxicity occurs because carboxyhemoglobin cannot release oxygen to tissues.",
            "atoms": [{"el":"C","x":-0.564,"y":0.0,"z":0.0},{"el":"O","x":0.564,"y":0.0,"z":0.0}],
            "bonds": [[0,1,3]]
        },
        {
            "id": "ozone", "name": "Ozone", "formula": "O₃", "commonName": "Trioxygen",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "47.997 g/mol",
            "geometry": "Bent", "bondAngles": "116.8°", "bondTypes": "Resonant covalent bonds (order 1.5)",
            "numAtoms": 3, "numBonds": 2, "hybridization": "sp²", "polarity": "Polar (μ = 0.53 D)",
            "physicalProps": "Pale blue gas with sharp chlorine-like odor; mp -192.2°C, bp -111.9°C.",
            "chemicalProps": "Powerful oxidizing agent (E° = +2.07 V); cleaves alkenes in ozonolysis; decomposes to O₂.",
            "uses": "Stratospheric UV shield, municipal drinking water ozonation, organic synthesis.",
            "facts": "The ozone layer filters 97-99% of damaging solar UV-B rays, protecting terrestrial organisms.",
            "atoms": [{"el":"O","x":0.0,"y":0.387,"z":0.0},{"el":"O","x":-1.088,"y":-0.194,"z":0.0},{"el":"O","x":1.088,"y":-0.194,"z":0.0}],
            "bonds": [[0,1,1],[0,2,2]]
        },
        {
            "id": "ammonia", "name": "Ammonia", "formula": "NH₃", "commonName": "Azane",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "17.031 g/mol",
            "geometry": "Trigonal Pyramidal", "bondAngles": "107.8°", "bondTypes": "Polar covalent σ bonds",
            "numAtoms": 4, "numBonds": 3, "hybridization": "sp³", "polarity": "Polar (μ = 1.47 D)",
            "physicalProps": "Colorless pungent gas; mp -77.73°C, bp -33.34°C; extremely water soluble.",
            "chemicalProps": "Brønsted-Lowry base (pKb = 4.75); undergoes quantum umbrella inversion at 24 GHz.",
            "uses": "Nitrogen fertilizers (urea, ammonium nitrate), nitric acid manufacture, refrigeration.",
            "facts": "The quantum umbrella inversion of ammonia was used in 1949 to construct the world's first atomic clock.",
            "atoms": [{"el":"N","x":0.0,"y":0.0,"z":0.116},{"el":"H","x":0.0,"y":0.940,"z":-0.271},{"el":"H","x":-0.814,"y":-0.470,"z":-0.271},{"el":"H","x":0.814,"y":-0.470,"z":-0.271}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1]]
        },
        {
            "id": "methane", "name": "Methane", "formula": "CH₄", "commonName": "Natural Gas",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "16.043 g/mol",
            "geometry": "Tetrahedral", "bondAngles": "109.5°", "bondTypes": "Covalent C-H σ bonds",
            "numAtoms": 5, "numBonds": 4, "hybridization": "sp³", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless, odorless gas; mp -182.5°C, bp -161.5°C; density 0.717 g/L.",
            "chemicalProps": "Combusts completely: CH₄ + 2O₂ → CO₂ + 2H₂O; free-radical halogenation with Cl₂.",
            "uses": "Clean-burning fuel in heating, power generation, steam methane reforming for hydrogen.",
            "facts": "Methane is 28× more potent than CO₂ as a greenhouse gas over a 100-year timescale.",
            "atoms": [{"el":"C","x":0.0,"y":0.0,"z":0.0},{"el":"H","x":0.629,"y":0.629,"z":0.629},{"el":"H","x":-0.629,"y":-0.629,"z":0.629},{"el":"H","x":-0.629,"y":0.629,"z":-0.629},{"el":"H","x":0.629,"y":-0.629,"z":-0.629}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1],[0,4,1]]
        },
        {
            "id": "ethane", "name": "Ethane", "formula": "C₂H₆", "commonName": "Dimethyl",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "30.070 g/mol",
            "geometry": "Tetrahedral at each carbon", "bondAngles": "109.5°", "bondTypes": "C-C and C-H σ bonds",
            "numAtoms": 8, "numBonds": 7, "hybridization": "sp³", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless odorless flammable gas; mp -182.8°C, bp -88.5°C.",
            "chemicalProps": "Staggered conformer is 12.6 kJ/mol lower than eclipsed; steam-cracked to ethylene.",
            "uses": "Petrochemical feedstock for ethylene manufacturing, refrigerant gas, fuel.",
            "facts": "Michael Faraday first synthesized ethane in 1834 by electrolyzing potassium acetate.",
            "atoms": [{"el":"C","x":-0.763,"y":0.0,"z":0.0},{"el":"C","x":0.763,"y":0.0,"z":0.0},{"el":"H","x":-1.16,"y":1.02,"z":0.0},{"el":"H","x":-1.16,"y":-0.51,"z":0.88},{"el":"H","x":-1.16,"y":-0.51,"z":-0.88},{"el":"H","x":1.16,"y":-1.02,"z":0.0},{"el":"H","x":1.16,"y":0.51,"z":0.88},{"el":"H","x":1.16,"y":0.51,"z":-0.88}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1],[0,4,1],[1,5,1],[1,6,1],[1,7,1]]
        },
        {
            "id": "ethene", "name": "Ethene", "formula": "C₂H₄", "commonName": "Ethylene",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "28.054 g/mol",
            "geometry": "Planar", "bondAngles": "121.3°", "bondTypes": "C=C double bond (1 σ + 1 π) + 4 C-H σ bonds",
            "numAtoms": 6, "numBonds": 5, "hybridization": "sp²", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless gas with sweet aroma; mp -169.2°C, bp -103.7°C.",
            "chemicalProps": "Electrophilic additions across double bond; polymerizes to polyethylene.",
            "uses": "Production of polyethylene, ethylene oxide, natural fruit-ripening hormone in agriculture.",
            "facts": "Ripening bananas naturally release ethene, which can be used to accelerate tomato ripening.",
            "atoms": [{"el":"C","x":-0.669,"y":0.0,"z":0.0},{"el":"C","x":0.669,"y":0.0,"z":0.0},{"el":"H","x":-1.235,"y":0.928,"z":0.0},{"el":"H","x":-1.235,"y":-0.928,"z":0.0},{"el":"H","x":1.235,"y":0.928,"z":0.0},{"el":"H","x":1.235,"y":-0.928,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1],[0,3,1],[1,4,1],[1,5,1]]
        },
        {
            "id": "ethyne", "name": "Ethyne", "formula": "C₂H₂", "commonName": "Acetylene",
            "category": "Simple Molecules", "categoryKey": "simple", "mw": "26.038 g/mol",
            "geometry": "Linear", "bondAngles": "180°", "bondTypes": "C≡C triple bond (1 σ + 2 π) + 2 C-H σ bonds",
            "numAtoms": 4, "numBonds": 3, "hybridization": "sp", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless gas; sublimes at -84°C at 1 atm.",
            "chemicalProps": "Weakly acidic terminal protons (pKa ~ 25); burns at 3300°C in oxygen.",
            "uses": "Oxy-acetylene cutting and welding torches, synthesis of vinyl chloride and neoprene.",
            "facts": "Oxy-acetylene produces the hottest known chemical gas flame, exceeding 3,330°C.",
            "atoms": [{"el":"C","x":-0.60,"y":0.0,"z":0.0},{"el":"C","x":0.60,"y":0.0,"z":0.0},{"el":"H","x":-1.66,"y":0.0,"z":0.0},{"el":"H","x":1.66,"y":0.0,"z":0.0}],
            "bonds": [[0,1,3],[0,2,1],[1,3,1]]
        }
    ]
