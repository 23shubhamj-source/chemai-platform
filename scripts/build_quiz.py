import json
import os

questions = [
    # 1. Atomic Structure & Periodicity
    {
        'id': 'atom_1',
        'topic': 'atomic',
        'topicName': 'Atomic Structure & Periodicity',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'Which quantum number specifies the three-dimensional shape and subshell of an electron orbital?',
        'options': ['Principal quantum number (n)', 'Azimuthal / Angular momentum quantum number (l)', 'Magnetic quantum number (m_l)', 'Spin quantum number (m_s)'],
        'answer': 1,
        'explanation': 'The azimuthal quantum number (l) designates the angular momentum and geometric shape of the orbital (l=0: s orbital, l=1: p orbital, l=2: d orbital, l=3: f orbital).'
    },
    {
        'id': 'atom_2',
        'topic': 'atomic',
        'topicName': 'Atomic Structure & Periodicity',
        'diff': 'medium',
        'type': 'mcq',
        'q': 'What is the ground-state electron configuration of chromium (Cr, Z = 24)?',
        'options': ['[Ar] 4s² 3d⁴', '[Ar] 4s¹ 3d⁵', '[Ar] 4s⁰ 3d⁶', '[Ar] 3d⁶'],
        'answer': 1,
        'explanation': 'Chromium exhibits an anomalous configuration [Ar] 4s¹ 3d⁵ because half-filled 3d subshells provide extra exchange energy stability compared to [Ar] 4s² 3d⁴.'
    },
    {
        'id': 'atom_3',
        'topic': 'atomic',
        'topicName': 'Atomic Structure & Periodicity',
        'diff': 'hard',
        'type': 'tf',
        'q': 'True or False: Across a period from left to right, effective nuclear charge (Z_eff) increases, causing atomic radii to decrease.',
        'options': ['True', 'False'],
        'answer': 0,
        'explanation': 'True. As protons are added to the nucleus while electrons enter the same valence shell with poor mutual shielding, Z_eff increases and draws electron clouds closer.'
    },
    {
        'id': 'atom_4',
        'topic': 'atomic',
        'topicName': 'Atomic Structure & Periodicity',
        'diff': 'expert',
        'type': 'numerical',
        'q': 'Calculate the wavelength (in nm) of a photon emitted during the Balmer n=3 to n=2 transition in atomic hydrogen (R_H ≈ 1.097 × 10⁷ m⁻¹).',
        'options': ['486 nm', '656 nm', '434 nm', '122 nm'],
        'answer': 1,
        'explanation': '1/lambda = R_H * (1/2² - 1/3²) = 1.097e7 * (5/36) => lambda ≈ 656.3 nm (H-alpha spectral line).'
    },

    # 2. Chemical Bonding & Molecular Structure
    {
        'id': 'bond_1',
        'topic': 'bonding',
        'topicName': 'Chemical Bonding & Molecular Structure',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'According to VSEPR theory, what is the geometric shape of sulfur hexafluoride (SF₆)?',
        'options': ['Trigonal bipyramidal', 'Octahedral', 'Square planar', 'Tetrahedral'],
        'answer': 1,
        'explanation': 'SF₆ has 6 bonding pairs and 0 lone pairs around sulfur (steric number = 6), giving an octahedral geometry.'
    },
    {
        'id': 'bond_2',
        'topic': 'bonding',
        'topicName': 'Chemical Bonding & Molecular Structure',
        'diff': 'medium',
        'type': 'mcq',
        'q': 'What is the hybridization of the central iodine atom in triiodide ion (I₃⁻)?',
        'options': ['sp³', 'sp³d', 'sp³d²', 'dsp²'],
        'answer': 1,
        'explanation': 'The central iodine in I₃⁻ has 2 bonded iodine atoms and 3 equatorial lone pairs (steric number 5), requiring sp³d hybridization.'
    },
    {
        'id': 'bond_3',
        'topic': 'bonding',
        'topicName': 'Chemical Bonding & Molecular Structure',
        'diff': 'hard',
        'type': 'mcq',
        'q': 'According to Molecular Orbital Theory, what is the bond order and magnetic behavior of the oxygen molecule (O₂)?',
        'options': ['Bond order 2, Diamagnetic', 'Bond order 2, Paramagnetic', 'Bond order 2.5, Paramagnetic', 'Bond order 1.5, Diamagnetic'],
        'answer': 1,
        'explanation': 'O₂ has bond order (8 - 4)/2 = 2. The two unpaired electrons in degenerate pi* antibonding orbitals impart paramagnetism.'
    },

    # 3. Thermodynamics
    {
        'id': 'thermo_1',
        'topic': 'thermo',
        'topicName': 'Thermodynamics & Thermochemistry',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'Under what thermodynamic conditions is a chemical reaction spontaneous at all temperatures?',
        'options': ['ΔH > 0 and ΔS > 0', 'ΔH < 0 and ΔS > 0', 'ΔH > 0 and ΔS < 0', 'ΔH < 0 and ΔS < 0'],
        'answer': 1,
        'explanation': 'ΔG = ΔH - T·ΔS. When ΔH is negative (exothermic) and ΔS is positive (entropy increase), ΔG is negative at all temperatures.'
    },
    {
        'id': 'thermo_2',
        'topic': 'thermo',
        'topicName': 'Thermodynamics & Thermochemistry',
        'diff': 'medium',
        'type': 'numerical',
        'q': 'For a reaction with ΔH° = -40 kJ/mol and ΔS° = -80 J/(mol·K), at what temperature (Kelvin) does ΔG° become 0?',
        'options': ['300 K', '400 K', '500 K', '600 K'],
        'answer': 2,
        'explanation': 'T = ΔH° / ΔS° = (-40,000 J/mol) / (-80 J/(mol·K)) = 500 K.'
    },

    # 4. Chemical Kinetics
    {
        'id': 'kinetics_1',
        'topic': 'kinetics',
        'topicName': 'Chemical Kinetics & Catalysis',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'What are the SI units of the rate constant (k) for a first-order reaction?',
        'options': ['mol·L⁻¹·s⁻¹', 'L·mol⁻¹·s⁻¹', 's⁻¹', 'L²·mol⁻²·s⁻¹'],
        'answer': 2,
        'explanation': 'For first-order kinetics, rate = k[A] implies units of k = (mol/L/s)/(mol/L) = s⁻¹.'
    },
    {
        'id': 'kinetics_2',
        'topic': 'kinetics',
        'topicName': 'Chemical Kinetics & Catalysis',
        'diff': 'medium',
        'type': 'numerical',
        'q': 'If the half-life of a first-order reaction is 20 minutes, what fraction remains after 60 minutes?',
        'options': ['1/2 (50%)', '1/4 (25%)', '1/8 (12.5%)', '1/16 (6.25%)'],
        'answer': 2,
        'explanation': 'After 3 half-lives: (1/2)³ = 1/8 = 12.5%.'
    },

    # 5. Chemical & Ionic Equilibrium
    {
        'id': 'equil_1',
        'topic': 'equilibrium',
        'topicName': 'Chemical & Ionic Equilibrium',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'For the Haber synthesis: N₂ (g) + 3H₂ (g) ⇌ 2NH₃ (g), increasing total pressure shifts equilibrium:',
        'options': ['To the left', 'To the right (towards products)', 'No change', 'Reverses the reaction'],
        'answer': 1,
        'explanation': 'Increasing pressure shifts towards the side with fewer gas moles (4 moles of reactant gas vs. 2 moles of product gas).'
    },
    {
        'id': 'equil_2',
        'topic': 'equilibrium',
        'topicName': 'Chemical & Ionic Equilibrium',
        'diff': 'medium',
        'type': 'numerical',
        'q': 'What is the pH of an equimolar buffer of acetic acid (pKa = 4.76) and sodium acetate?',
        'options': ['3.76', '4.76', '5.76', '7.00'],
        'answer': 1,
        'explanation': 'pH = pKa + log([A⁻]/[HA]) = 4.76 + log(1) = 4.76.'
    },

    # 6. Electrochemistry
    {
        'id': 'electro_1',
        'topic': 'electrochem',
        'topicName': 'Electrochemistry & Redox Reactions',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'In any electrochemical cell, oxidation always takes place at the:',
        'options': ['Cathode', 'Anode', 'Salt bridge', 'External circuit'],
        'answer': 1,
        'explanation': 'Oxidation occurs at the anode (An Ox), and reduction occurs at the cathode (Red Cat).'
    },
    {
        'id': 'electro_2',
        'topic': 'electrochem',
        'topicName': 'Electrochemistry & Redox Reactions',
        'diff': 'medium',
        'type': 'numerical',
        'q': 'For Daniell cell with E°(Cu²⁺/Cu) = +0.34 V and E°(Zn²⁺/Zn) = -0.76 V, what is E°_cell?',
        'options': ['+0.42 V', '+1.10 V', '-1.10 V', '+0.76 V'],
        'answer': 1,
        'explanation': 'E°_cell = E°_cathode - E°_anode = +0.34 - (-0.76) = +1.10 V.'
    },

    # 7. Solutions
    {
        'id': 'sol_1',
        'topic': 'solutions',
        'topicName': 'Solutions & Colligative Properties',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'Which property is NOT a colligative property?',
        'options': ['Osmotic pressure', 'Boiling point elevation', 'Viscosity', 'Freezing point depression'],
        'answer': 2,
        'explanation': 'Viscosity depends on solute identity and structure, whereas colligative properties depend solely on the number of solute particles.'
    },

    # 8. Gases
    {
        'id': 'gas_1',
        'topic': 'gases',
        'topicName': 'States of Matter & Gas Laws',
        'diff': 'easy',
        'type': 'numerical',
        'q': 'What volume does 1 mole of an ideal gas occupy at STP (0°C, 1 atm)?',
        'options': ['11.2 L', '22.4 L', '24.5 L', '44.8 L'],
        'answer': 1,
        'explanation': 'At 273.15 K and 1 atm, molar gas volume is 22.414 L.'
    },

    # 9. Surface Chemistry
    {
        'id': 'surf_1',
        'topic': 'surface',
        'topicName': 'Surface Chemistry & Colloids',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'The scattering of a beam of light by colloidal particles is called the:',
        'options': ['Doppler effect', 'Tyndall effect', 'Raman effect', 'Zeeman effect'],
        'answer': 1,
        'explanation': 'The Tyndall effect is the optical scattering of light by suspended colloidal particles.'
    },

    # 10. Coordination
    {
        'id': 'coord_1',
        'topic': 'coordination',
        'topicName': 'Coordination Compounds',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'What is the coordination number of cobalt in [Co(NH₃)₆]³⁺?',
        'options': ['3', '4', '6', '8'],
        'answer': 2,
        'explanation': 'Six monodentate ammonia ligands coordinate to Co³⁺, giving a coordination number of 6.'
    },

    # 11. GOC
    {
        'id': 'goc_1',
        'topic': 'goc',
        'topicName': 'General Organic Chemistry (GOC)',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'Which carbocation is the most stable?',
        'options': ['Methyl (CH₃⁺)', 'Primary (CH₃CH₂⁺)', 'Secondary ((CH₃)₂CH⁺)', 'Tertiary ((CH₃)₃C⁺)'],
        'answer': 3,
        'explanation': 'Tertiary carbocations have 9 hyperconjugative alpha-hydrogens and strong +I stabilization.'
    },

    # 12. Hydrocarbons
    {
        'id': 'hydro_1',
        'topic': 'hydrocarbons',
        'topicName': 'Hydrocarbons (Alkanes, Alkenes, Alkynes)',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'In electrophilic addition of HBr to propene, the major product is:',
        'options': ['1-bromopropane', '2-bromopropane', '1,2-dibromopropane', 'cyclopropane'],
        'answer': 1,
        'explanation': 'Markovnikov addition yields 2-bromopropane via the more stable secondary carbocation intermediate.'
    },

    # 13. Haloalkanes
    {
        'id': 'halo_1',
        'topic': 'haloalkanes',
        'topicName': 'Haloalkanes & Haloarenes',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'An S_N2 reaction at a chiral center proceeds with:',
        'options': ['Complete inversion of configuration', 'Complete retention', 'Racemization', 'Rearrangement'],
        'answer': 0,
        'explanation': 'Backside attack in a concerted bimolecular mechanism leads to Walden inversion.'
    },

    # 14. Alcohols
    {
        'id': 'alc_1',
        'topic': 'alcohols',
        'topicName': 'Alcohols, Phenols & Ethers',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'Why is phenol more acidic than ethanol?',
        'options': ['Higher molar mass', 'Phenoxide anion is resonance-stabilized', 'Ethanol is aromatic', 'Phenol is insoluble'],
        'answer': 1,
        'explanation': 'Delocalization of the phenoxide negative charge into the aromatic ring lowers pKa to ~9.95 vs ~16 for ethanol.'
    },

    # 15. Carbonyls
    {
        'id': 'carb_1',
        'topic': 'carbonyls',
        'topicName': 'Aldehydes, Ketones & Carboxylic Acids',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'Which reagent gives a silver mirror test with aldehydes?',
        'options': ['Lucas reagent', 'Tollens reagent', 'Benedict reagent', 'Ninhydrin'],
        'answer': 1,
        'explanation': 'Tollens reagent reduces Ag⁺ to metallic silver upon oxidizing aldehydes.'
    },

    # 16. Nitrogen Compounds
    {
        'id': 'nitro_1',
        'topic': 'nitrogen',
        'topicName': 'Amines & Nitrogen Compounds',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'What is the order of basicity of methylamines in aqueous solution?',
        'options': ['(CH₃)₂NH > CH₃NH₂ > (CH₃)₃N > NH₃', '(CH₃)₃N > (CH₃)₂NH > CH₃NH₂ > NH₃', 'NH₃ > (CH₃)₃N > (CH₃)₂NH', 'CH₃NH₂ > (CH₃)₂NH > (CH₃)₃N'],
        'answer': 0,
        'explanation': '2° > 1° > 3° > NH₃ due to combined effects of inductive electron donation, steric hindrance, and hydration stability.'
    },

    # 17. Biomolecules
    {
        'id': 'bio_1',
        'topic': 'biomolecules',
        'topicName': 'Biomolecules & Polymers',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'What type of bond connects amino acids in a protein chain?',
        'options': ['Glycosidic', 'Peptide (amide)', 'Phosphodiester', 'Disulfide'],
        'answer': 1,
        'explanation': 'Peptide bonds (-CO-NH-) link amino acids together.'
    },

    # 18. Environmental
    {
        'id': 'env_1',
        'topic': 'environmental',
        'topicName': 'Environmental Chemistry',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'Which gases are the primary causes of acid rain?',
        'options': ['CO and CH₄', 'SO₂ and NO₂', 'O₂ and N₂', 'Ar and He'],
        'answer': 1,
        'explanation': 'SO₂ and NO₂ react with atmospheric water vapor to form H₂SO₄ and HNO₃.'
    },

    # 19. Spectroscopy
    {
        'id': 'spec_1',
        'topic': 'spectroscopy',
        'topicName': 'Spectroscopy & Analytical Techniques',
        'diff': 'easy',
        'type': 'mcq',
        'q': 'In IR spectroscopy, an intense peak near 1715 cm⁻¹ indicates:',
        'options': ['O-H stretch', 'C=O carbonyl stretch', 'C-O single bond', 'C≡C alkyne stretch'],
        'answer': 1,
        'explanation': 'The carbonyl C=O group creates an intense absorption peak between 1680-1750 cm⁻¹.'
    },

    # 20. Stoichiometry
    {
        'id': 'stoich_1',
        'topic': 'stoichiometry',
        'topicName': 'Stoichiometry & Mole Concept',
        'diff': 'easy',
        'type': 'numerical',
        'q': 'How many moles of CO₂ are produced from burning 1 mole of methane (CH₄ + 2O₂ → CO₂ + 2H₂O)?',
        'options': ['0.5 mole', '1.0 mole', '2.0 moles', '4.0 moles'],
        'answer': 1,
        'explanation': '1 mole of CH₄ yields 1 mole of CO₂.'
    }
]

with open('js/quiz-data.js', 'w', encoding='utf-8') as f:
    f.write('/* ChemAI Platform - 20-Topic Chemistry Question Bank */
')
    f.write('window.CHEMAI_QUIZ_QUESTIONS = ' + json.dumps(questions, indent=2, ensure_ascii=False) + ';
')

print(f'Wrote {len(questions)} quiz questions to js/quiz-data.js')
