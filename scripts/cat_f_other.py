# Category F: Other Important Molecules (Part 1)
def get_other_part1():
    return [
        {
            "id": "so2", "name": "Sulfur Dioxide", "formula": "SO₂", "commonName": "Sulfurous Anhydride",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "64.066 g/mol",
            "geometry": "Bent (~119°)", "bondAngles": "119.5°", "bondTypes": "Resonant polar covalent bonds (bond order ~1.5)",
            "numAtoms": 3, "numBonds": 2, "hybridization": "sp² at Sulfur", "polarity": "Polar (μ = 1.63 D)",
            "physicalProps": "Colorless toxic gas with pungent choking match-head smell; bp -10°C; density 2.63 g/L.",
            "chemicalProps": "Acidic oxide; dissolves in water to form sulfurous acid H₂SO₃; oxidized to SO₃ in contact process.",
            "uses": "Sulfuric acid production (contact process), wine preservative and antioxidant (E220), bleaching agent.",
            "facts": "Volcanic eruptions release millions of tons of sulfur dioxide into the upper atmosphere, forming aerosol veils that temporarily cool global climate.",
            "atoms": [{"el":"S","x":0.0,"y":0.35,"z":0.0},{"el":"O","x":-1.25,"y":-0.35,"z":0.0},{"el":"O","x":1.25,"y":-0.35,"z":0.0}],
            "bonds": [[0,1,2],[0,2,2]]
        },
        {
            "id": "so3", "name": "Sulfur Trioxide", "formula": "SO₃", "commonName": "Sulfuric Oxide",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "80.06 g/mol",
            "geometry": "Trigonal Planar (D3h)", "bondAngles": "120.0°", "bondTypes": "3 resonant S=O bonds (order 1.33)",
            "numAtoms": 4, "numBonds": 3, "hybridization": "sp² at Sulfur", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless liquid or silky white crystalline solid (gamma form); mp 16.9°C, bp 45°C; fumes heavily in air.",
            "chemicalProps": "Extremely powerful Lewis acid and dehydrating agent; reacts violently with water forming H₂SO₄ fog.",
            "uses": "Essential intermediate in the contact process for sulfuric acid manufacture, sulfonation of detergents.",
            "facts": "Dissolving sulfur trioxide in concentrated sulfuric acid forms fuming sulfuric acid, chemically known as oleum (H₂S₂O₇).",
            "atoms": [{"el":"S","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.42,"z":0.0},{"el":"O","x":1.23,"y":-0.71,"z":0.0},{"el":"O","x":-1.23,"y":-0.71,"z":0.0}],
            "bonds": [[0,1,2],[0,2,2],[0,3,2]]
        },
        {
            "id": "n2o", "name": "Nitrous Oxide", "formula": "N₂O", "commonName": "Laughing Gas / Dinitrogen Monoxide",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "44.013 g/mol",
            "geometry": "Linear (N-N-O)", "bondAngles": "180°", "bondTypes": "Resonant N≡N⁺-O⁻ and N⁻=N⁺=O bonds",
            "numAtoms": 3, "numBonds": 2, "hybridization": "sp at central Nitrogen", "polarity": "Slightly polar (μ = 0.166 D)",
            "physicalProps": "Colorless sweet-smelling non-flammable gas; mp -90.86°C, bp -88.48°C; density 1.977 g/L.",
            "chemicalProps": "Thermal decomposition at >575°C yields nitrogen and oxygen: 2N₂O → 2N₂ + O₂ (acts as oxidizer in engines).",
            "uses": "Dental surgical anesthesia and analgesia, whipped cream aerosol propellant, automotive nitrous oxide engine boost.",
            "facts": "Humphry Davy tested nitrous oxide on himself in 1799, noting that it produced euphoric sensations and fits of laughter.",
            "atoms": [{"el":"N","x":-1.13,"y":0.0,"z":0.0},{"el":"N","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":1.19,"y":0.0,"z":0.0}],
            "bonds": [[0,1,3],[1,2,1]]
        },
        {
            "id": "no2", "name": "Nitrogen Dioxide", "formula": "NO₂", "commonName": "Nitrogen Peroxide",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "46.005 g/mol",
            "geometry": "Bent (~134°)", "bondAngles": "134.3°", "bondTypes": "Resonant covalent bonds with single unpaired electron",
            "numAtoms": 3, "numBonds": 2, "hybridization": "sp² at Nitrogen", "polarity": "Polar (μ = 0.316 D)",
            "physicalProps": "Reddish-brown toxic gas with acrid bleach-like odor; mp -11.2°C, bp 21.15°C; paramagnetic.",
            "chemicalProps": "Exists in dynamic thermal equilibrium with colorless dinitrogen tetroxide: 2NO₂ (brown) ⇌ N₂O₄ (colorless).",
            "uses": "Intermediate in the Ostwald process for nitric acid, oxidizer for rocket hypergolic fuels.",
            "facts": "Nitrogen dioxide is responsible for the yellowish-brown haze visible over cities with heavy vehicular air pollution.",
            "atoms": [{"el":"N","x":0.0,"y":0.3,"z":0.0},{"el":"O","x":-1.1,"y":-0.2,"z":0.0},{"el":"O","x":1.1,"y":-0.2,"z":0.0}],
            "bonds": [[0,1,2],[0,2,1]]
        },
        {
            "id": "h2s", "name": "Hydrogen Sulfide", "formula": "H₂S", "commonName": "Hydrosulfuric Acid / Rotten Egg Gas",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "34.08 g/mol",
            "geometry": "Bent (~92.1°)", "bondAngles": "92.1°", "bondTypes": "Polar covalent H-S σ bonds",
            "numAtoms": 3, "numBonds": 2, "hybridization": "Almost unhybridized 3p on Sulfur", "polarity": "Polar (μ = 0.97 D)",
            "physicalProps": "Colorless, highly toxic, flammable gas with foul rotten-egg stench; mp -82°C, bp -60°C; density 1.36 g/L.",
            "chemicalProps": "Weak diprotic acid (pKa1 = 7.0, pKa2 = 19); burns in air to form SO₂; precipitates insoluble black metal sulfides.",
            "uses": "Qualitative inorganic salt analysis reagent, precursor to organosulfur compounds and elemental sulfur (Claus process).",
            "facts": "Although human noses detect H₂S at parts-per-billion levels, concentrations above 100 ppm quickly paralyze the olfactory nerve, leaving victims unaware of fatal exposure.",
            "atoms": [{"el":"S","x":0.0,"y":0.0,"z":0.0},{"el":"H","x":-0.97,"y":0.97,"z":0.0},{"el":"H","x":0.97,"y":0.97,"z":0.0}],
            "bonds": [[0,1,1],[0,2,1]]
        },
        {
            "id": "sio2", "name": "Silicon Dioxide", "formula": "SiO₂", "commonName": "Silica / Quartz / Sand",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "60.084 g/mol",
            "geometry": "Giant 3D tetrahedral network of SiO₄ units", "bondAngles": "Si-O-Si 144°, O-Si-O 109.5°",
            "bondTypes": "Polar covalent network σ bonds (Mohs hardness 7)", "numAtoms": 3, "numBonds": 2,
            "hybridization": "sp³ at Silicon", "polarity": "Non-polar macroscopic crystal",
            "physicalProps": "Transparent to white crystalline solid (quartz) or amorphous powder; mp 1713°C, bp 2950°C; insoluble in water.",
            "chemicalProps": "Acidic oxide; attacked specifically by hydrofluoric acid: SiO₂ + 4HF → SiF₄ + 2H₂O; melts with Na₂CO₃ into silicate glass.",
            "uses": "Primary component of standard window glass, concrete aggregate, microchip semiconductor insulator, silica gel desiccant.",
            "facts": "Quartz is piezoelectric: applying mechanical stress generates an electric voltage, forming the timing heartbeat of all modern quartz wristwatches.",
            "atoms": [{"el":"Si","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":-1.6,"y":0.0,"z":0.0},{"el":"O","x":1.6,"y":0.0,"z":0.0}],
            "bonds": [[0,1,2],[0,2,2]]
        },
        {
            "id": "bh3", "name": "Borane", "formula": "BH₃", "commonName": "Trihydridoboron",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "13.83 g/mol",
            "geometry": "Trigonal Planar (D3h)", "bondAngles": "120.0°", "bondTypes": "3 electron-deficient B-H σ bonds (6 valence electrons)",
            "numAtoms": 4, "numBonds": 3, "hybridization": "sp² with empty 2pz orbital", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless transient gas; spontaneously dimerizes to diborane B₂H₆ containing 3-center-2-electron bonds.",
            "chemicalProps": "Potent Lewis acid; stabilized as Lewis base adducts (BH₃·THF, BH₃·SMe₂); key reagent in anti-Markovnikov hydroboration-oxidation of alkenes.",
            "uses": "Hydroboration-oxidation synthesis of primary alcohols, selective reduction of carboxylic acids.",
            "facts": "Herbert C. Brown won the 1979 Nobel Prize in Chemistry for developing organoborane reactions using borane.",
            "atoms": [{"el":"B","x":0.0,"y":0.0,"z":0.0},{"el":"H","x":0.0,"y":1.19,"z":0.0},{"el":"H","x":1.03,"y":-0.60,"z":0.0},{"el":"H","x":-1.03,"y":-0.60,"z":0.0}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1]]
        },
        {
            "id": "h3bo3", "name": "Boric Acid", "formula": "H₃BO₃", "commonName": "Orthoboric Acid / Boracic Acid",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "61.83 g/mol",
            "geometry": "Trigonal Planar around Boron (C3h)", "bondAngles": "120.0°", "bondTypes": "3 B-O σ bonds + 3 O-H bonds",
            "numAtoms": 7, "numBonds": 6, "hybridization": "sp² at Boron", "polarity": "Non-polar planar symmetry",
            "physicalProps": "White crystalline scales or powder with greasy feel; mp 170.9°C (decomposes); soluble in boiling water.",
            "chemicalProps": "Monobasic Lewis acid in water (does not donate H⁺, but abstracts OH⁻: B(OH)₃ + 2H₂O ⇌ [B(OH)₄]⁻ + H₃O⁺, pKa = 9.24).",
            "uses": "Antiseptic eyewash, flame retardant in cellulose insulation, cockroach and ant pest control insecticide, neutron absorber.",
            "facts": "Boric acid was pumped into the damaged nuclear reactors at Chernobyl in 1986 because boron-10 avidly absorbs thermal neutrons to halt fission.",
            "atoms": [{"el":"B","x":0.0,"y":0.0,"z":0.0},{"el":"O","x":0.0,"y":1.36,"z":0.0},{"el":"O","x":1.18,"y":-0.68,"z":0.0},{"el":"O","x":-1.18,"y":-0.68,"z":0.0},{"el":"H","x":0.8,"y":1.8,"z":0.0},{"el":"H","x":1.1,"y":-1.6,"z":0.0},{"el":"H","x":-1.9,"y":-0.2,"z":0.0}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1],[1,4,1],[2,5,1],[3,6,1]]
        }
    ]

