# Category D: Important Inorganic Compounds (Part 1)
def get_inorganic_part1():
    return [
        {
            "id": "nacl", "name": "Sodium Chloride", "formula": "NaCl", "commonName": "Table Salt / Halite",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "58.443 g/mol",
            "geometry": "Face-Centered Cubic (FCC) Lattice", "bondAngles": "90° & 180°",
            "bondTypes": "Ionic bond Na⁺···Cl⁻ (lattice energy 787 kJ/mol)", "numAtoms": 2, "numBonds": 1,
            "hybridization": "Ionic crystal", "polarity": "Extremely polar (ionic)",
            "physicalProps": "White crystalline cubic solid; mp 801°C, bp 1413°C; density 2.165 g/cm³; refractive index 1.544.",
            "chemicalProps": "Neutral salt in water (pH = 7.0); electrolyzed via chlor-alkali process to yield Cl₂, H₂, and NaOH.",
            "uses": "Essential dietary electrolyte, road de-icing salt, food preservation curing, chemical chlor-alkali feedstock.",
            "facts": "In ancient Rome, salt was so valuable that soldiers were sometimes paid in salt rations—the origin of the modern word 'salary'.",
            "atoms": [{"el":"Na","x":-1.18,"y":0.0,"z":0.0},{"el":"Cl","x":1.18,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1]]
        },
        {
            "id": "caco3", "name": "Calcium Carbonate", "formula": "CaCO₃", "commonName": "Limestone / Calcite / Chalk",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "100.086 g/mol",
            "geometry": "Trigonal planar carbonate CO₃²⁻ with Ca²⁺", "bondAngles": "O-C-O 120°",
            "bondTypes": "Ionic Ca²⁺ with resonant CO₃²⁻ anion", "numAtoms": 5, "numBonds": 4,
            "hybridization": "sp² at Carbon", "polarity": "Polar ionic",
            "physicalProps": "Fine white odorless powder; decomposes at 825°C to CaO and CO₂; poorly soluble in pure water (0.013 g/L).",
            "chemicalProps": "Reacts with acids releasing vigorous effervescence of CO₂ gas: CaCO₃ + 2HCl → CaCl₂ + H₂O + CO₂.",
            "uses": "Building stone and cement, dietary calcium supplement, antacid tablets (Tums), paper filler and white pigment.",
            "facts": "Over 4% of Earth's crust is composed of calcium carbonate, primarily formed from the accumulated shells of marine organisms over millions of years.",
            "atoms": [{"el":"Ca","x":0.0,"y":-1.8,"z":0.0},{"el":"C","x":0.0,"y":0.6,"z":0.0},{"el":"O","x":0.0,"y":1.8,"z":0.0},{"el":"O","x":1.1,"y":0.0,"z":0.0},{"el":"O","x":-1.1,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1],[1,2,2],[1,3,1],[1,4,1]]
        },
        {
            "id": "nahco3", "name": "Sodium Bicarbonate", "formula": "NaHCO₃", "commonName": "Baking Soda",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "84.007 g/mol",
            "geometry": "Planar HCO₃⁻ with Na⁺", "bondAngles": "O=C-O 120°",
            "bondTypes": "Ionic Na⁺···HCO₃⁻, covalent C-O and O-H bonds", "numAtoms": 6, "numBonds": 5,
            "hybridization": "sp² at Carbon", "polarity": "Polar ionic",
            "physicalProps": "White crystalline powder; decomposes above 50°C to Na₂CO₃, H₂O, and CO₂; mild alkaline taste.",
            "chemicalProps": "Amphoteric salt; reacts with culinary acids (vinegar, buttermilk) releasing CO₂ bubbles for leavening.",
            "uses": "Culinary baking leavener, dry chemical fire extinguishers, mild antacid, refrigerator deodorizer.",
            "facts": "Baking soda releases carbon dioxide gas when heated or acidified, creating tiny bubbles that cause dough and cakes to rise.",
            "atoms": [{"el":"Na","x":-1.8,"y":-0.5,"z":0.0},{"el":"C","x":0.5,"y":0.0,"z":0.0},{"el":"O","x":0.5,"y":1.25,"z":0.0},{"el":"O","x":-0.6,"y":-0.7,"z":0.0},{"el":"O","x":1.6,"y":-0.7,"z":0.0},{"el":"H","x":2.4,"y":-0.2,"z":0.0}],
            "bonds": [[0,3,1],[1,2,2],[1,3,1],[1,4,1],[4,5,1]]
        },
        {
            "id": "cao", "name": "Calcium Oxide", "formula": "CaO", "commonName": "Quicklime / Burnt Lime",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "56.077 g/mol",
            "geometry": "Cubic Rocksalt Structure", "bondAngles": "90° & 180°",
            "bondTypes": "Ionic bond Ca²⁺···O²⁻ (lattice energy 3414 kJ/mol)", "numAtoms": 2, "numBonds": 1,
            "hybridization": "Ionic lattice", "polarity": "Extremely polar (ionic)",
            "physicalProps": "White, caustic, alkaline crystalline solid; mp 2613°C, bp 2850°C; emits brilliant white light when heated (limelight).",
            "chemicalProps": "Violently reacts with water (slaking) generating intense heat: CaO + H₂O → Ca(OH)₂ (ΔH = -63.7 kJ/mol).",
            "uses": "Steelmaking flux, cement manufacture, self-heating meal cans, paper pulp kraft recovery.",
            "facts": "Heating quicklime to 2,570°C in an oxy-hydrogen flame produces an incandescent glow—the origin of the theatrical term 'in the limelight'.",
            "atoms": [{"el":"Ca","x":-1.2,"y":0.0,"z":0.0},{"el":"O","x":1.2,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1]]
        },
        {
            "id": "mgo", "name": "Magnesium Oxide", "formula": "MgO", "commonName": "Magnesia",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "40.304 g/mol",
            "geometry": "Cubic Halite Lattice", "bondAngles": "90° & 180°",
            "bondTypes": "Ionic bond Mg²⁺···O²⁻ (lattice energy 3791 kJ/mol)", "numAtoms": 2, "numBonds": 1,
            "hybridization": "Ionic lattice", "polarity": "Polar ionic",
            "physicalProps": "White hygroscopic solid; extremely high melting point (2852°C); electrical insulator with high thermal conductivity.",
            "chemicalProps": "Basic oxide; reacts slowly with water to form Mg(OH)₂; dissolves readily in acids.",
            "uses": "Refractory brick lining for steel blast furnaces, electrical cable insulation, gymnastic chalk, antacid.",
            "facts": "Because MgO combines exceptional electrical insulation with high thermal conductivity, it is packed inside electric heating elements (like stove burners).",
            "atoms": [{"el":"Mg","x":-1.05,"y":0.0,"z":0.0},{"el":"O","x":1.05,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1]]
        },
        {
            "id": "h2o2", "name": "Hydrogen Peroxide", "formula": "H₂O₂", "commonName": "Perhydrol / Dioxidane",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "34.014 g/mol",
            "geometry": "Non-planar Open-Book conformation", "bondAngles": "H-O-O 94.8°, dihedral angle 111.5°",
            "bondTypes": "O-O single peroxide bond + 2 O-H σ bonds", "numAtoms": 4, "numBonds": 3,
            "hybridization": "sp³ at Oxygen", "polarity": "Polar (μ = 2.26 D)",
            "physicalProps": "Colorless liquid, slightly more viscous than water; mp -0.43°C, bp 150.2°C; density 1.45 g/cm³.",
            "chemicalProps": "Disproportionates spontaneously: 2H₂O₂ → 2H₂O + O₂ (catalyzed by MnO₂ or catalase); strong oxidizer.",
            "uses": "Paper pulp wood bleaching, household antiseptic (3%), rocket monopropellant (90% high-test peroxide).",
            "facts": "Bombardier beetles spray boiling hydrogen peroxide and hydroquinone from abdomen glands as a chemical defense mechanism.",
            "atoms": [{"el":"O","x":-0.74,"y":0.0,"z":0.0},{"el":"O","x":0.74,"y":0.0,"z":0.0},{"el":"H","x":-1.0,"y":0.93,"z":0.0},{"el":"H","x":1.0,"y":-0.46,"z":0.8}],
            "bonds": [[0,1,1],[0,2,1],[1,3,1]]
        },
        {
            "id": "na2co3", "name": "Sodium Carbonate", "formula": "Na₂CO₃", "commonName": "Soda Ash / Washing Soda",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "105.988 g/mol",
            "geometry": "Planar CO₃²⁻ surrounded by Na⁺ ions", "bondAngles": "120°",
            "bondTypes": "Ionic 2Na⁺···CO₃²⁻, covalent C-O bonds", "numAtoms": 6, "numBonds": 5,
            "hybridization": "sp² at Carbon", "polarity": "Polar ionic",
            "physicalProps": "White odorless powder; mp 851°C; density 2.54 g/cm³; forms decahydrate (washing soda).",
            "chemicalProps": "Moderately strong alkaline salt in solution (pH ~ 11.5); softens hard water by precipitating Ca²⁺ as CaCO₃.",
            "uses": "Glass manufacturing (lowers silica melting temperature), laundry water softening, chemical pH regulator.",
            "facts": "Over 50% of worldwide sodium carbonate production is consumed directly by the glass-making industry to melt sand at lower energy costs.",
            "atoms": [{"el":"C","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.3,"z":0.0},{"el":"O","x":1.1,"y":-0.65,"z":0.0},{"el":"O","x":-1.1,"y":-0.65,"z":0.0},{"el":"Na","x":2.2,"y":0.5,"z":0.0},{"el":"Na","x":-2.2,"y":0.5,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1],[0,3,1],[2,4,1],[3,5,1]]
        },
        {
            "id": "kmno4", "name": "Potassium Permanganate", "formula": "KMnO₄", "commonName": "Condy's Crystals",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "158.034 g/mol",
            "geometry": "Tetrahedral around Manganese", "bondAngles": "109.5°",
            "bondTypes": "Ionic K⁺ with tetrahedral MnO₄⁻", "numAtoms": 6, "numBonds": 5,
            "hybridization": "d³s or sp³ at Mn", "polarity": "Polar ionic",
            "physicalProps": "Deep purple-bronze needle crystals; decomposes at 240°C; intense magenta/purple solution.",
            "chemicalProps": "Powerful oxidizing agent (Mn(VII) reduces to colorless Mn(II) in acid, or brown MnO₂ in neutral); self-indicating titrant.",
            "uses": "Redox titration titrant, municipal water treatment (iron/manganese removal), wound antiseptic disinfectant.",
            "facts": "The intense purple color of KMnO₄ is caused by ligand-to-metal charge transfer (LMCT) from oxygen p-orbitals to empty manganese 3d-orbitals.",
            "atoms": [{"el":"Mn","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.65,"z":0.0},{"el":"O","x":1.55,"y":-0.55,"z":0.0},{"el":"O","x":-0.78,"y":-0.55,"z":1.35},{"el":"O","x":-0.78,"y":-0.55,"z":-1.35},{"el":"K","x":0.0,"y":3.2,"z":0.0}],
            "bonds": [[0,1,2],[0,2,2],[0,3,1],[0,4,1],[1,5,1]]
        }
    ]

# Category D: Important Inorganic Compounds (Part 2)
def get_inorganic_part2():
    return [
        {
            "id": "cuso4", "name": "Copper(II) Sulfate", "formula": "CuSO₄", "commonName": "Blue Vitriol (hydrate)",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "159.609 g/mol",
            "geometry": "Distorted Octahedral in pentahydrate", "bondAngles": "109.5° in SO₄²⁻",
            "bondTypes": "Ionic Cu²⁺···SO₄²⁻ with dative coordination to water", "numAtoms": 6, "numBonds": 5,
            "hybridization": "sp³ at Sulfur, d²sp³ at Copper", "polarity": "Polar ionic",
            "physicalProps": "Anhydrous form is white/pale green powder; pentahydrate is vivid bright blue crystals; mp 110°C (loses H₂O).",
            "chemicalProps": "Reacts with iron nails in single displacement: Fe + CuSO₄ → FeSO₄ + Cu (reddish copper coats nail).",
            "uses": "Agricultural fungicide (Bordeaux mixture), copper electroplating bath, Fehling's test reagent for reducing sugars.",
            "facts": "Anhydrous CuSO₄ turns from chalky white to intense electric blue upon contact with trace moisture, making it a reliable water sensor.",
            "atoms": [{"el":"S","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.48,"z":0.0},{"el":"O","x":0.0,"y":-1.48,"z":0.0},{"el":"O","x":1.4,"y":0.0,"z":0.5},{"el":"O","x":-1.4,"y":0.0,"z":-0.5},{"el":"Cu","x":0.0,"y":2.9,"z":0.0}],
            "bonds": [[0,1,2],[0,2,2],[0,3,1],[0,4,1],[1,5,1]]
        },
        {
            "id": "nh4cl", "name": "Ammonium Chloride", "formula": "NH₄Cl", "commonName": "Sal Ammoniac",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "53.491 g/mol",
            "geometry": "Tetrahedral NH₄⁺ + Cl⁻ (CsCl type crystal)", "bondAngles": "109.5° in NH₄⁺",
            "bondTypes": "Ionic bond NH₄⁺···Cl⁻ + coordinate covalent N-H bonds", "numAtoms": 6, "numBonds": 5,
            "hybridization": "sp³ at Nitrogen", "polarity": "Polar ionic",
            "physicalProps": "White crystalline solid; sublimes upon heating at 338°C; highly endothermic dissolution (chills water).",
            "chemicalProps": "Thermally dissociates into gases: NH₄Cl(s) ⇌ NH₃(g) + HCl(g); acidic salt in aqueous solution (pH ~ 5).",
            "uses": "Soldering flux (cleans metal oxides), dry Leclanché batteries, salty liquorice flavoring (salmiak).",
            "facts": "In Nordic countries, ammonium chloride is used as the key flavoring agent in salmiak salty licorice candy.",
            "atoms": [{"el":"N","x":-0.7,"y":0.0,"z":0.0},{"el":"H","x":-0.7,"y":1.02,"z":0.0},{"el":"H","x":-0.7,"y":-0.51,"z":0.88},{"el":"H","x":-0.7,"y":-0.51,"z":-0.88},{"el":"H","x":0.3,"y":0.0,"z":0.0},{"el":"Cl","x":1.8,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1],[0,4,1],[4,5,1]]
        },
        {
            "id": "kcl", "name": "Potassium Chloride", "formula": "KCl", "commonName": "Sylvite / Muriate of Potash",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "74.551 g/mol",
            "geometry": "Face-Centered Cubic (FCC) Rock Salt", "bondAngles": "90° & 180°",
            "bondTypes": "Ionic K⁺···Cl⁻ (lattice energy 715 kJ/mol)", "numAtoms": 2, "numBonds": 1,
            "hybridization": "Ionic lattice", "polarity": "Polar ionic",
            "physicalProps": "White crystalline vitreous solid; mp 770°C, bp 1420°C; density 1.984 g/cm³; saline taste.",
            "chemicalProps": "Neutral salt; dissolves completely in water; reacts with silver nitrate to precipitate white AgCl.",
            "uses": "Potash agricultural fertilizer (source of K), low-sodium salt substitutes, medical treatment of hypokalemia.",
            "facts": "Potassium ions are the primary intracellular cation in all human cells, vital for generating cardiac and nerve electrical action potentials.",
            "atoms": [{"el":"K","x":-1.35,"y":0.0,"z":0.0},{"el":"Cl","x":1.35,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1]]
        },
        {
            "id": "fe2o3", "name": "Iron(III) Oxide", "formula": "Fe₂O₃", "commonName": "Hematite / Rust / Jeweler's Rouge",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "159.69 g/mol",
            "geometry": "Corundum-type hexagonal crystal structure", "bondAngles": "Octahedral coordination around Fe",
            "bondTypes": "Ionic bond with significant covalent character", "numAtoms": 5, "numBonds": 6,
            "hybridization": "d²sp³ at Fe", "polarity": "Polar ionic",
            "physicalProps": "Red-brown fine powder; mp 1565°C; ferromagnetic/antiferromagnetic behavior; insoluble in water.",
            "chemicalProps": "Reduced in blast furnace by CO to metallic iron: Fe₂O₃ + 3CO → 2Fe + 3CO₂; reacts with Al in thermite reaction.",
            "uses": "Primary iron ore for steel production, magnetic storage media (gamma-Fe₂O₃), glass polishing, red pigment.",
            "facts": "Mars is known as the 'Red Planet' because its surface dust is rich in iron(III) oxide (rust).",
            "atoms": [{"el":"Fe","x":-1.3,"y":0.0,"z":0.0},{"el":"Fe","x":1.3,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.3,"z":0.0},{"el":"O","x":0.0,"y":-1.3,"z":0.0},{"el":"O","x":0.0,"y":0.0,"z":1.4}],
            "bonds": [[0,2,1],[1,2,1],[0,3,1],[1,3,1],[0,4,1],[1,4,1]]
        },
        {
            "id": "zno", "name": "Zinc Oxide", "formula": "ZnO", "commonName": "Zinc White / Philosopher's Wool",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "81.38 g/mol",
            "geometry": "Hexagonal Wurtzite structure", "bondAngles": "109.5° tetrahedral coordination",
            "bondTypes": "Polar covalent / ionic Zn-O bonds", "numAtoms": 2, "numBonds": 1,
            "hybridization": "sp³ at Zn and O", "polarity": "Polar crystal",
            "physicalProps": "White powder at room temperature, turns yellow when hot (thermochromism); mp 1975°C; wide bandgap semiconductor (3.37 eV).",
            "chemicalProps": "Amphoteric oxide; dissolves in both acids (yielding Zn²⁺) and bases (yielding zincate [Zn(OH)₄]²⁻).",
            "uses": "Broad-spectrum physical mineral sunscreen (blocks UVA/UVB), rubber vulcanization activator, calamine lotion.",
            "facts": "Zinc oxide is thermochromic: it turns yellow when heated above 300°C due to loss of trace oxygen, and reverts to pure white upon cooling.",
            "atoms": [{"el":"Zn","x":-0.95,"y":0.0,"z":0.0},{"el":"O","x":0.95,"y":0.0,"z":0.0}],
            "bonds": [[0,1,1]]
        },
        {
            "id": "al2o3", "name": "Aluminum Oxide", "formula": "Al₂O₃", "commonName": "Alumina / Corundum / Sapphire / Ruby",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "101.96 g/mol",
            "geometry": "Trigonal Corundum lattice", "bondAngles": "Octahedral coordination around Al",
            "bondTypes": "Strong ionic/covalent network (Mohs hardness 9)", "numAtoms": 5, "numBonds": 6,
            "hybridization": "Ionic network", "polarity": "Polar ionic",
            "physicalProps": "White hard solid or gemstone; mp 2072°C, bp 2977°C; Mohs hardness 9 (second only to diamond/carborundum).",
            "chemicalProps": "Amphoteric oxide; dissolves in acids and hot concentrated NaOH; highly resistant to chemical corrosion.",
            "uses": "Industrial abrasive sandpaper, smelting feed for aluminum metal (Hall-Héroult process), scratch-resistant sapphire watch crystals.",
            "facts": "Rubies and sapphires are simply single crystals of aluminum oxide (corundum) tinted red by chromium or blue by titanium and iron impurities.",
            "atoms": [{"el":"Al","x":-1.3,"y":0.0,"z":0.0},{"el":"Al","x":1.3,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.3,"z":0.0},{"el":"O","x":0.0,"y":-1.3,"z":0.0},{"el":"O","x":0.0,"y":0.0,"z":1.4}],
            "bonds": [[0,2,1],[1,2,1],[0,3,1],[1,3,1],[0,4,1],[1,4,1]]
        },
        {
            "id": "agno3", "name": "Silver Nitrate", "formula": "AgNO₃", "commonName": "Lunar Caustic",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "169.87 g/mol",
            "geometry": "Planar NO₃⁻ anion with Ag⁺", "bondAngles": "120° in NO₃⁻",
            "bondTypes": "Ionic Ag⁺···NO₃⁻ + resonant N-O covalent bonds", "numAtoms": 5, "numBonds": 4,
            "hybridization": "sp² at Nitrogen", "polarity": "Polar ionic",
            "physicalProps": "Colorless transparent tabular crystals; mp 212°C; blackens on contact with skin/light as metallic silver precipitates.",
            "chemicalProps": "Precipitates halide ions quantitatively: Ag⁺ + Cl⁻ → AgCl(s) (curdy white precipitate); Tollens reagent component.",
            "uses": "Halide quantitative titration, mirror silvering, antiseptic cautery for nosebleeds and warts.",
            "facts": "Alchemists called silver nitrate 'lunar caustic' because they associated silver with Luna (the Moon) and it causticly blackens skin.",
            "atoms": [{"el":"Ag","x":-1.7,"y":0.0,"z":0.0},{"el":"N","x":0.9,"y":0.0,"z":0.0},{"el":"O","x":0.9,"y":1.25,"z":0.0},{"el":"O","x":-0.2,"y":-0.65,"z":0.0},{"el":"O","x":2.0,"y":-0.65,"z":0.0}],
            "bonds": [[0,3,1],[1,2,2],[1,3,1],[1,4,1]]
        },
        {
            "id": "caso4", "name": "Calcium Sulfate", "formula": "CaSO₄", "commonName": "Gypsum / Plaster of Paris",
            "category": "Inorganic Compounds", "categoryKey": "inorganic", "mw": "136.14 g/mol",
            "geometry": "Tetrahedral SO₄²⁻ with Ca²⁺", "bondAngles": "109.5° in SO₄²⁻",
            "bondTypes": "Ionic Ca²⁺···SO₄²⁻", "numAtoms": 6, "numBonds": 5,
            "hybridization": "sp³ at Sulfur", "polarity": "Polar ionic",
            "physicalProps": "White fine crystalline powder; mp 1460°C; forms hemihydrate (plaster of Paris) and dihydrate (gypsum).",
            "chemicalProps": "Plaster of Paris rehydrates exothermically into rigid interlocking gypsum crystals: CaSO₄·0.5H₂O + 1.5H₂O → CaSO₄·2H₂O.",
            "uses": "Drywall plasterboard in building construction, orthopaedic bone fracture casts, tofu coagulant.",
            "facts": "When gypsum is heated to 150°C, it loses 75% of its water to form Plaster of Paris, named after Montmartre gypsum deposits in Paris.",
            "atoms": [{"el":"S","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.48,"z":0.0},{"el":"O","x":0.0,"y":-1.48,"z":0.0},{"el":"O","x":1.4,"y":0.0,"z":0.5},{"el":"O","x":-1.4,"y":0.0,"z":-0.5},{"el":"Ca","x":0.0,"y":2.9,"z":0.0}],
            "bonds": [[0,1,2],[0,2,2],[0,3,1],[0,4,1],[1,5,1]]
        }
    ]

def get_inorganic_molecules():
    return get_inorganic_part1() + get_inorganic_part2()
