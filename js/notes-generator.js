/* ==========================================================================
   ChemAI Platform - Advanced AI Chemistry Notes Generator
   10 Chemistry Branches x 10 Note Styles with Markdown Export & Live API
   ========================================================================== */

(function initNotesGenerator() {
  const PRESET_NOTES = {
    physical: {
      title: "Physical Chemistry Master Guide",
      summary: "Physical chemistry investigates macroscopic and particulate phenomena in chemical systems in terms of the principles, practices, and concepts of physics such as motion, energy, force, time, thermodynamics, quantum chemistry, and statistical mechanics.",
      formulas: [
        "First Law: ΔU = q + w (where w = -P·ΔV for PV work)",
        "Gibbs Spontaneity: ΔG = ΔH - T·ΔS",
        "Arrhenius Equation: k = A · exp(-Ea / (R·T))",
        "Nernst Equation: E = E° - (RT/nF) · ln(Q) = E° - (0.0592/n) · log10(Q) at 298 K",
        "Ideal Gas Law: P·V = n·R·T",
        "van 't Hoff Equation: d(ln K)/dT = ΔH° / (R·T²)"
      ],
      keyPoints: [
        "State functions (H, U, S, G) depend only on the initial and final states, independent of the path taken.",
        "A process is spontaneous when the total entropy of the universe increases (ΔS_universe > 0), equivalent to ΔG_sys < 0 at constant T and P.",
        "Catalysts accelerate reaction rates by providing an alternative reaction pathway with lower activation energy (Ea) without altering thermodynamic equilibrium ΔG or K_eq.",
        "Zero-order half-life depends directly on initial concentration: t_1/2 = [A]0 / (2k); first-order half-life is independent: t_1/2 = ln(2) / k."
      ],
      examTips: [
        "Watch signs: work done BY the system on surroundings has w < 0 under IUPAC conventions.",
        "Temperature in thermodynamic and kinetic formulas MUST always be in Kelvin (K = °C + 273.15).",
        "Remember that pure solids and pure liquids have unit activity (activity = 1) and are omitted from equilibrium constant expressions."
      ]
    },
    organic: {
      title: "Organic Chemistry & Reaction Mechanisms",
      summary: "Organic chemistry focuses on the structure, properties, composition, reactions, and synthesis of carbon-containing compounds. Reaction pathways are driven by nucleophilic-electrophilic interactions and orbital overlap.",
      formulas: [
        "Hückel's Rule for Aromaticity: Cyclic, planar, conjugated systems with (4n + 2) delocalized π-electrons",
        "Degree of Unsaturation: DoU = C - (H/2) - (Halogens/2) + (N/2) + 1",
        "Specific Optical Rotation: [α] = α / (c · l) (where c in g/mL, l in dm)"
      ],
      keyPoints: [
        "SN2 vs SN1: SN2 is bimolecular, concerted, backside attack causing Walden inversion; favored by methyl/1° halides and polar aprotic solvents (DMSO, DMF, acetone). SN1 is unimolecular, carbocation intermediate, racemization; favored by 3° halides and polar protic solvents (H2O, EtOH).",
        "Markovnikov's Rule: Electrophiles (H+) add to the alkene carbon with the greater number of hydrogens, producing the more stable carbocation intermediate.",
        "Acidity Trends: Carboxylic acids > Phenols > Water > Alcohols > Terminal Alkynes > Amines > Alkenes > Alkanes. Resonance delocalization and inductive electron withdrawal increase acidity."
      ],
      examTips: [
        "Always evaluate carbocation rearrangement (hydride or methyl shifts) whenever a secondary carbocation is adjacent to a tertiary or quaternary carbon.",
        "Remember Zaitsev's rule: elimination reactions preferentially yield the more substituted, thermodynamically stable alkene, unless a bulky hindered base (like potassium tert-butoxide) enforces Hofmann anti-Zaitsev regiochemistry."
      ]
    },
    inorganic: {
      title: "Inorganic Chemistry & Coordination Complexes",
      summary: "Inorganic chemistry explores the synthesis, bonding, and electronic structures of metals, non-metals, coordination complexes, and organometallics.",
      formulas: [
        "Crystal Field Stabilization Energy (Octahedral): CFSE = (-0.4·t2g + 0.6·eg)·Δo + P",
        "Magnetic Moment (Spin-only formula): μ_eff = sqrt(n · (n + 2)) Bohr Magnetons (BM), where n = unpaired electrons",
        "Effective Atomic Number (EAN): EAN = Z - Oxidation State + 2 × (Coordination Number)"
      ],
      keyPoints: [
        "Spectrochemical Series: I- < Br- < S2- < SCN- < Cl- < NO3- < F- < OH- < C2O4(2-) < H2O < NCS- < edta < NH3 < en < NO2- < CN- < CO. Strong-field ligands create large Δo, causing low-spin configurations.",
        "Jahn-Teller Distortion: Any non-linear molecular system in a degenerate electronic state will undergo geometrical distortion (typically axial elongation in d9 Cu2+ complexes) to remove orbital degeneracy and lower overall energy.",
        "Lanthanide Contraction: The steady decrease in atomic and ionic radii from Lanthanum to Lutetium caused by the poor shielding effect of 4f electrons, resulting in nearly identical covalent radii for 4d and 5d transition elements (e.g., Zr and Hf)."
      ],
      examTips: [
        "Transition metals lose ns valence electrons BEFORE (n-1)d electrons upon ionization (e.g., Fe is [Ar] 4s2 3d6, but Fe2+ is [Ar] 3d6).",
        "Check chelate effect: complexes with bidentate or polydentate chelating ligands (such as ethylenediamine or EDTA) have much higher formation constants due to favorable entropy release (ΔS > 0)."
      ]
    },
    analytical: {
      title: "Analytical Chemistry & Instrumental Methods",
      summary: "Analytical chemistry develops methods and instrumentation to separate, identify, and quantify chemical components in natural and artificial materials.",
      formulas: [
        "Beer-Lambert Law: A = ε · b · c (where ε is molar absorptivity in L/(mol·cm), b is pathlength in cm, c is molarity)",
        "Transmittance to Absorbance: A = -log10(T) = 2 - log10(%T)",
        "Chromatographic Resolution: R_s = 2 · (t_R2 - t_R1) / (w1 + w2)"
      ],
      keyPoints: [
        "Standard addition is used to eliminate complex matrix interference effects by spiking identical aliquots of sample with known increments of standard analyte.",
        "Internal standards compensate for random instrument variations, injection fluctuations, and evaporative sample losses in chromatographic analysis (GC/HPLC).",
        "In acid-base titrations, choose an indicator whose pKa is within ±1 unit of the equivalence point pH."
      ],
      examTips: [
        "Linearity in Beer's law holds best when absorbance A is between 0.1 and 1.0; at high concentrations (A > 1.5), electrostatic solute-solute interactions cause negative deviation."
      ]
    },
    biochemistry: {
      title: "Biochemistry & Cellular Macromolecules",
      summary: "Biochemistry examines chemical processes within living organisms, focusing on enzymatic catalysis, nucleic acid replication, protein folding, and bioenergetics.",
      formulas: [
        "Michaelis-Menten Equation: v0 = (Vmax · [S]) / (Km + [S])",
        "Lineweaver-Burk Double Reciprocal: 1/v0 = (Km / Vmax) · (1/[S]) + (1 / Vmax)",
        "Isoelectric Point of Amino Acids: pI = (pKa1 + pKa2) / 2"
      ],
      keyPoints: [
        "Km represents the substrate concentration at which reaction velocity is exactly half of Vmax. Lower Km signifies higher substrate affinity.",
        "Competitive inhibitors increase apparent Km without changing Vmax (can be overcome by excess substrate). Non-competitive inhibitors reduce Vmax without altering Km.",
        "DNA double helix is stabilized by Watson-Crick hydrogen bonding (2 H-bonds for A=T, 3 H-bonds for G≡C) and hydrophobic base stacking interactions."
      ],
      examTips: [
        "Lineweaver-Burk plot x-intercept is -1/Km and y-intercept is 1/Vmax. Competitive inhibition causes lines to intersect at the y-axis."
      ]
    },
    environmental: {
      title: "Environmental Chemistry & Green Metrics",
      summary: "Environmental chemistry analyzes the sources, reactions, transport, and fates of chemical species in water, air, soil, and living environments.",
      formulas: [
        "Atom Economy (%): (Molecular Mass of Desired Product / Total Molecular Mass of all Reactants) × 100%",
        "Environmental Factor (E-factor): Total Mass of Waste (kg) / Mass of Desired Product (kg)",
        "Biochemical Oxygen Demand: BOD = DO_initial - DO_final (after 5 days incubation at 20°C)"
      ],
      keyPoints: [
        "Stratospheric Ozone Depletion: Initiated by photolytic cleavage of CFCs by UV-C, liberating free chlorine radicals Cl• which catalytically destroy O3 without being consumed.",
        "Green Chemistry 12 Principles emphasize waste prevention, atom economy, less hazardous chemical syntheses, safer solvents, energy efficiency, and renewable feedstocks."
      ],
      examTips: [
        "Acid rain is defined as precipitation with pH < 5.6 (normal rain is slightly acidic at pH ~5.6 due to dissolved CO2 forming carbonic acid H2CO3)."
      ]
    },
    industrial: {
      title: "Industrial & Applied Chemistry Processes",
      summary: "Exploration of large-scale chemical syntheses that sustain modern agriculture, polymers, pharmaceuticals, and manufacturing.",
      formulas: [
        "Percent Yield: (Actual Yield / Theoretical Maximum Yield) × 100%",
        "Haber-Bosch Enthalpy: N2 (g) + 3H2 (g) ⇌ 2NH3 (g), ΔH = -92.4 kJ/mol",
        "Contact Process Oxidation: 2SO2 (g) + O2 (g) ⇌ 2SO3 (g), V2O5 catalyst"
      ],
      keyPoints: [
        "Haber-Bosch operates under compromise conditions: 450°C (fast kinetics despite unfavorable exothermic equilibrium) and 200 atm (high pressure shifts toward products) over an Fe/K2O/Al2O3 catalyst.",
        "Polymers are synthesized via addition polymerization (free radical or Ziegler-Natta, e.g. polyethylene) or condensation polymerization (step-growth releasing small byproduct like H2O, e.g. Nylon-6,6 and PET)."
      ],
      examTips: [
        "Remember that SO3 is not dissolved directly in water in the Contact process because the reaction is violently exothermic and creates an unmanageable acid mist; instead it is absorbed in concentrated H2SO4 to yield oleum (H2S2O7)."
      ]
    },
    electrochem: {
      title: "Advanced Electrochemistry & Energy Systems",
      summary: "Study of electrical energy interconversion with chemical reactions, interfacial electron transfers, battery chemistry, and electrolytic cells.",
      formulas: [
        "Faraday's Law of Electrolysis: m = (Q · M) / (n · F) = (I · t · M) / (n · F)",
        "Cell Potential to Equilibrium: E°_cell = (0.0592 V / n) · log10(K_eq) at 298.15 K",
        "Electrical Work: W_max = - ΔG = n · F · E_cell"
      ],
      keyPoints: [
        "Lithium-ion batteries operate via intercalation of Li+ ions into graphite anodes and transition metal oxide cathodes (e.g. LiCoO2) without metallic lithium deposition.",
        "Fuel cells directly convert chemical energy of a fuel (H2) and oxidant (O2) into electricity with water as the only exhaust: 2H2 + O2 → 2H2O (efficiency > 60%)."
      ],
      examTips: [
        "Standard electrode potentials are always listed as REDUCTION potentials. More positive E° means greater tendency to be reduced (stronger oxidizing agent)."
      ]
    },
    thermo: {
      title: "Chemical Thermodynamics & Statistical Mechanics",
      summary: "Macroscopic equilibrium thermodynamics analyzing entropy, chemical potentials, phase diagrams, and spontaneity criteria.",
      formulas: [
        "Entropy of Mixing: ΔS_mix = - R · Σ (ni · ln(xi))",
        "Clausius-Clapeyron Equation: ln(P2/P1) = - (ΔH_vap / R) · (1/T2 - 1/T1)",
        "Gibbs Phase Rule: F = C - P + 2 (Degrees of freedom = Components - Phases + 2)"
      ],
      keyPoints: [
        "At the triple point of water (0.01°C, 611.65 Pa), three phases coexist in equilibrium, giving zero degrees of freedom (invariant state).",
        "Residual entropy at 0 K arises from spatial or configurational disorder (e.g. in CO or ice crystal structures) where molecules freeze in random orientations."
      ],
      examTips: [
        "For Clausius-Clapeyron, ensure R is in J/(mol·K) (8.314) and ΔH_vap is in J/mol (convert kJ to J by multiplying by 1000)."
      ]
    },
    spectroscopy: {
      title: "Spectroscopy & Structure Elucidation",
      summary: "Techniques for deducing unknown molecular structures through interaction with electromagnetic radiation and mass fragmentation.",
      formulas: [
        "Planck-Einstein Relation: E = h · ν = (h · c) / λ = h · c · ν_bar",
        "Chemical Shift: δ (ppm) = (ν_sample - ν_TMS in Hz) / (Spectrometer frequency in MHz)",
        "Spin-Spin Splitting: Multiplicity = 2nI + 1 (for protons where I=1/2, Multiplicity = n + 1)"
      ],
      keyPoints: [
        "IR Functional Groups: Broad O-H stretch at 3200-3600 cm⁻¹, sharp C=O stretch at 1680-1750 cm⁻¹, terminal alkyne C≡C at ~2100-2260 cm⁻¹ and ≡C-H at 3300 cm⁻¹.",
        "Mass Spectrometry Nitrogen Rule: Organic molecules containing an odd number of nitrogen atoms have an odd nominal molecular weight (M+); even number or zero nitrogens gives an even molecular weight."
      ],
      examTips: [
        "Look for halogen signatures in MS: Chlorine exhibits a 3:1 ratio of [M]+ to [M+2]+ (due to 35Cl and 37Cl); Bromine exhibits an unmistakable 1:1 ratio (due to 79Br and 81Br)."
      ]
    }
  };

  window.generateAINotes = async function() {
    const branch = document.getElementById("notesTopicSelect")?.value || "physical";
    const style = document.getElementById("notesStyleSelect")?.value || "summary";
    const level = document.getElementById("notesLevelSelect")?.value || "AP / Undergraduate Chemistry";
    const outputContainer = document.getElementById("notesOutputContent");

    if (!outputContainer) return;
    outputContainer.innerHTML = '<div style="display:flex;align-items:center;gap:0.75rem;padding:1.5rem;color:var(--color-emerald);"><span class="typing-dot"></span> Generating comprehensive structured chemistry notes...</div>';

    // Try backend API first
    try {
      const response = await fetch("/api/generate-notes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ branch, style, level })
      });

      if (response.ok) {
        const data = await response.json();
        if (data.notes) {
          renderGeneratedNotes(data.title || branch, data.notes, level, style);
          return;
        }
      }
    } catch (err) {
      // Backend not running, use client-side curated templates
    }

    // Fallback to client data
    const tmpl = PRESET_NOTES[branch] || PRESET_NOTES.physical;
    let contentHtml = `
      <div style="margin-bottom:1.25rem;">
        <h4 style="color:var(--color-emerald);font-size:1.1rem;margin-bottom:0.4rem;">Core Overview</h4>
        <p style="color:var(--text-main);line-height:1.6;">${tmpl.summary}</p>
      </div>

      <div style="margin-bottom:1.25rem;">
        <h4 style="color:var(--color-emerald);font-size:1.1rem;margin-bottom:0.5rem;">Key Formulas & Quantitative Principles</h4>
        <ul style="padding-left:1.25rem;color:var(--text-main);line-height:1.7;">
          ${tmpl.formulas.map(f => `<li><code style="background:var(--bg-surface);padding:0.15rem 0.4rem;border-radius:4px;color:var(--color-cyan);font-family:var(--font-mono);">${f}</code></li>`).join("")}
        </ul>
      </div>

      <div style="margin-bottom:1.25rem;">
        <h4 style="color:var(--color-emerald);font-size:1.1rem;margin-bottom:0.5rem;">Fundamental Mechanisms & Conceptual Pillars</h4>
        <ul style="padding-left:1.25rem;color:var(--text-main);line-height:1.7;">
          ${tmpl.keyPoints.map(p => `<li>${p}</li>`).join("")}
        </ul>
      </div>

      <div style="background:rgba(16,185,129,0.08);border-left:3px solid var(--color-emerald);padding:0.9rem 1.1rem;border-radius:0 6px 6px 0;">
        <h4 style="color:var(--color-emerald);font-size:1rem;margin-bottom:0.35rem;">High-Yield Exam Strategy</h4>
        <ul style="padding-left:1.25rem;color:var(--text-muted);font-size:0.88rem;line-height:1.6;margin:0;">
          ${tmpl.examTips.map(t => `<li>${t}</li>`).join("")}
        </ul>
      </div>
    `;

    renderGeneratedNotes(tmpl.title, contentHtml, level, style);
  };

  function renderGeneratedNotes(title, bodyContent, level, style) {
    const outputContainer = document.getElementById("notesOutputContent");
    if (!outputContainer) return;

    window._currentNotesMarkdown = `# ${title}
Standard: ${level} | Style: ${style}

` + bodyContent.replace(/<[^>]+>/g, "
").replace(/
\s*
/g, "

");

    outputContainer.innerHTML = `
      <div style="border-bottom: 2px solid var(--border-emerald); padding-bottom: 0.75rem; margin-bottom: 1.25rem;">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;margin-bottom:0.35rem;">
          <span class="chip chip-emerald">${style.toUpperCase()} · ${level}</span>
          <span style="font-size:0.8rem;color:var(--color-emerald);">ChemAI Knowledge Engine</span>
        </div>
        <h3 style="font-size: 1.4rem; color: var(--text-highlight); margin: 0.25rem 0;">${title}</h3>
      </div>
      <div style="font-size:0.92rem;color:var(--text-main);line-height:1.65;">
        ${bodyContent}
      </div>
    `;
  }

  window.copyNotesToClipboard = function() {
    const text = window._currentNotesMarkdown || document.getElementById("notesOutputContent")?.innerText;
    if (text) {
      navigator.clipboard.writeText(text).then(() => {
        alert("Study notes successfully copied to clipboard!");
      });
    }
  };

  window.downloadNotesMarkdown = function() {
    const text = window._currentNotesMarkdown || document.getElementById("notesOutputContent")?.innerText;
    if (!text) {
      alert("Please generate notes first.");
      return;
    }
    const blob = new Blob([text], { type: "text/markdown;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = "ChemAI-Study-Notes.md";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
  };

  window.printNotes = function() {
    const content = document.getElementById("notesOutputContent")?.innerHTML;
    if (!content) return;
    const printWin = window.open("", "_blank");
    printWin.document.write(`
      <html>
        <head>
          <title>ChemAI Study Notes</title>
          <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; padding: 2rem; color: #111; }
            h2, h3, h4 { color: #059669; }
            code { background: #f1f5f9; padding: 2px 6px; border-radius: 4px; font-family: monospace; }
            ul { padding-left: 20px; }
          </style>
        </head>
        <body>${content}</body>
      </html>
    `);
    printWin.document.close();
    printWin.focus();
    printWin.print();
  };
})();
