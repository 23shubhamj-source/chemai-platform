/* ==========================================================================
   ChemAI Platform - Advanced AI Chemistry Notes Generator
   15+ Chemistry Disciplines x 10 Note Styles with Markdown Export & Live API
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
        "Nernst Equation: E = E° - (RT/nF)·ln(Q) = E° - (0.0592/n)·log10(Q) at 298 K",
        "Ideal Gas Law: P·V = n·R·T",
        "van 't Hoff Equation: d(ln K)/dT = ΔH° / (R·T²)"
      ],
      keyPoints: [
        "State functions (H, U, S, G) depend only on initial and final states, independent of path.",
        "A process is spontaneous when total universe entropy increases (ΔS_univ > 0), equivalent to ΔG_sys < 0 at constant T and P.",
        "Catalysts accelerate reaction rates by lowering activation energy (Ea) without altering equilibrium position K_eq.",
        "First-order half-life is concentration-independent: t_1/2 = ln(2) / k."
      ],
      examTips: [
        "Watch signs: work done BY the system on surroundings has w < 0 under IUPAC conventions.",
        "Temperature in thermodynamic and kinetic formulas MUST always be in Kelvin (K = °C + 273.15).",
        "Pure solids and liquids have unit activity (a = 1) and are omitted from equilibrium constant expressions."
      ]
    },
    bonding: {
      title: "Chemical Bonding, VSEPR & Molecular Structure",
      summary: "Chemical bonding represents the thermodynamic stabilization achieved when valence electrons are shared or transferred between atomic nuclei to minimize Coulombic potential energy.",
      formulas: [
        "Formal Charge: FC = Valence e⁻ - Nonbonding e⁻ - 0.5·(Bonding e⁻)",
        "Dipole Moment: μ = q · r (Debye units, 1 D = 3.336 × 10⁻³⁰ C·m)",
        "Bond Order: BO = 0.5 · (N_bonding - N_antibonding)"
      ],
      keyPoints: [
        "VSEPR Theory: Electron pairs repel each other to adopt shapes maximizing spatial separation.",
        "Repulsion hierarchy: Lone Pair - Lone Pair > Lone Pair - Bond Pair > Bond Pair - Bond Pair.",
        "Hybridization models: sp (linear 180°), sp² (trigonal planar 120°), sp³ (tetrahedral 109.5°), sp³d (trigonal bipyramidal), sp³d² (octahedral 90°)."
      ],
      examTips: [
        "Exceptions to octet rule: Incomplete octet (BeCl₂, BF₃), odd-electron molecules (NO, NO₂), expanded octet (PCl₅, SF₆).",
        "Resonance structures do not physically interconvert; the real molecule is a single resonance hybrid."
      ]
    },
    thermo: {
      title: "Thermodynamics & Spontaneity Master Sheet",
      summary: "Chemical thermodynamics governs heat and work transformations, enthalpy changes, entropy generation, and free energy criteria for equilibrium.",
      formulas: [
        "Reaction Enthalpy: ΔH°_rxn = Σ n·ΔH°_f(products) - Σ m·ΔH°_f(reactants)",
        "Gibbs Free Energy: ΔG° = ΔH° - T·ΔS° = -R·T·ln(K_eq)",
        "Hess's Law: ΔH_total = ΔH₁ + ΔH₂ + ΔH₃",
        "Clausius-Clapeyron: ln(P₂/P₁) = - (ΔH_vap / R) · (1/T₂ - 1/T₁)"
      ],
      keyPoints: [
        "Second Law: Total entropy of the universe strictly increases for spontaneous processes (ΔS_univ > 0).",
        "Third Law: Entropy of a pure perfect crystalline substance is zero at absolute zero (0 K).",
        "When ΔH < 0 and ΔS > 0, ΔG is ALWAYS negative: spontaneous at all temperatures."
      ],
      examTips: [
        "Convert ΔH from kJ/mol to J/mol when computing ΔG = ΔH - TΔS where ΔS is in J/(mol·K).",
        "When ΔH and ΔS have identical signs, spontaneity depends on temperature: T_eq = ΔH / ΔS."
      ]
    },
    acids: {
      title: "Acids, Bases & Buffer Equilibria Guide",
      summary: "Acid-base chemistry explores proton transfer, electron-pair coordination, aqueous equilibrium constants, pH quantification, and buffer mechanisms.",
      formulas: [
        "pH & pOH: pH = -log10[H⁺], pOH = -log10[OH⁻]",
        "Autoionization of Water: Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴ at 25°C",
        "Henderson-Hasselbalch: pH = pKa + log10([A⁻] / [HA])",
        "Weak Acid Ionization: Ka = [H⁺][A⁻] / [HA]"
      ],
      keyPoints: [
        "Arrhenius: H⁺ / OH⁻ producers in water. Brønsted-Lowry: Proton donor / acceptor. Lewis: Electron pair acceptor / donor.",
        "Strong acids dissociate 100%: HCl, HBr, HI, HNO₃, HClO₄, H₂SO₄.",
        "Buffer solutions resist pH change; maximal buffer capacity occurs when pH = pKa."
      ],
      examTips: [
        "For a conjugate acid-base pair at 25°C: Ka · Kb = Kw = 10⁻¹⁴, so pKa + pKb = 14.00.",
        "In polyprotic acids (H₃PO₄), Ka1 >> Ka2 >> Ka3. The pH is governed primarily by Ka1."
      ]
    },
    organic: {
      title: "Organic Chemistry & Reaction Mechanisms",
      summary: "Organic chemistry focuses on the structure, properties, composition, reactions, and synthesis of carbon-containing compounds.",
      formulas: [
        "Hückel's Rule for Aromaticity: Planar cyclic conjugated rings containing (4n + 2) delocalized π-electrons",
        "Degree of Unsaturation: DoU = C - (H/2) - (Halogens/2) + (N/2) + 1"
      ],
      keyPoints: [
        "SN2 vs SN1: SN2 is bimolecular, concerted, backside attack causing Walden inversion; favored by 1° halides and polar aprotic solvents. SN1 is unimolecular, carbocation intermediate, racemization; favored by 3° halides.",
        "Markovnikov's Rule: Electrophiles add to alkene carbon holding more hydrogens, yielding the more stable carbocation.",
        "Acidity Trends: Carboxylic acids > Phenols > Water > Alcohols > Alkynes > Amines > Alkanes."
      ],
      examTips: [
        "Evaluate carbocation rearrangement (hydride or methyl shift) whenever a 2° carbocation is adjacent to 3°/4° centers.",
        "Zaitsev vs Hofmann: Non-bulky bases yield more substituted alkene; bulky bases (KOtBu) yield Hofmann alkene."
      ]
    },
    inorganic: {
      title: "Inorganic Chemistry & Coordination Complexes",
      summary: "Exploration of d-block transition metals, crystal field splitting, Werner complexes, and periodic trends.",
      formulas: [
        "CFSE (Octahedral): CFSE = (-0.4·t2g + 0.6·eg)·Δo + P",
        "Spin-Only Magnetic Moment: μ_eff = sqrt(n · (n + 2)) BM"
      ],
      keyPoints: [
        "Spectrochemical Series: I⁻ < Br⁻ < Cl⁻ < F⁻ < OH⁻ < H₂O < NH₃ < en < NO₂⁻ < CN⁻ < CO. Strong ligands cause low-spin.",
        "Jahn-Teller Effect: Non-linear molecules with degenerate ground states undergo geometric distortion.",
        "Lanthanide Contraction: Steady decrease in radii across 4f series makes 4d and 5d elements nearly identical in size."
      ],
      examTips: [
        "Transition metals lose ns electrons before (n-1)d electrons upon ionization: Fe is [Ar] 4s² 3d⁶, but Fe²⁺ is [Ar] 3d⁶.",
        "Chelate effect: Polydentate ligands form complexes with vastly higher stability constants due to ΔS > 0."
      ]
    },
    analytical: {
      title: "Analytical Chemistry & Instrumental Methods",
      summary: "Quantitative and qualitative measurement of chemical species, calibration, and instrumental spectroscopy.",
      formulas: [
        "Beer-Lambert Law: A = ε · b · c",
        "Absorbance: A = -log10(T) = 2 - log10(%T)"
      ],
      keyPoints: [
        "Standard addition eliminates complex matrix interference effects.",
        "Internal standards compensate for instrument fluctuations and sample loss in chromatography."
      ],
      examTips: [
        "Beer-Lambert law shows negative deviations at high concentrations (A > 1.5) due to electrostatic interactions."
      ]
    },
    biochemistry: {
      title: "Biochemistry & Cellular Macromolecules",
      summary: "Chemical processes within living systems, enzymology, bioenergetics, and macromolecular structures.",
      formulas: [
        "Michaelis-Menten: v0 = (Vmax · [S]) / (Km + [S])",
        "Lineweaver-Burk: 1/v0 = (Km / Vmax) · (1/[S]) + (1 / Vmax)"
      ],
      keyPoints: [
        "Km is substrate concentration where rate is half Vmax; lower Km indicates higher affinity.",
        "Competitive inhibitors increase apparent Km without changing Vmax. Non-competitive decrease Vmax."
      ],
      examTips: [
        "Enzymes accelerate rates by lowering activation barrier without changing thermodynamic ΔG° or equilibrium."
      ]
    },
    environmental: {
      title: "Environmental Chemistry & Green Metrics",
      summary: "Atmospheric, aquatic, and soil chemistry, pollution monitoring, and 12 Principles of Green Chemistry.",
      formulas: [
        "Atom Economy (%): (Mass of Desired Product / Total Mass of Reactants) × 100%",
        "Environmental Factor (E-Factor): Total Mass of Waste / Mass of Product"
      ],
      keyPoints: [
        "Ozone depletion is catalyzed by CFC chlorine radicals: Cl• + O₃ → ClO• + O₂.",
        "Acid rain is precipitation with pH < 5.6, caused by SO₂ and NO₂."
      ],
      examTips: [
        "Normal unpolluted rain is slightly acidic (pH ~5.6) due to dissolved atmospheric CO₂."
      ]
    },
    industrial: {
      title: "Industrial Chemistry & Chemical Processes",
      summary: "Large-scale commercial syntheses, reactor engineering, and polymer manufacturing.",
      formulas: [
        "Percentage Yield: (Actual Yield / Theoretical Yield) × 100%",
        "Haber Synthesis: N₂ + 3H₂ ⇌ 2NH₃, ΔH = -92.4 kJ/mol"
      ],
      keyPoints: [
        "Haber-Bosch compromise: 450°C and 200 atm over promoted iron catalyst.",
        "Contact process absorbs SO₃ into concentrated H₂SO₄ to form oleum, avoiding acid mist."
      ],
      examTips: [
        "Promoters: K₂O and Al₂O₃ enhance activity and prevent sintering of iron catalysts."
      ]
    },
    electrochem: {
      title: "Advanced Electrochemistry & Energy Systems",
      summary: "Electron transfer, galvanic and electrolytic cells, batteries, fuel cells, and corrosion kinetics.",
      formulas: [
        "Faraday's Law: m = (I · t · M) / (n · F)",
        "Cell Potential: ΔG° = -n · F · E°_cell",
        "Nernst Equation: E = E° - (0.0592/n) · log10(Q)"
      ],
      keyPoints: [
        "Anode is site of oxidation (An Ox); Cathode is site of reduction (Red Cat).",
        "Lithium-ion cells operate by reversible intercalation of Li⁺ ions between layered host structures."
      ],
      examTips: [
        "Standard reduction potentials are intensive properties: Never multiply E° when multiplying stoichiometric coefficients!"
      ]
    },
    spectroscopy: {
      title: "Spectroscopy & Molecular Characterization",
      summary: "Identification of chemical structures via infrared, NMR, UV-Vis, and mass spectrometry.",
      formulas: [
        "Planck Relation: E = h·ν = (h·c)/λ",
        "Chemical Shift: δ (ppm) = (ν_sample - ν_TMS) / Frequency in MHz",
        "Multiplicity: n + 1 (for protons)"
      ],
      keyPoints: [
        "IR: Broad O-H (3200-3600 cm⁻¹), sharp C=O (1680-1750 cm⁻¹), C-H (2850-3100 cm⁻¹).",
        "¹H-NMR: Chemical shift gives electronic environment; integral gives proton count; splitting gives neighbors."
      ],
      examTips: [
        "Halogen MS signatures: Chlorine has 3:1 [M]⁺ to [M+2]⁺ ratio; Bromine has 1:1 ratio."
      ]
    }
  };

  // Cross-reference aliases
  PRESET_NOTES.thermodynamics = PRESET_NOTES.thermo;
  PRESET_NOTES.acid = PRESET_NOTES.acids;
  PRESET_NOTES.kinetics = PRESET_NOTES.physical;
  PRESET_NOTES.equilibrium = PRESET_NOTES.acids;
  PRESET_NOTES.stoichiometry = PRESET_NOTES.physical;

  // Style Content Formatter
  function buildStyledNotesContent(data, style, level) {
    const title = data.title || "Chemistry Study Sheet";
    const summary = data.summary || "Core chemical principles and conceptual framework.";
    const formulas = data.formulas || [];
    const keyPoints = data.keyPoints || [];
    const examTips = data.examTips || [];

    let sectionsHtml = "";

    // Header badge
    sectionsHtml += `
      <div style="border-bottom:1px solid var(--border-subtle);padding-bottom:0.75rem;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
        <div>
          <h4 style="font-size:1.15rem;font-weight:700;color:var(--text-bright);margin:0;">${title}</h4>
          <span style="font-size:0.75rem;color:var(--color-emerald);font-weight:600;text-transform:uppercase;letter-spacing:0.05em;">Target: ${level}</span>
        </div>
        <span class="chip chip-cobalt" style="font-size:0.75rem;padding:0.25rem 0.6rem;text-transform:capitalize;">${style.replace('_', ' ')}</span>
      </div>
    `;

    // Overview section
    sectionsHtml += `
      <div style="margin-bottom:1.25rem;">
        <h5 style="font-size:0.85rem;text-transform:uppercase;letter-spacing:0.05em;color:var(--color-emerald);margin-bottom:0.4rem;display:flex;align-items:center;gap:0.4rem;">
          <span>&#9670;</span> Conceptual Overview
        </h5>
        <p style="color:var(--text-main);line-height:1.6;font-size:0.9rem;margin:0;">${summary}</p>
      </div>
    `;

    // Formulas Section
    if (formulas.length > 0 && (style === 'summary' || style === 'formulas' || style === 'exam_sheet' || style === 'textbook' || style === 'mechanisms')) {
      sectionsHtml += `
        <div style="margin-bottom:1.25rem;">
          <h5 style="font-size:0.85rem;text-transform:uppercase;letter-spacing:0.05em;color:var(--color-cyan, #06b6d4);margin-bottom:0.5rem;display:flex;align-items:center;gap:0.4rem;">
            <span>&#9670;</span> Essential Equations & Governing Laws
          </h5>
          <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(260px, 1fr));gap:0.6rem;">
            ${formulas.map(f => `
              <div style="background:rgba(255,255,255,0.03);border:1px solid rgba(255,255,255,0.08);border-left:3px solid var(--color-cyan, #06b6d4);padding:0.6rem 0.8rem;border-radius:4px;font-family:var(--font-mono, monospace);font-size:0.82rem;color:var(--text-bright);">
                ${f}
              </div>
            `).join('')}
          </div>
        </div>
      `;
    }

    // Key Takeaways & Core Concepts
    if (keyPoints.length > 0 && (style !== 'formulas')) {
      sectionsHtml += `
        <div style="margin-bottom:1.25rem;">
          <h5 style="font-size:0.85rem;text-transform:uppercase;letter-spacing:0.05em;color:var(--color-amber, #f59e0b);margin-bottom:0.5rem;display:flex;align-items:center;gap:0.4rem;">
            <span>&#9670;</span> Core Principles & Critical Mechanics
          </h5>
          <ul style="margin:0;padding-left:1.2rem;display:flex;flex-direction:column;gap:0.4rem;">
            ${keyPoints.map(kp => `
              <li style="color:var(--text-muted);font-size:0.88rem;line-height:1.5;">${kp}</li>
            `).join('')}
          </ul>
        </div>
      `;
    }

    // Exam Pitfalls & High-Yield Reminders
    if (examTips.length > 0 && (style === 'summary' || style === 'exam_sheet' || style === 'pitfalls' || style === 'flashcards' || style === 'textbook')) {
      sectionsHtml += `
        <div style="margin-bottom:0.75rem;background:rgba(239, 68, 68, 0.08);border:1px solid rgba(239, 68, 68, 0.25);border-radius:var(--radius-sm, 6px);padding:0.75rem 1rem;">
          <h5 style="font-size:0.82rem;text-transform:uppercase;letter-spacing:0.05em;color:#f87171;margin-bottom:0.4rem;display:flex;align-items:center;gap:0.4rem;">
            <span>&#9888;</span> High-Yield Exam Reminders & Common Pitfalls
          </h5>
          <ul style="margin:0;padding-left:1.2rem;display:flex;flex-direction:column;gap:0.35rem;">
            ${examTips.map(tip => `
              <li style="color:#fca5a5;font-size:0.85rem;line-height:1.45;">${tip}</li>
            `).join('')}
          </ul>
        </div>
      `;
    }

    // Active recall for QA or flashcards
    if (style === 'qa' || style === 'flashcards') {
      sectionsHtml += `
        <div style="margin-top:1rem;background:rgba(99, 102, 241, 0.08);border:1px solid rgba(99, 102, 241, 0.25);border-radius:var(--radius-sm, 6px);padding:0.75rem 1rem;">
          <h5 style="font-size:0.82rem;text-transform:uppercase;letter-spacing:0.05em;color:#a5b4fc;margin-bottom:0.4rem;">
            <span>&#9733;</span> Active Recall Concept Check
          </h5>
          <p style="color:var(--text-muted);font-size:0.85rem;margin:0 0 0.5rem 0;">Q: How does temperature change affect an endothermic equilibrium reaction?</p>
          <details style="font-size:0.82rem;color:var(--color-emerald);cursor:pointer;">
            <summary>Reveal Concept Answer</summary>
            <p style="color:var(--text-bright);margin-top:0.4rem;padding-left:0.5rem;border-left:2px solid var(--color-emerald);">Increasing temperature supplies heat energy, shifting endothermic equilibrium towards products (forward reaction).</p>
          </details>
        </div>
      `;
    }

    return sectionsHtml;
  }

  // Simple Markdown to HTML converter
  function formatMarkdownToHtml(mdText) {
    if (!mdText) return "";
    let html = mdText
      .replace(/^### (.*$)/gim, '<h5 style="font-size:0.95rem;color:var(--color-cyan, #06b6d4);margin:0.8rem 0 0.3rem 0;">$1</h5>')
      .replace(/^## (.*$)/gim, '<h4 style="font-size:1.05rem;color:var(--color-emerald);margin:1rem 0 0.4rem 0;">$1</h4>')
      .replace(/^# (.*$)/gim, '<h3 style="font-size:1.2rem;color:var(--text-bright);margin:0 0 0.5rem 0;">$1</h3>')
      .replace(/\*\*(.*?)\*\*/gim, '<strong style="color:var(--text-bright);">$1</strong>')
      .replace(/\*(.*?)\*/gim, '<em>$1</em>')
      .replace(/^\s*-\s+(.*$)/gim, '<li style="color:var(--text-muted);margin-bottom:0.3rem;">$1</li>')
      .replace(/^\s*\d+\.\s+(.*$)/gim, '<li style="color:var(--text-muted);margin-bottom:0.3rem;">$1</li>');

    return html.split(/\n\s*\n/).map(p => {
      p = p.trim();
      if (!p) return "";
      if (p.startsWith("<h") || p.startsWith("<ul") || p.startsWith("<div") || p.startsWith("<p") || p.startsWith("<li")) {
        return p;
      }
      return '<p style="color:var(--text-main);line-height:1.6;font-size:0.9rem;margin-bottom:0.75rem;">' + p + '</p>';
    }).join("\n");
  }

  // Render notes output into UI
  function renderGeneratedNotes(title, htmlContent, level, style, rawMd) {
    const container = document.getElementById("notesOutputContent");
    if (!container) return;

    container.innerHTML = htmlContent;

    // Save active markdown representation for export & copy
    if (rawMd) {
      window._currentNotesMarkdown = rawMd;
    } else {
      const cleanText = container.innerText || container.textContent || "";
      window._currentNotesMarkdown = "# " + title + "\n" +
        "Target Level: " + level + " | Style: " + style + "\n" +
        "Generated by ChemAI Scientific Platform\n\n" +
        cleanText;
    }
  }

  // Primary API/Engine Entry Point
  window.generateAINotes = async function() {
    const topicSelect = document.getElementById("notesTopicSelect");
    const styleSelect = document.getElementById("notesStyleSelect");
    const levelSelect = document.getElementById("notesLevelSelect");
    const outputDiv = document.getElementById("notesOutputContent");

    if (!outputDiv) {
      console.warn("ChemAI Notes: notesOutputContent container not found in DOM");
      return;
    }

    const selectedKey = (topicSelect && topicSelect.value ? topicSelect.value.trim().toLowerCase() : "physical");
    const topicName = (topicSelect && topicSelect.options && topicSelect.selectedIndex >= 0)
      ? topicSelect.options[topicSelect.selectedIndex].text
      : "Chemistry Study Sheet";
    const selectedStyle = (styleSelect && styleSelect.value) ? styleSelect.value : "summary";
    const selectedLevel = (levelSelect && levelSelect.value) ? levelSelect.value : "AP Chemistry";

    // Show high-tech loading state
    outputDiv.innerHTML = `
      <div style="text-align:center;padding:2rem 1rem;">
        <div style="display:inline-block;width:32px;height:32px;border:3px solid rgba(16,185,129,0.2);border-top:3px solid var(--color-emerald);border-radius:50%;animation:spin 0.8s linear infinite;"></div>
        <p style="margin-top:0.75rem;font-size:0.9rem;color:var(--color-emerald);font-weight:600;">Generating Scientific Notes...</p>
        <p style="font-size:0.8rem;color:var(--text-dim);margin:0;">Synthesizing ${topicName} for ${selectedLevel} (${selectedStyle})</p>
      </div>
      <style>@keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }</style>
    `;

    // Attempt live server API first with a responsive timeout
    let fetchedNotes = null;
    try {
      const controller = new AbortController();
      const timeoutId = setTimeout(() => controller.abort(), 3500);

      const res = await fetch("/api/generate-notes", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          topic: topicName,
          branch: selectedKey,
          style: selectedStyle,
          level: selectedLevel
        }),
        signal: controller.signal
      });
      clearTimeout(timeoutId);

      if (res.ok) {
        const json = await res.json();
        if (json && json.notes) {
          fetchedNotes = json.notes;
        }
      }
    } catch (err) {
      // Offline fallback or static GitHub Pages
    }

    if (fetchedNotes) {
      const renderedHtml = `
        <div style="border-bottom:1px solid var(--border-subtle);padding-bottom:0.75rem;margin-bottom:1rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.5rem;">
          <div>
            <h4 style="font-size:1.15rem;font-weight:700;color:var(--text-bright);margin:0;">${topicName}</h4>
            <span style="font-size:0.75rem;color:var(--color-emerald);font-weight:600;text-transform:uppercase;">Level: ${selectedLevel}</span>
          </div>
          <span class="chip chip-cobalt" style="font-size:0.75rem;padding:0.25rem 0.6rem;">AI Synthesized</span>
        </div>
        ${formatMarkdownToHtml(fetchedNotes)}
      `;
      renderGeneratedNotes(topicName, renderedHtml, selectedLevel, selectedStyle, fetchedNotes);
      return;
    }

    // Instant local client-side scientific knowledge engine fallback
    const preset = PRESET_NOTES[selectedKey] || PRESET_NOTES.physical;
    const notesHtml = buildStyledNotesContent(preset, selectedStyle, selectedLevel);
    renderGeneratedNotes(preset.title || topicName, notesHtml, selectedLevel, selectedStyle);
  };

  // Clipboard copy function
  window.copyNotesToClipboard = function() {
    const textToCopy = window._currentNotesMarkdown || (document.getElementById("notesOutputContent") ? document.getElementById("notesOutputContent").innerText : "");
    if (!textToCopy) {
      alert("Please generate notes first before copying.");
      return;
    }

    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(textToCopy).then(() => {
        showToast("Chemistry notes copied to clipboard!");
      }).catch(() => {
        fallbackCopyText(textToCopy);
      });
    } else {
      fallbackCopyText(textToCopy);
    }
  };

  // Download Markdown file function
  window.downloadNotesMarkdown = function() {
    const textToSave = window._currentNotesMarkdown || (document.getElementById("notesOutputContent") ? document.getElementById("notesOutputContent").innerText : "");
    if (!textToSave) {
      alert("Please generate notes first before downloading.");
      return;
    }

    const topicSelect = document.getElementById("notesTopicSelect");
    const rawName = (topicSelect && topicSelect.value) ? topicSelect.value : "Chemistry";
    const filename = `ChemAI_Notes_${rawName}.md`;

    const blob = new Blob([textToSave], { type: "text/markdown;charset=utf-8" });
    const url = URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showToast("Downloaded " + filename);
  };

  // Print function
  window.printNotes = function() {
    const outputDiv = document.getElementById("notesOutputContent");
    if (!outputDiv || !outputDiv.innerText.trim()) {
      alert("Please generate notes first before printing.");
      return;
    }

    const printWindow = window.open("", "_blank");
    if (!printWindow) {
      window.print();
      return;
    }

    printWindow.document.write(`
      <!DOCTYPE html>
      <html>
      <head>
        <title>ChemAI Chemistry Revision Sheet</title>
        <style>
          body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
            color: #111;
            padding: 2rem;
            line-height: 1.6;
          }
          h3, h4, h5 { color: #0f172a; margin-top: 1.2rem; }
          ul { padding-left: 1.5rem; }
          .chip { display: inline-block; padding: 2px 8px; border: 1px solid #ccc; border-radius: 4px; font-size: 12px; }
          @media print {
            body { padding: 0; }
          }
        </style>
      </head>
      <body>
        <div style="border-bottom: 2px solid #0f172a; padding-bottom: 0.5rem; margin-bottom: 1.5rem;">
          <h2 style="margin: 0;">ChemAI Laboratory — Revision Study Sheet</h2>
          <small>Verified Academic Chemistry Reference</small>
        </div>
        ${outputDiv.innerHTML}
      </body>
      </html>
    `);
    printWindow.document.close();
    printWindow.focus();
    setTimeout(() => {
      printWindow.print();
      printWindow.close();
    }, 400);
  };

  // Helper toast notification
  function showToast(msg) {
    let toast = document.getElementById("chemaiToast");
    if (!toast) {
      toast = document.createElement("div");
      toast.id = "chemaiToast";
      toast.style.position = "fixed";
      toast.style.bottom = "24px";
      toast.style.right = "24px";
      toast.style.background = "#10b981";
      toast.style.color = "#022c22";
      toast.style.padding = "10px 18px";
      toast.style.borderRadius = "8px";
      toast.style.fontWeight = "600";
      toast.style.fontSize = "0.88rem";
      toast.style.boxShadow = "0 8px 24px rgba(0,0,0,0.3)";
      toast.style.zIndex = "9999";
      toast.style.transition = "all 0.3s ease";
      document.body.appendChild(toast);
    }
    toast.textContent = msg;
    toast.style.opacity = "1";
    toast.style.transform = "translateY(0)";
    setTimeout(() => {
      toast.style.opacity = "0";
      toast.style.transform = "translateY(10px)";
    }, 3000);
  }

  function fallbackCopyText(text) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";
    textArea.style.left = "-9999px";
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
      document.execCommand("copy");
      showToast("Chemistry notes copied to clipboard!");
    } catch (err) {
      alert("Unable to copy to clipboard automatically.");
    }
    document.body.removeChild(textArea);
  }

})();