# Category F: Other Important Molecules (Part 2)
def get_other_part2():
    return [
        {
            "id": "benzaldehyde", "name": "Benzaldehyde", "formula": "C₇H₆O", "commonName": "Oil of Bitter Almond",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "106.12 g/mol",
            "geometry": "Planar aromatic ring with conjugated aldehyde", "bondAngles": "120° ring, C-C=O 123°",
            "bondTypes": "Aromatic π system, C=O double bond, C-H σ bonds", "numAtoms": 14, "numBonds": 14,
            "hybridization": "sp² at ring and carbonyl C", "polarity": "Polar (μ = 2.77 D)",
            "physicalProps": "Colorless to yellowish liquid with characteristic marzipan/almond aroma; mp -26°C, bp 178.1°C.",
            "chemicalProps": "Oxidizes in air to white benzoic acid crystals; undergoes benzoin condensation and Cannizzaro reaction.",
            "uses": "Artificial almond extract flavoring, precursor to malachite green and acridine dyes, fragrance ingredient.",
            "facts": "Benzaldehyde naturally occurs in bitter almonds, apricot kernels, and peach stones, where it is bound to toxic amygdalin.",
            "atoms": [{"el":"C","x":0.0,"y":1.4,"z":0.0},{"el":"C","x":1.2,"y":0.7,"z":0.0},{"el":"C","x":1.2,"y":-0.7,"z":0.0},{"el":"C","x":0.0,"y":-1.4,"z":0.0},{"el":"C","x":-1.2,"y":-0.7,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"C","x":0.0,"y":2.9,"z":0.0},{"el":"O","x":1.1,"y":3.5,"z":0.0},{"el":"H","x":-0.9,"y":3.5,"z":0.0},{"el":"H","x":2.1,"y":1.2,"z":0.0},{"el":"H","x":2.1,"y":-1.2,"z":0.0},{"el":"H","x":0.0,"y":-2.5,"z":0.0},{"el":"H","x":-2.1,"y":-1.2,"z":0.0},{"el":"H","x":-2.1,"y":1.2,"z":0.0}],
            "bonds": [[0,1,2],[1,2,1],[2,3,2],[3,4,1],[4,5,2],[5,0,1],[0,6,1],[6,7,2],[6,8,1],[1,9,1],[2,10,1],[3,11,1],[4,12,1],[5,13,1]]
        },
        {
            "id": "naphthalene", "name": "Naphthalene", "formula": "C₁₀H₈", "commonName": "Mothballs / White Tar",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "128.17 g/mol",
            "geometry": "Planar fused bicyclic aromatic ring (D2h)", "bondAngles": "120.0°",
            "bondTypes": "Delocalized 10-π electron aromatic system (Hückel 4n+2 with n=2)", "numAtoms": 18, "numBonds": 19,
            "hybridization": "sp² at all 10 carbons", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "White crystalline flakes; mp 80.26°C, bp 218°C; readily sublimes at room temperature; pungent tarry smell.",
            "chemicalProps": "Undergoes electrophilic aromatic substitution preferentially at the alpha (1) position rather than beta (2).",
            "uses": "Traditional mothballs insecticide, manufacture of phthalic anhydride for plasticizers, azo dyes.",
            "facts": "Naphthalene is the simplest polycyclic aromatic hydrocarbon (PAH) and the first PAH ever detected in interstellar dust clouds.",
            "atoms": [{"el":"C","x":-0.7,"y":1.4,"z":0.0},{"el":"C","x":0.7,"y":1.4,"z":0.0},{"el":"C","x":1.4,"y":0.0,"z":0.0},{"el":"C","x":0.7,"y":-1.4,"z":0.0},{"el":"C","x":-0.7,"y":-1.4,"z":0.0},{"el":"C","x":-1.4,"y":0.0,"z":0.0},{"el":"C","x":2.8,"y":0.0,"z":0.0},{"el":"C","x":3.5,"y":1.4,"z":0.0},{"el":"C","x":2.8,"y":2.4,"z":0.0},{"el":"C","x":1.4,"y":2.4,"z":0.0},{"el":"H","x":-1.2,"y":2.3,"z":0.0},{"el":"H","x":-2.5,"y":0.0,"z":0.0},{"el":"H","x":-1.2,"y":-2.3,"z":0.0},{"el":"H","x":1.2,"y":-2.3,"z":0.0},{"el":"H","x":3.3,"y":-0.9,"z":0.0},{"el":"H","x":4.6,"y":1.4,"z":0.0},{"el":"H","x":3.3,"y":3.4,"z":0.0},{"el":"H","x":0.9,"y":3.4,"z":0.0}],
            "bonds": [[0,1,1],[1,2,2],[2,3,1],[3,4,2],[4,5,1],[5,0,2],[2,6,1],[6,7,2],[7,8,1],[8,9,2],[9,1,1],[0,10,1],[5,11,1],[4,12,1],[3,13,1],[6,14,1],[7,15,1],[8,16,1],[9,17,1]]
        },
        {
            "id": "aspirin", "name": "Aspirin", "formula": "C₉H₈O₄", "commonName": "Acetylsalicylic Acid / ASA",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "180.157 g/mol",
            "geometry": "Planar benzene ring with ortho ester and carboxyl", "bondAngles": "120° ring",
            "bondTypes": "Aromatic π system, 2 C=O double bonds, C-O, O-H, C-H bonds", "numAtoms": 21, "numBonds": 21,
            "hybridization": "sp² ring and carbonyls, sp³ methyl", "polarity": "Polar (μ = 2.4 D)",
            "physicalProps": "Colorless to white crystalline powder with faint vinegar smell (hydrolysis); mp 136°C; poorly soluble in water.",
            "chemicalProps": "Irreversibly inhibits cyclooxygenase enzymes (COX-1 and COX-2) by transferring its acetyl group to a serine residue.",
            "uses": "Analgesic, antipyretic, anti-inflammatory, low-dose daily blood-thinner antiplatelet for stroke and heart attack prevention.",
            "facts": "Felix Hoffmann synthesized stable acetylsalicylic acid at Bayer in 1897 to relieve his father's debilitating arthritis pain.",
            "atoms": [{"el":"C","x":0.0,"y":1.4,"z":0.0},{"el":"C","x":1.2,"y":0.7,"z":0.0},{"el":"C","x":1.2,"y":-0.7,"z":0.0},{"el":"C","x":0.0,"y":-1.4,"z":0.0},{"el":"C","x":-1.2,"y":-0.7,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"C","x":0.0,"y":2.9,"z":0.0},{"el":"O","x":1.1,"y":3.6,"z":0.0},{"el":"O","x":-1.2,"y":3.5,"z":0.0},{"el":"H","x":-1.1,"y":4.5,"z":0.0},{"el":"O","x":2.4,"y":1.4,"z":0.0},{"el":"C","x":3.6,"y":0.8,"z":0.0},{"el":"O","x":3.8,"y":-0.4,"z":0.0},{"el":"C","x":4.7,"y":1.8,"z":0.0},{"el":"H","x":2.1,"y":-1.2,"z":0.0},{"el":"H","x":0.0,"y":-2.5,"z":0.0},{"el":"H","x":-2.1,"y":-1.2,"z":0.0},{"el":"H","x":-2.1,"y":1.2,"z":0.0}],
            "bonds": [[0,1,2],[1,2,1],[2,3,2],[3,4,1],[4,5,2],[5,0,1],[0,6,1],[6,7,2],[6,8,1],[8,9,1],[1,10,1],[10,11,1],[11,12,2],[11,13,1],[2,14,1],[3,15,1],[4,16,1],[5,17,1]]
        },
        {
            "id": "paracetamol", "name": "Paracetamol", "formula": "C₈H₉NO₂", "commonName": "Acetaminophen / Tylenol",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "151.163 g/mol",
            "geometry": "Planar benzene ring with para-substituted hydroxyl and acetamide", "bondAngles": "120° ring",
            "bondTypes": "Aromatic π system, phenolic O-H, amide C=O and N-H bonds", "numAtoms": 20, "numBonds": 20,
            "hybridization": "sp² ring, amide C and N; sp³ methyl", "polarity": "Polar (μ = 2.8 D)",
            "physicalProps": "White crystalline solid with slightly bitter taste; mp 169°C; moderately soluble in water (14 g/L).",
            "chemicalProps": "Inhibits prostaglandin synthesis in the brain by reducing the active peroxidase site of COX; oxidized by CYP2E1 to toxic NAPQI.",
            "uses": "Front-line fever reducer (antipyretic) and pain reliever (analgesic) for headaches, arthritis, and flu.",
            "facts": "Unlike ibuprofen and aspirin, paracetamol does not reduce peripheral tissue inflammation or cause stomach ulcers.",
            "atoms": [{"el":"C","x":0.0,"y":1.4,"z":0.0},{"el":"C","x":1.2,"y":0.7,"z":0.0},{"el":"C","x":1.2,"y":-0.7,"z":0.0},{"el":"C","x":0.0,"y":-1.4,"z":0.0},{"el":"C","x":-1.2,"y":-0.7,"z":0.0},{"el":"C","x":-1.2,"y":0.7,"z":0.0},{"el":"O","x":0.0,"y":2.7,"z":0.0},{"el":"H","x":0.8,"y":3.2,"z":0.0},{"el":"N","x":0.0,"y":-2.8,"z":0.0},{"el":"H","x":-0.8,"y":-3.3,"z":0.0},{"el":"C","x":1.1,"y":-3.6,"z":0.0},{"el":"O","x":2.2,"y":-3.1,"z":0.0},{"el":"C","x":0.9,"y":-5.1,"z":0.0},{"el":"H","x":2.1,"y":1.2,"z":0.0},{"el":"H","x":2.1,"y":-1.2,"z":0.0},{"el":"H","x":-2.1,"y":-1.2,"z":0.0},{"el":"H","x":-2.1,"y":1.2,"z":0.0}],
            "bonds": [[0,1,2],[1,2,1],[2,3,2],[3,4,1],[4,5,2],[5,0,1],[0,6,1],[6,7,1],[3,8,1],[8,9,1],[8,10,1],[10,11,2],[10,12,1],[1,13,1],[2,14,1],[4,15,1],[5,16,1]]
        },
        {
            "id": "ibuprofen", "name": "Ibuprofen", "formula": "C₁₃H₁₈O₂", "commonName": "Advil / Motrin",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "206.28 g/mol",
            "geometry": "Planar benzene ring with isobutyl and propionic acid branches", "bondAngles": "120° ring, 109.5° aliphatic",
            "bondTypes": "Aromatic π system, carboxyl C=O, C-O, O-H bonds, aliphatic C-C, C-H", "numAtoms": 33, "numBonds": 33,
            "hybridization": "sp² ring and carboxyl, sp³ side chains", "polarity": "Weakly polar (lipophilic)",
            "physicalProps": "White crystalline powder with slight odor; mp 75-78°C; practically insoluble in water, soluble in ethanol.",
            "chemicalProps": "Non-steroidal anti-inflammatory drug (NSAID); non-selectively reversibly inhibits COX-1 and COX-2 enzymes.",
            "uses": "Treatment of pain, menstrual cramps, inflammatory rheumatoid arthritis, sports muscular injuries.",
            "facts": "Ibuprofen is sold as a racemic mixture of (R) and (S) enantiomers, but the human body naturally converts the inactive (R)-isomer into the active (S)-isomer.",
            "atoms": [{"el":"C","x":-1.4,"y":0.0,"z":0.0},{"el":"C","x":-0.7,"y":1.2,"z":0.0},{"el":"C","x":0.7,"y":1.2,"z":0.0},{"el":"C","x":1.4,"y":0.0,"z":0.0},{"el":"C","x":0.7,"y":-1.2,"z":0.0},{"el":"C","x":-0.7,"y":-1.2,"z":0.0},{"el":"C","x":2.9,"y":0.0,"z":0.0},{"el":"C","x":3.6,"y":-1.3,"z":0.0},{"el":"C","x":3.4,"y":1.2,"z":0.0},{"el":"O","x":2.9,"y":2.3,"z":0.0},{"el":"O","x":4.7,"y":1.0,"z":0.0},{"el":"H","x":5.0,"y":1.9,"z":0.0},{"el":"C","x":-2.9,"y":0.0,"z":0.0},{"el":"C","x":-3.6,"y":-1.3,"z":0.0},{"el":"C","x":-3.3,"y":-2.5,"z":0.9},{"el":"C","x":-3.3,"y":-2.5,"z":-0.9}],
            "bonds": [[0,1,2],[1,2,1],[2,3,2],[3,4,1],[4,5,2],[5,0,1],[3,6,1],[6,7,1],[6,8,1],[8,9,2],[8,10,1],[10,11,1],[0,12,1],[12,13,1],[13,14,1],[13,15,1]]
        },
        {
            "id": "ccl4", "name": "Carbon Tetrachloride", "formula": "CCl₄", "commonName": "Tetrachloromethane / Halon-104",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "153.82 g/mol",
            "geometry": "Perfect Tetrahedral (Td)", "bondAngles": "109.47°",
            "bondTypes": "4 highly polar C-Cl σ bonds with mutual cancellation", "numAtoms": 5, "numBonds": 4,
            "hybridization": "sp³", "polarity": "Non-polar (dipoles cancel, μ = 0 D)",
            "physicalProps": "Dense, heavy, colorless liquid with sweet chloroform-like odor; mp -22.9°C, bp 76.7°C; density 1.587 g/cm³.",
            "chemicalProps": "Non-flammable; dissolves non-polar fats and oils; phased out under Montreal Protocol due to ozone depletion.",
            "uses": "Historical dry-cleaning solvent and fire extinguishing fluid, CFC refrigerant feedstock.",
            "facts": "Even though each C-Cl bond is extremely polar, carbon tetrachloride is completely non-polar because its 4 dipoles cancel out symmetrically in 3D.",
            "atoms": [{"el":"C","x":0.0,"y":0.0,"z":0.0},{"el":"Cl","x":1.02,"y":1.02,"z":1.02},{"el":"Cl","x":-1.02,"y":-1.02,"z":1.02},{"el":"Cl","x":-1.02,"y":1.02,"z":-1.02},{"el":"Cl","x":1.02,"y":-1.02,"z":-1.02}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1],[0,4,1]]
        },
        {
            "id": "sf6", "name": "Sulfur Hexafluoride", "formula": "SF₆", "commonName": "Elegance / High-Voltage Gas",
            "category": "Other Major Compounds", "categoryKey": "other", "mw": "146.06 g/mol",
            "geometry": "Regular Octahedral (Oh)", "bondAngles": "90.0° & 180.0°",
            "bondTypes": "6 polar covalent S-F bonds (hypervalent sulfur octet expansion)", "numAtoms": 7, "numBonds": 6,
            "hybridization": "sp³d² at Sulfur", "polarity": "Non-polar (μ = 0 D)",
            "physicalProps": "Colorless, odorless, non-toxic, non-flammable dense gas; sublimes at -63.8°C; density 6.13 g/L (5× heavier than air).",
            "chemicalProps": "Extremely inert due to tight steric shielding of the central sulfur atom by 6 fluorine atoms; high dielectric breakdown strength.",
            "uses": "Dielectric insulating gas in high-voltage circuit breakers and transformers, eye vitrectomy surgery tamponade.",
            "facts": "Because SF₆ is 5 times denser than air, sound waves travel much slower through it, making a person's voice sound deep and baritone when inhaled.",
            "atoms": [{"el":"S","x":0.0,"y":0.0,"z":0.0},{"el":"F","x":0.0,"y":1.56,"z":0.0},{"el":"F","x":0.0,"y":-1.56,"z":0.0},{"el":"F","x":1.56,"y":0.0,"z":0.0},{"el":"F","x":-1.56,"y":0.0,"z":0.0},{"el":"F","x":0.0,"y":0.0,"z":1.56},{"el":"F","x":0.0,"y":0.0,"z":-1.56}],
            "bonds": [[0,1,1],[0,2,1],[0,3,1],[0,4,1],[0,5,1],[0,6,1]]
        }
    ]

def get_other_molecules():
    return get_other_part1() + get_other_part2()
