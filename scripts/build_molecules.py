# -*- coding: utf-8 -*-
import json, math

def get_molecules():
    mols = []
    
    # ------------------ CATEGORY A: SIMPLE MOLECULES (12) ------------------
    mols.append({
        'id': 'water',
        'name': 'Water',
        'formula': 'H₂O',
        'commonName': 'Dihydrogen Monoxide',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '18.015 g/mol',
        'geometry': 'Bent',
        'bondAngles': '104.45°',
        'bondTypes': 'Polar covalent σ bonds',
        'numAtoms': 3,
        'numBonds': 2,
        'hybridization': 'sp³',
        'polarity': 'Polar (μ = 1.85 D)',
        'physicalProps': 'Colorless liquid at STP; mp 0°C, bp 100°C; density 1.00 g/cm³; high specific heat (4.184 J/g·K).',
        'chemicalProps': 'Amphoteric (acts as acid and base); autoionizes Kw = 1.0 × 10⁻¹⁴; forms extensive 3D hydrogen bonding network.',
        'uses': 'Universal solvent in biology and chemical syntheses, industrial coolant, baseline reference for temperature and density scales.',
        'facts': 'Ice floats on liquid water because its hydrogen-bonded hexagonal crystal lattice holds molecules farther apart than the chaotic liquid state.',
        'atoms': [
            {'el': 'O', 'x': 0.0, 'y': 0.0, 'z': 0.0},
            {'el': 'H', 'x': -0.757, 'y': 0.586, 'z': 0.0},
            {'el': 'H', 'x': 0.757, 'y': 0.586, 'z': 0.0}
        ],
        'bonds': [[0, 1, 1], [0, 2, 1]]
    })
    
    mols.append({
        'id': 'hydrogen',
        'name': 'Hydrogen Gas',
        'formula': 'H₂',
        'commonName': 'Molecular Hydrogen',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '2.016 g/mol',
        'geometry': 'Linear',
        'bondAngles': '180°',
        'bondTypes': 'Non-polar covalent σ bond',
        'numAtoms': 2,
        'numBonds': 1,
        'hybridization': '1s-1s overlap',
        'polarity': 'Non-polar (μ = 0 D)',
        'physicalProps': 'Colorless, odorless gas; mp -259.16°C, bp -252.87°C; density 0.089 g/L (lightest gas known).',
        'chemicalProps': 'Highly flammable; reacts with oxygen to form water: 2H₂ + O₂ → 2H₂O (ΔH° = -572 kJ); strong reducing agent.',
        'uses': 'Haber-Bosch ammonia synthesis, petroleum hydrotreating, zero-emission fuel cells, cryogenic liquid rocket propellant.',
        'facts': 'Hydrogen makes up roughly 75% of all normal baryonic matter in the universe and was forged in the first three minutes following the Big Bang.',
        'atoms': [
            {'el': 'H', 'x': -0.37, 'y': 0.0, 'z': 0.0},
            {'el': 'H', 'x': 0.37, 'y': 0.0, 'z': 0.0}
        ],
        'bonds': [[0, 1, 1]]
    })
    
    mols.append({
        'id': 'oxygen',
        'name': 'Oxygen Gas',
        'formula': 'O₂',
        'commonName': 'Dioxygen',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '31.998 g/mol',
        'geometry': 'Linear',
        'bondAngles': '180°',
        'bondTypes': 'Covalent double bond (1 σ + 1 π)',
        'numAtoms': 2,
        'numBonds': 1,
        'hybridization': 'sp²',
        'polarity': 'Non-polar (μ = 0 D)',
        'physicalProps': 'Colorless gas, pale blue cryogenic liquid; mp -218.79°C, bp -182.96°C; density 1.429 g/L.',
        'chemicalProps': 'Paramagnetic ground state with 2 unpaired electrons in π* orbitals; strong oxidizer essential for aerobic respiration.',
        'uses': 'Cellular respiration, hospital oxygen masks, steel manufacturing, blast furnaces, and rocket oxidizers.',
        'facts': 'Liquid oxygen is visibly magnetic and will pool in the gap between the poles of a strong horseshoe neodymium magnet.',
        'atoms': [
            {'el': 'O', 'x': -0.605, 'y': 0.0, 'z': 0.0},
            {'el': 'O', 'x': 0.605, 'y': 0.0, 'z': 0.0}
        ],
        'bonds': [[0, 1, 2]]
    })

    mols.append({
        'id': 'nitrogen',
        'name': 'Nitrogen Gas',
        'formula': 'N₂',
        'commonName': 'Dinitrogen',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '28.014 g/mol',
        'geometry': 'Linear',
        'bondAngles': '180°',
        'bondTypes': 'Covalent triple bond (1 σ + 2 π)',
        'numAtoms': 2,
        'numBonds': 1,
        'hybridization': 'sp',
        'polarity': 'Non-polar (μ = 0 D)',
        'physicalProps': 'Colorless, odorless inert gas; mp -210.0°C, bp -195.79°C; density 1.251 g/L.',
        'chemicalProps': 'Chemically inert at ambient conditions due to immense bond dissociation energy (945 kJ/mol).',
        'uses': 'Inert atmosphere for food packaging, liquid nitrogen cryogenic preservation, ammonia synthesis.',
        'facts': 'Makes up 78.08% of the Earth atmosphere, shielding life by diluting reactive oxygen.',
        'atoms': [
            {'el': 'N', 'x': -0.55, 'y': 0.0, 'z': 0.0},
            {'el': 'N', 'x': 0.55, 'y': 0.0, 'z': 0.0}
        ],
        'bonds': [[0, 1, 3]]
    })

    mols.append({
        'id': 'carbondioxide',
        'name': 'Carbon Dioxide',
        'formula': 'CO₂',
        'commonName': 'Carbonic Acid Gas / Dry Ice',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '44.009 g/mol',
        'geometry': 'Linear',
        'bondAngles': '180°',
        'bondTypes': 'Two polar covalent double bonds (2 σ + 2 π)',
        'numAtoms': 3,
        'numBonds': 2,
        'hybridization': 'sp',
        'polarity': 'Non-polar (μ = 0 D)',
        'physicalProps': 'Colorless odorless gas; sublimes at -78.5°C; density 1.977 g/L.',
        'chemicalProps': 'Acidic anhydride; dissolves in water producing carbonic acid H₂CO₃; reacts with Ca(OH)₂ forming milky CaCO₃.',
        'uses': 'Plant photosynthesis, carbonated drinks, fire extinguishers, supercritical green extraction of pharmaceuticals.',
        'facts': 'Solid carbon dioxide (dry ice) sublimes straight from solid to gas at 1 atm without forming a liquid puddle.',
        'atoms': [
            {'el': 'C', 'x': 0.0, 'y': 0.0, 'z': 0.0},
            {'el': 'O', 'x': -1.16, 'y': 0.0, 'z': 0.0},
            {'el': 'O', 'x': 1.16, 'y': 0.0, 'z': 0.0}
        ],
        'bonds': [[0, 1, 2], [0, 2, 2]]
    })

    mols.append({
        'id': 'carbonmonoxide',
        'name': 'Carbon Monoxide',
        'formula': 'CO',
        'commonName': 'Carbon Oxide',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '28.010 g/mol',
        'geometry': 'Linear',
        'bondAngles': '180°',
        'bondTypes': 'Triple bond with coordinate covalent bond',
        'numAtoms': 2,
        'numBonds': 1,
        'hybridization': 'sp',
        'polarity': 'Slightly polar (μ = 0.122 D)',
        'physicalProps': 'Colorless, odorless, highly toxic gas; mp -205.0°C, bp -191.5°C.',
        'chemicalProps': 'Strong field ligand forming metal carbonyls; binds hemoglobin with 200x affinity of O₂.',
        'uses': 'Syngas fuel, iron blast furnace metallurgy, industrial synthesis of methanol and acetic acid.',
        'facts': 'Carbon monoxide is often known as the silent killer because humans have no sensory receptors to detect it in air.',
        'atoms': [
            {'el': 'C', 'x': -0.564, 'y': 0.0, 'z': 0.0},
            {'el': 'O', 'x': 0.564, 'y': 0.0, 'z': 0.0}
        ],
        'bonds': [[0, 1, 3]]
    })

    mols.append({
        'id': 'ozone',
        'name': 'Ozone',
        'formula': 'O₃',
        'commonName': 'Trioxygen',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '47.997 g/mol',
        'geometry': 'Bent',
        'bondAngles': '116.8°',
        'bondTypes': 'Resonant covalent bonds (bond order 1.5)',
        'numAtoms': 3,
        'numBonds': 2,
        'hybridization': 'sp²',
        'polarity': 'Polar (μ = 0.53 D)',
        'physicalProps': 'Pale blue gas with a sharp electrical odor; mp -192.2°C, bp -111.9°C.',
        'chemicalProps': 'Powerful oxidant (E° = +2.07 V); cleaves alkenes in ozonolysis; decomposes to O₂.',
        'uses': 'Stratospheric UV protection, water sterilization, disinfection of medical equipment.',
        'facts': 'The stratospheric ozone layer filters over 97% of the dangerous solar ultraviolet radiation before it hits Earth surface.',
        'atoms': [
            {'el': 'O', 'x': 0.0, 'y': 0.387, 'z': 0.0},
            {'el': 'O', 'x': -1.088, 'y': -0.194, 'z': 0.0},
            {'el': 'O', 'x': 1.088, 'y': -0.194, 'z': 0.0}
        ],
        'bonds': [[0, 1, 1], [0, 2, 2]]
    })

    mols.append({
        'id': 'ammonia',
        'name': 'Ammonia',
        'formula': 'NH₃',
        'commonName': 'Azane / Spirit of Hartshorn',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '17.031 g/mol',
        'geometry': 'Trigonal Pyramidal',
        'bondAngles': '107.8°',
        'bondTypes': 'Polar covalent σ bonds',
        'numAtoms': 4,
        'numBonds': 3,
        'hybridization': 'sp³',
        'polarity': 'Polar (μ = 1.47 D)',
        'physicalProps': 'Colorless pungent gas; mp -77.73°C, bp -33.34°C; highly water soluble.',
        'chemicalProps': 'Weak base (pKb = 4.75); forms ammonium salts with acids; undergoes quantum umbrella inversion.',
        'uses': 'Production of agricultural fertilizers (urea, ammonium nitrate), nitric acid synthesis, cleaners.',
        'facts': 'The quantum tunneling umbrella inversion of ammonia was used in 1949 to build the worlds very first atomic clock.',
        'atoms': [
            {'el': 'N', 'x': 0.0, 'y': 0.0, 'z': 0.116},
            {'el': 'H', 'x': 0.0, 'y': 0.940, 'z': -0.271},
            {'el': 'H', 'x': -0.814, 'y': -0.470, 'z': -0.271},
            {'el': 'H', 'x': 0.814, 'y': -0.470, 'z': -0.271}
        ],
        'bonds': [[0, 1, 1], [0, 2, 1], [0, 3, 1]]
    })

    mols.append({
        'id': 'methane',
        'name': 'Methane',
        'formula': 'CH₄',
        'commonName': 'Natural Gas / Marsh Gas',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '16.043 g/mol',
        'geometry': 'Tetrahedral',
        'bondAngles': '109.47°',
        'bondTypes': 'Covalent C-H σ bonds',
        'numAtoms': 5,
        'numBonds': 4,
        'hybridization': 'sp³',
        'polarity': 'Non-polar (μ = 0 D)',
        'physicalProps': 'Colorless, odorless gas; mp -182.5°C, bp -161.5°C; density 0.717 g/L.',
        'chemicalProps': 'Combusts: CH₄ + 2O₂ → CO₂ + 2H₂O; free radical halogenation under UV light.',
        'uses': 'Primary fuel in natural gas heating, power generation, steam methane reforming for industrial H₂.',
        'facts': 'Methane is produced by methanogenic archaea in wetlands and digestive tracts of ruminants.',
        'atoms': [
            {'el': 'C', 'x': 0.0, 'y': 0.0, 'z': 0.0},
            {'el': 'H', 'x': 0.629, 'y': 0.629, 'z': 0.629},
            {'el': 'H', 'x': -0.629, 'y': -0.629, 'z': 0.629},
            {'el': 'H', 'x': -0.629, 'y': 0.629, 'z': -0.629},
            {'el': 'H', 'x': 0.629, 'y': -0.629, 'z': -0.629}
        ],
        'bonds': [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1]]
    })

    mols.append({
        'id': 'ethane',
        'name': 'Ethane',
        'formula': 'C₂H₆',
        'commonName': 'Dimethyl',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '30.070 g/mol',
        'geometry': 'Tetrahedral at each carbon',
        'bondAngles': '109.5°',
        'bondTypes': 'C-C σ bond and 6 C-H σ bonds',
        'numAtoms': 8,
        'numBonds': 7,
        'hybridization': 'sp³',
        'polarity': 'Non-polar (μ = 0 D)',
        'physicalProps': 'Colorless odorless gas; mp -182.8°C, bp -88.5°C.',
        'chemicalProps': 'Staggered conformation is 12.6 kJ/mol lower in energy than eclipsed; steam cracked to ethylene.',
        'uses': 'Petrochemical feedstock for ethylene manufacturing, refrigerant, fuel.',
        'facts': 'Ethane was first synthesized electrochemically by Michael Faraday in 1834 by electrolyzing potassium acetate.',
        'atoms': [
            {'el': 'C', 'x': -0.763, 'y': 0.0, 'z': 0.0},
            {'el': 'C', 'x': 0.763, 'y': 0.0, 'z': 0.0},
            {'el': 'H', 'x': -1.16, 'y': 1.02, 'z': 0.0},
            {'el': 'H', 'x': -1.16, 'y': -0.51, 'z': 0.88},
            {'el': 'H', 'x': -1.16, 'y': -0.51, 'z': -0.88},
            {'el': 'H', 'x': 1.16, 'y': -1.02, 'z': 0.0},
            {'el': 'H', 'x': 1.16, 'y': 0.51, 'z': 0.88},
            {'el': 'H', 'x': 1.16, 'y': 0.51, 'z': -0.88}
        ],
        'bonds': [[0, 1, 1], [0, 2, 1], [0, 3, 1], [0, 4, 1], [1, 5, 1], [1, 6, 1], [1, 7, 1]]
    })

    mols.append({
        'id': 'ethene',
        'name': 'Ethene',
        'formula': 'C₂H₄',
        'commonName': 'Ethylene',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '28.054 g/mol',
        'geometry': 'Planar',
        'bondAngles': '121.3° (H-C-H 117.4°)',
        'bondTypes': 'C=C double bond (1 σ + 1 π) + 4 C-H σ bonds',
        'numAtoms': 6,
        'numBonds': 5,
        'hybridization': 'sp²',
        'polarity': 'Non-polar (μ = 0 D)',
        'physicalProps': 'Colorless gas with sweetish aroma; mp -169.2°C, bp -103.7°C.',
        'chemicalProps': 'Electrophilic addition with Br₂/H₂O; readily polymerizes into polyethylene via Ziegler-Natta catalysis.',
        'uses': 'Production of polyethylene plastics, ethylene glycol antifreeze, natural ripening hormone for fruits.',
        'facts': 'Apples and bananas naturally emit ethene gas as an endogenous hormone to signal fruit ripening.',
        'atoms': [
            {'el': 'C', 'x': -0.669, 'y': 0.0, 'z': 0.0},
            {'el': 'C', 'x': 0.669, 'y': 0.0, 'z': 0.0},
            {'el': 'H', 'x': -1.235, 'y': 0.928, 'z': 0.0},
            {'el': 'H', 'x': -1.235, 'y': -0.928, 'z': 0.0},
            {'el': 'H', 'x': 1.235, 'y': 0.928, 'z': 0.0},
            {'el': 'H', 'x': 1.235, 'y': -0.928, 'z': 0.0}
        ],
        'bonds': [[0, 1, 2], [0, 2, 1], [0, 3, 1], [1, 4, 1], [1, 5, 1]]
    })

    mols.append({
        'id': 'ethyne',
        'name': 'Ethyne',
        'formula': 'C₂H₂',
        'commonName': 'Acetylene',
        'category': 'Simple Molecules',
        'categoryKey': 'simple',
        'mw': '26.038 g/mol',
        'geometry': 'Linear',
        'bondAngles': '180°',
        'bondTypes': 'C≡C triple bond (1 σ + 2 π) + 2 C-H σ bonds',
        'numAtoms': 4,
        'numBonds': 3,
        'hybridization': 'sp',
        'polarity': 'Non-polar (μ = 0 D)',
        'physicalProps': 'Colorless gas; sublimes at -84°C at atmospheric pressure.',
        'chemicalProps': 'Acidic terminal protons (pKa ~ 25); forms metal acetylides; burns at 3300°C in oxygen.',
        'uses': 'Oxy-acetylene cutting and welding torches, synthesis of vinyl monomers and synthetic resins.',
        'facts': 'The oxy-acetylene torch reaches 3,332°C, hot enough to melt and weld steel with precision.',
        'atoms': [
            {'el': 'C', 'x': -0.60, 'y': 0.0, 'z': 0.0},
            {'el': 'C', 'x': 0.60, 'y': 0.0, 'z': 0.0},
            {'el': 'H', 'x': -1.66, 'y': 0.0, 'z': 0.0},
            {'el': 'H', 'x': 1.66, 'y': 0.0, 'z': 0.0}
        ],
        'bonds': [[0, 1, 3], [0, 2, 1], [1, 3, 1]]
    })

    return mols

if __name__ == '__main__':
    m = get_molecules()
    print('Generated', len(m), 'molecules so far')
