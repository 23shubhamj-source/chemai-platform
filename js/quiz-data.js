/* ChemAI Platform Question Bank */
window.CHEMAI_QUIZ_QUESTIONS = [
  {
    "id": "atom_1",
    "topic": "atomic",
    "topicName": "Atomic Structure & Periodicity",
    "diff": "easy",
    "type": "mcq",
    "q": "Which quantum number specifies orbital shape?",
    "options": [
      "Principal (n)",
      "Azimuthal (l)",
      "Magnetic (ml)",
      "Spin (ms)"
    ],
    "answer": 1,
    "explanation": "Azimuthal quantum number l defines orbital shape."
  },
  {
    "id": "atom_2",
    "topic": "atomic",
    "topicName": "Atomic Structure & Periodicity",
    "diff": "medium",
    "type": "mcq",
    "q": "What is ground-state electron configuration of Cr (Z=24)?",
    "options": [
      "[Ar] 4s2 3d4",
      "[Ar] 4s1 3d5",
      "[Ar] 4s0 3d6",
      "[Ar] 3d6"
    ],
    "answer": 1,
    "explanation": "Half-filled 3d5 shell provides extra exchange energy stability."
  },
  {
    "id": "atom_3",
    "topic": "atomic",
    "topicName": "Atomic Structure & Periodicity",
    "diff": "hard",
    "type": "tf",
    "q": "True or False: Across a period, effective nuclear charge increases, decreasing atomic radius.",
    "options": [
      "True",
      "False"
    ],
    "answer": 0,
    "explanation": "True. Z_eff increases as protons are added to same valence shell."
  },
  {
    "id": "atom_4",
    "topic": "atomic",
    "topicName": "Atomic Structure & Periodicity",
    "diff": "expert",
    "type": "numerical",
    "q": "What is the wavelength of Balmer n=3 to n=2 line in H?",
    "options": [
      "486 nm",
      "656 nm",
      "434 nm",
      "122 nm"
    ],
    "answer": 1,
    "explanation": "656.3 nm is the H-alpha red line."
  },
  {
    "id": "bond_1",
    "topic": "bonding",
    "topicName": "Chemical Bonding & Structure",
    "diff": "easy",
    "type": "mcq",
    "q": "What is the shape of SF6 according to VSEPR?",
    "options": [
      "Trigonal bipyramidal",
      "Octahedral",
      "Square planar",
      "Tetrahedral"
    ],
    "answer": 1,
    "explanation": "6 bonding pairs and 0 lone pairs form an octahedron."
  },
  {
    "id": "bond_2",
    "topic": "bonding",
    "topicName": "Chemical Bonding & Structure",
    "diff": "medium",
    "type": "mcq",
    "q": "What is hybridization of central I in I3-?",
    "options": [
      "sp3",
      "sp3d",
      "sp3d2",
      "dsp2"
    ],
    "answer": 1,
    "explanation": "2 bonds and 3 lone pairs gives steric number 5 (sp3d)."
  },
  {
    "id": "bond_3",
    "topic": "bonding",
    "topicName": "Chemical Bonding & Structure",
    "diff": "hard",
    "type": "mcq",
    "q": "What is bond order and magnetic behavior of O2 in MO theory?",
    "options": [
      "2, Diamagnetic",
      "2, Paramagnetic",
      "2.5, Paramagnetic",
      "1.5, Diamagnetic"
    ],
    "answer": 1,
    "explanation": "Bond order 2 with two unpaired pi* electrons makes it paramagnetic."
  },
  {
    "id": "thermo_1",
    "topic": "thermo",
    "topicName": "Thermodynamics",
    "diff": "easy",
    "type": "mcq",
    "q": "When is a reaction spontaneous at all temperatures?",
    "options": [
      "dH > 0, dS > 0",
      "dH < 0, dS > 0",
      "dH > 0, dS < 0",
      "dH < 0, dS < 0"
    ],
    "answer": 1,
    "explanation": "Negative dH and positive dS ensures negative dG."
  },
  {
    "id": "thermo_2",
    "topic": "thermo",
    "topicName": "Thermodynamics",
    "diff": "medium",
    "type": "numerical",
    "q": "If dH = -40 kJ/mol and dS = -80 J/(mol K), at what T does dG = 0?",
    "options": [
      "300 K",
      "400 K",
      "500 K",
      "600 K"
    ],
    "answer": 2,
    "explanation": "T = dH / dS = -40000 / -80 = 500 K."
  },
  {
    "id": "kinetics_1",
    "topic": "kinetics",
    "topicName": "Chemical Kinetics",
    "diff": "easy",
    "type": "mcq",
    "q": "What is unit of k for first-order reaction?",
    "options": [
      "mol L-1 s-1",
      "L mol-1 s-1",
      "s-1",
      "L2 mol-2 s-1"
    ],
    "answer": 2,
    "explanation": "First-order rate constant has units of reciprocal time (s-1)."
  },
  {
    "id": "kinetics_2",
    "topic": "kinetics",
    "topicName": "Chemical Kinetics",
    "diff": "medium",
    "type": "numerical",
    "q": "If t1/2 = 20 min for 1st order reaction, what fraction remains after 60 min?",
    "options": [
      "1/2 (50%)",
      "1/4 (25%)",
      "1/8 (12.5%)",
      "1/16 (6.25%)"
    ],
    "answer": 2,
    "explanation": "(1/2)^3 = 1/8."
  },
  {
    "id": "equil_1",
    "topic": "equilibrium",
    "topicName": "Chemical Equilibrium",
    "diff": "easy",
    "type": "mcq",
    "q": "Increasing pressure on N2 + 3H2 <=> 2NH3 shifts equilibrium:",
    "options": [
      "Left",
      "Right",
      "No change",
      "Halts"
    ],
    "answer": 1,
    "explanation": "Shifts towards fewer gas moles (4 moles -> 2 moles)."
  },
  {
    "id": "equil_2",
    "topic": "equilibrium",
    "topicName": "Chemical Equilibrium",
    "diff": "medium",
    "type": "numerical",
    "q": "What is pH of buffer with 0.1M CH3COOH (pKa 4.76) and 0.1M CH3COONa?",
    "options": [
      "3.76",
      "4.76",
      "5.76",
      "7.00"
    ],
    "answer": 1,
    "explanation": "pH = pKa + log(1) = 4.76."
  },
  {
    "id": "electro_1",
    "topic": "electrochem",
    "topicName": "Electrochemistry",
    "diff": "easy",
    "type": "mcq",
    "q": "Oxidation always occurs at which electrode?",
    "options": [
      "Cathode",
      "Anode",
      "Salt bridge",
      "Potentiometer"
    ],
    "answer": 1,
    "explanation": "Anode is site of oxidation (An Ox)."
  },
  {
    "id": "electro_2",
    "topic": "electrochem",
    "topicName": "Electrochemistry",
    "diff": "medium",
    "type": "numerical",
    "q": "Given E(Cu2+/Cu)=+0.34V and E(Zn2+/Zn)=-0.76V, what is E_cell?",
    "options": [
      "+0.42 V",
      "+1.10 V",
      "-1.10 V",
      "+0.76 V"
    ],
    "answer": 1,
    "explanation": "0.34 - (-0.76) = +1.10 V."
  },
  {
    "id": "sol_1",
    "topic": "solutions",
    "topicName": "Solutions & Colligative Properties",
    "diff": "easy",
    "type": "mcq",
    "q": "Which is NOT a colligative property?",
    "options": [
      "Osmotic pressure",
      "Boiling point elevation",
      "Viscosity",
      "Freezing point depression"
    ],
    "answer": 2,
    "explanation": "Viscosity depends on intermolecular forces, not particle count."
  },
  {
    "id": "gas_1",
    "topic": "gases",
    "topicName": "Gas Laws",
    "diff": "easy",
    "type": "numerical",
    "q": "Molar volume of ideal gas at STP (0 C, 1 atm) is:",
    "options": [
      "11.2 L",
      "22.4 L",
      "24.5 L",
      "44.8 L"
    ],
    "answer": 1,
    "explanation": "22.414 L at STP."
  },
  {
    "id": "surf_1",
    "topic": "surface",
    "topicName": "Surface Chemistry",
    "diff": "easy",
    "type": "mcq",
    "q": "Scattering of light by colloidal particles is called:",
    "options": [
      "Doppler effect",
      "Tyndall effect",
      "Raman effect",
      "Compton effect"
    ],
    "answer": 1,
    "explanation": "Tyndall effect makes beam path visible in colloids."
  },
  {
    "id": "coord_1",
    "topic": "coordination",
    "topicName": "Coordination Chemistry",
    "diff": "easy",
    "type": "mcq",
    "q": "Coordination number of Co in [Co(NH3)6]3+ is:",
    "options": [
      "3",
      "4",
      "6",
      "8"
    ],
    "answer": 2,
    "explanation": "Six monodentate ammonia ligands coordinate to Co."
  },
  {
    "id": "goc_1",
    "topic": "goc",
    "topicName": "General Organic Chemistry",
    "diff": "easy",
    "type": "mcq",
    "q": "Which carbocation is most stable?",
    "options": [
      "Methyl",
      "Ethyl",
      "Isopropyl",
      "tert-Butyl"
    ],
    "answer": 3,
    "explanation": "Tertiary carbocation has 9 alpha hydrogens providing hyperconjugation."
  },
  {
    "id": "hydro_1",
    "topic": "hydrocarbons",
    "topicName": "Hydrocarbons",
    "diff": "easy",
    "type": "mcq",
    "q": "Addition of HBr to propene gives major product:",
    "options": [
      "1-bromopropane",
      "2-bromopropane",
      "1,2-dibromopropane",
      "propane"
    ],
    "answer": 1,
    "explanation": "Markovnikov addition produces 2-bromopropane."
  },
  {
    "id": "halo_1",
    "topic": "haloalkanes",
    "topicName": "Haloalkanes",
    "diff": "easy",
    "type": "mcq",
    "q": "SN2 reaction mechanism proceeds with:",
    "options": [
      "Walden inversion of configuration",
      "Retention",
      "Racemization",
      "Rearrangement"
    ],
    "answer": 0,
    "explanation": "Backside nucleophilic attack causes complete stereochemical inversion."
  },
  {
    "id": "alc_1",
    "topic": "alcohols",
    "topicName": "Alcohols & Phenols",
    "diff": "easy",
    "type": "mcq",
    "q": "Why is phenol more acidic than ethanol?",
    "options": [
      "Phenol has higher mass",
      "Phenoxide is resonance stabilized",
      "Ethanol is aromatic",
      "Phenol is neutral"
    ],
    "answer": 1,
    "explanation": "Phenoxide negative charge delocalizes into aromatic ring."
  },
  {
    "id": "carb_1",
    "topic": "carbonyls",
    "topicName": "Aldehydes & Ketones",
    "diff": "easy",
    "type": "mcq",
    "q": "Tollens test produces silver mirror with:",
    "options": [
      "Ketones only",
      "Aldehydes",
      "Ethers",
      "Tertiary alcohols"
    ],
    "answer": 1,
    "explanation": "Aldehydes reduce Tollens reagent [Ag(NH3)2]+ to silver mirror."
  },
  {
    "id": "nitro_1",
    "topic": "nitrogen",
    "topicName": "Amines",
    "diff": "easy",
    "type": "mcq",
    "q": "Aqueous basicity order of methylamines is:",
    "options": [
      "2 > 1 > 3 > NH3",
      "3 > 2 > 1 > NH3",
      "NH3 > 3 > 2",
      "1 > 2 > 3"
    ],
    "answer": 0,
    "explanation": "2 > 1 > 3 > NH3 due to inductive, steric, and hydration balance."
  },
  {
    "id": "bio_1",
    "topic": "biomolecules",
    "topicName": "Biomolecules",
    "diff": "easy",
    "type": "mcq",
    "q": "Linkage connecting amino acids in proteins is:",
    "options": [
      "Glycosidic",
      "Peptide (amide)",
      "Phosphodiester",
      "Ester"
    ],
    "answer": 1,
    "explanation": "Peptide bond (-CO-NH-) links amino acids."
  },
  {
    "id": "env_1",
    "topic": "environmental",
    "topicName": "Environmental Chemistry",
    "diff": "easy",
    "type": "mcq",
    "q": "Major gases responsible for acid rain are:",
    "options": [
      "CO and CH4",
      "SO2 and NO2",
      "O2 and N2",
      "Ar and He"
    ],
    "answer": 1,
    "explanation": "SO2 and NO2 form sulfuric and nitric acids in rainwater."
  },
  {
    "id": "spec_1",
    "topic": "spectroscopy",
    "topicName": "Spectroscopy",
    "diff": "easy",
    "type": "mcq",
    "q": "Strong IR absorption near 1715 cm-1 is:",
    "options": [
      "O-H stretch",
      "C=O stretch",
      "C-O stretch",
      "C#C stretch"
    ],
    "answer": 1,
    "explanation": "Carbonyl C=O stretch produces intense band near 1715 cm-1."
  },
  {
    "id": "stoich_1",
    "topic": "stoichiometry",
    "topicName": "Stoichiometry",
    "diff": "easy",
    "type": "numerical",
    "q": "Combustion of 1 mole of CH4 produces how many moles of CO2?",
    "options": [
      "0.5 mol",
      "1.0 mol",
      "2.0 mol",
      "4.0 mol"
    ],
    "answer": 1,
    "explanation": "CH4 + 2O2 -> CO2 + 2H2O yields 1 mole CO2."
  }
];
