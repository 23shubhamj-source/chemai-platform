/* ==========================================================================
   ChemAI Platform - Master Application Controller (Part 1)
   Coordinates navigation, modals, search palette, and typing hero
   ========================================================================== */

(function initApp() {
  // 1. Hero Dynamic Typing Animation
  const typingPhrases = [
    "balance complex chemical equations.",
    "simulate acid-base titration curves.",
    "calculate molar masses & compositions.",
    "render interactive 3D molecular structures.",
    "solve limiting reagent stoichiometry.",
    "elucidate infrared & NMR spectra.",
    "explain reaction mechanisms step-by-step."
  ];

  let phraseIdx = 0;
  let charIdx = 0;
  let isDeleting = false;
  const typeSpeed = 70;
  const deleteSpeed = 35;
  const pauseEnd = 1800;

  function typeHeroLoop() {
    const el = document.getElementById("heroTypingText");
    if (!el) return;

    const currentPhrase = typingPhrases[phraseIdx];

    if (!isDeleting) {
      el.textContent = currentPhrase.substring(0, charIdx + 1);
      charIdx++;
      if (charIdx === currentPhrase.length) {
        isDeleting = true;
        setTimeout(typeHeroLoop, pauseEnd);
        return;
      }
      setTimeout(typeHeroLoop, typeSpeed);
    } else {
      el.textContent = currentPhrase.substring(0, charIdx - 1);
      charIdx--;
      if (charIdx === 0) {
        isDeleting = false;
        phraseIdx = (phraseIdx + 1) % typingPhrases.length;
        setTimeout(typeHeroLoop, 400);
        return;
      }
      setTimeout(typeHeroLoop, deleteSpeed);
    }
  }

  // 2. Global Search Command Palette (Ctrl+K)
  const SEARCH_INDEX = [
    { title: "Chemical Equation Balancer", cat: "Student Essentials", action: () => openCalculatorModal("balancer"), desc: "Balance redox and combustion equations with linear algebra." },
    { title: "Molar Mass Calculator", cat: "Student Essentials", action: () => openCalculatorModal("molarmass"), desc: "Exact molecular weights and elemental percentage composition." },
    { title: "Stoichiometry & Limiting Reagent", cat: "Student Essentials", action: () => openCalculatorModal("stoichiometry"), desc: "Theoretical product yield and remaining excess." },
    { title: "pH & pOH Calculator", cat: "Student Essentials", action: () => openCalculatorModal("ph"), desc: "Interconvert pH, pOH, [H+], and [OH-] with acidity bar." },
    { title: "Solution Dilution (M1V1 = M2V2)", cat: "Student Essentials", action: () => openCalculatorModal("dilution"), desc: "Calculate stock concentration and working volumes." },
    { title: "Ideal Gas Law (PV = nRT)", cat: "Student Essentials", action: () => openCalculatorModal("gas"), desc: "Solve for Pressure, Volume, Moles, or Temperature." },
    { title: "Thermodynamics (ΔG = ΔH - TΔS)", cat: "Student Essentials", action: () => openCalculatorModal("thermo"), desc: "Gibbs free energy, reaction spontaneity, and equilibrium constant." },
    { title: "Percentage Yield Calculator", cat: "Student Essentials", action: () => openCalculatorModal("yield"), desc: "Compare actual recovered yield against theoretical maximum." },
    { title: "Electron Configuration & Aufbau", cat: "Student Essentials", action: () => openCalculatorModal("config"), desc: "Orbital energy filling, noble gas shorthand, valence electrons." },
    { title: "Acid-Base Titration Lab", cat: "Virtual Lab", action: () => { window.location.hash = "#virtual-lab"; window.switchLabExperiment?.("titration"); }, desc: "Burette drip simulation with real-time pH titration curve." },
    { title: "Universal pH Indicator Lab", cat: "Virtual Lab", action: () => { window.location.hash = "#virtual-lab"; window.switchLabExperiment?.("indicator"); }, desc: "Test common household chemicals on 0-14 pH scale." },
    { title: "Precipitation Reactions Lab", cat: "Virtual Lab", action: () => { window.location.hash = "#virtual-lab"; window.switchLabExperiment?.("precipitation"); }, desc: "Mixing ionic salts with solubility rules breakdown." },
    { title: "Interactive Periodic Table", cat: "Molecular Tools", action: () => { window.location.hash = "#periodic-table"; }, desc: "Explore all 118 IUPAC elements with physical constants." },
    { title: "3D Molecule Viewer", cat: "Molecular Tools", action: () => { window.location.hash = "#molecule-viewer"; }, desc: "WebGL 3D Ball-and-Stick and Space-Filling molecular viewer." },
    { title: "Chemistry Quiz Generator", cat: "Study Tools", action: () => { window.location.hash = "#study-tools"; }, desc: "Custom multiple-choice chemistry quizzes with explanations." },
    { title: "AI Notes Generator", cat: "Study Tools", action: () => { window.location.hash = "#study-tools"; }, desc: "High-yield structured study sheets and revision summaries." }
  ];

  window.openSearchPalette = function() {
    const modal = document.getElementById("searchModalBackdrop");
    const input = document.getElementById("searchPaletteInput");
    if (modal) {
      modal.classList.add("open");
      if (input) {
        input.value = "";
        input.focus();
        renderSearchResults("");
      }
    }
  };

  window.closeSearchPalette = function() {
    const modal = document.getElementById("searchModalBackdrop");
    if (modal) modal.classList.remove("open");
  };

  function renderSearchResults(query) {
    const container = document.getElementById("searchResultsList");
    if (!container) return;
    container.innerHTML = "";

    const filtered = SEARCH_INDEX.filter((item) => {
      if (!query) return true;
      const q = query.toLowerCase();
      return item.title.toLowerCase().includes(q) || item.cat.toLowerCase().includes(q) || item.desc.toLowerCase().includes(q);
    });

    if (filtered.length === 0) {
      container.innerHTML = `<li style="padding: 1.5rem; text-align: center; color: var(--text-muted);">No chemistry tools match "${query}". Try searching "pH", "molar", or "titration".</li>`;
      return;
    }

    filtered.forEach((item) => {
      const li = document.createElement("li");
      li.className = "search-result-item";
      li.innerHTML = `
        <div class="search-item-left">
          <span class="chip chip-emerald" style="font-size:0.7rem;">${item.cat}</span>
          <div>
            <div class="search-item-title">${item.title}</div>
            <div class="search-item-desc">${item.desc}</div>
          </div>
        </div>
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M5 12h14M12 5l7 7-7 7"/></svg>
      `;
      li.addEventListener("click", () => {
        window.closeSearchPalette();
        item.action();
      });
      container.appendChild(li);
    });
  }

  // 3. Calculator Modal Dispatcher & Form Builder
  window.openCalculatorModal = function(toolKey) {
    const modal = document.getElementById("calculatorModalBackdrop");
    const titleEl = document.getElementById("calcModalTitle");
    const bodyEl = document.getElementById("calcModalBody");
    if (!modal || !titleEl || !bodyEl) return;

    modal.classList.add("open");

    if (toolKey === "balancer") {
      titleEl.innerHTML = `Chemical Equation Balancer`;
      bodyEl.innerHTML = `
        <p style="color:var(--text-muted);font-size:0.9rem;margin-bottom:1.25rem;">Enter unbalanced chemical equation using formula symbols and '->' or '=' (e.g. <code>C3H8 + O2 -> CO2 + H2O</code> or <code>Fe + O2 -> Fe2O3</code>).</p>
        <div class="calc-form-group">
          <label class="calc-label">Chemical Reaction</label>
          <div class="calc-input-wrapper">
            <input type="text" id="calcInputEq" class="calc-input" placeholder="e.g. C3H8 + O2 -> CO2 + H2O" value="C3H8 + O2 -> CO2 + H2O">
          </div>
        </div>
        <div class="calc-actions-row">
          <button class="btn btn-primary" onclick="runEquationBalancer()">Balance Equation</button>
          <button class="btn btn-ghost" onclick="document.getElementById('calcInputEq').value='Fe + O2 -> Fe2O3'">Sample: Rusting</button>
        </div>
        <div id="calcOutputArea"></div>
      `;
    } else if (toolKey === "molarmass") {
      titleEl.innerHTML = `Molar Mass & % Composition Calculator`;
      bodyEl.innerHTML = `
        <p style="color:var(--text-muted);font-size:0.9rem;margin-bottom:1.25rem;">Enter any chemical formula or hydrate (e.g. <code>CuSO4.5H2O</code>, <code>Ca(OH)2</code>, or <code>C12H22O11</code>).</p>
        <div class="calc-form-group">
          <label class="calc-label">Formula</label>
          <div class="calc-input-wrapper">
            <input type="text" id="calcInputMassFormula" class="calc-input" placeholder="e.g. CuSO4.5H2O" value="CuSO4.5H2O">
          </div>
        </div>
        <div class="calc-actions-row">
          <button class="btn btn-primary" onclick="runMolarMassCalc()">Compute Molar Mass</button>
          <button class="btn btn-ghost" onclick="document.getElementById('calcInputMassFormula').value='C6H12O6'">Glucose C₆H₁₂O₆</button>
        </div>
        <div id="calcOutputArea"></div>
      `;
    } else if (toolKey === "ph") {
      titleEl.innerHTML = `pH & pOH Calculator`;
      bodyEl.innerHTML = `
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
          <div class="calc-form-group">
            <label class="calc-label">Parameter Type</label>
            <div class="calc-input-wrapper">
              <select id="calcPHType" class="calc-input" style="cursor:pointer;">
                <option value="pH">pH value</option>
                <option value="pOH">pOH value</option>
                <option value="H">[H+] molarity</option>
                <option value="OH">[OH-] molarity</option>
              </select>
            </div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Value</label>
            <div class="calc-input-wrapper">
              <input type="number" step="any" id="calcPHVal" class="calc-input" placeholder="e.g. 3.0" value="3.0">
            </div>
          </div>
        </div>
        <div class="calc-actions-row">
          <button class="btn btn-primary" onclick="runPHCalc()">Calculate</button>
        </div>
        <div id="calcOutputArea"></div>
      `;
    } else if (toolKey === "dilution") {
      titleEl.innerHTML = `Solution Dilution (M₁V₁ = M₂V₂)`;
      bodyEl.innerHTML = `
        <p style="color:var(--text-muted);font-size:0.9rem;margin-bottom:1.25rem;">Fill in any 3 fields to solve for the remaining 4th.</p>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
          <div class="calc-form-group">
            <label class="calc-label">Initial Concentration M₁ (M)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="dilM1" class="calc-input" placeholder="e.g. 12.0" value="12.0"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Initial Volume V₁ (mL)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="dilV1" class="calc-input" placeholder="Leave empty to solve"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Final Concentration M₂ (M)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="dilM2" class="calc-input" placeholder="e.g. 1.0" value="1.0"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Final Volume V₂ (mL)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="dilV2" class="calc-input" placeholder="e.g. 500" value="500"></div>
          </div>
        </div>
        <div class="calc-actions-row">
          <button class="btn btn-primary" onclick="runDilutionCalc()">Solve Dilution</button>
        </div>
        <div id="calcOutputArea"></div>
      `;
    } else if (toolKey === "gas") {
      titleEl.innerHTML = `Ideal Gas Law (PV = nRT)`;
      bodyEl.innerHTML = `
        <p style="color:var(--text-muted);font-size:0.9rem;margin-bottom:1.25rem;">Enter any 3 variables to compute the 4th.</p>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
          <div class="calc-form-group">
            <label class="calc-label">Pressure P (atm)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="gasP" class="calc-input" placeholder="e.g. 1.0" value="1.0"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Volume V (L)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="gasV" class="calc-input" placeholder="Leave empty to solve"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Amount n (moles)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="gasN" class="calc-input" placeholder="e.g. 2.5" value="2.5"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Temperature T (K)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="gasT" class="calc-input" placeholder="e.g. 298.15" value="298.15"></div>
          </div>
        </div>
        <div class="calc-actions-row">
          <button class="btn btn-primary" onclick="runGasCalc()">Compute Gas State</button>
        </div>
        <div id="calcOutputArea"></div>
      `;
    } else if (toolKey === "thermo") {
      titleEl.innerHTML = `Thermodynamics (ΔG = ΔH - TΔS)`;
      bodyEl.innerHTML = `
        <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:1rem;">
          <div class="calc-form-group">
            <label class="calc-label">ΔH (kJ/mol)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="thermoH" class="calc-input" placeholder="e.g. -92.2" value="-92.2"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">ΔS (J/(mol·K))</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="thermoS" class="calc-input" placeholder="e.g. -198.7" value="-198.7"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Temperature (K)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="thermoT" class="calc-input" placeholder="e.g. 298" value="298"></div>
          </div>
        </div>
        <div class="calc-actions-row">
          <button class="btn btn-primary" onclick="runThermoCalc()">Calculate Free Energy</button>
        </div>
        <div id="calcOutputArea"></div>
      `;
    } else if (toolKey === "stoichiometry") {
      titleEl.innerHTML = `Stoichiometry & Limiting Reagent`;
      bodyEl.innerHTML = `
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
          <div class="calc-form-group">
            <label class="calc-label">Reactant A Formula</label>
            <div class="calc-input-wrapper"><input type="text" id="stochRA" class="calc-input" value="H2"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Mass Reactant A (g)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="stochMA" class="calc-input" value="4.0"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Reactant B Formula</label>
            <div class="calc-input-wrapper"><input type="text" id="stochRB" class="calc-input" value="O2"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Mass Reactant B (g)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="stochMB" class="calc-input" value="16.0"></div>
          </div>
        </div>
        <div class="calc-form-group">
          <label class="calc-label">Target Product Formula</label>
          <div class="calc-input-wrapper"><input type="text" id="stochP" class="calc-input" value="H2O"></div>
        </div>
        <div class="calc-actions-row">
          <button class="btn btn-primary" onclick="runStoichiometryCalc()">Compute Limiting Reagent</button>
        </div>
        <div id="calcOutputArea"></div>
      `;
    } else if (toolKey === "yield") {
      titleEl.innerHTML = `Percentage Yield Calculator`;
      bodyEl.innerHTML = `
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:1rem;">
          <div class="calc-form-group">
            <label class="calc-label">Actual Yield (g)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="yieldActual" class="calc-input" placeholder="e.g. 14.8" value="14.8"></div>
          </div>
          <div class="calc-form-group">
            <label class="calc-label">Theoretical Yield (g)</label>
            <div class="calc-input-wrapper"><input type="number" step="any" id="yieldTheo" class="calc-input" placeholder="e.g. 18.0" value="18.0"></div>
          </div>
        </div>
        <div class="calc-actions-row">
          <button class="btn btn-primary" onclick="runYieldCalc()">Compute Yield</button>
        </div>
        <div id="calcOutputArea"></div>
      `;
    } else if (toolKey === "config") {
      titleEl.innerHTML = `Electron Configuration & Aufbau Tool`;
      bodyEl.innerHTML = `
        <div class="calc-form-group">
          <label class="calc-label">Element Symbol or Atomic Number</label>
          <div class="calc-input-wrapper"><input type="text" id="configInputEl" class="calc-input" placeholder="e.g. Fe, Au, or 26" value="Fe"></div>
        </div>
        <div class="calc-actions-row">
          <button class="btn btn-primary" onclick="runElectronConfigCalc()">Generate Configuration</button>
        </div>
        <div id="calcOutputArea"></div>
      `;
    }
  };

  window.closeCalculatorModal = function() {
    const modal = document.getElementById("calculatorModalBackdrop");
    if (modal) modal.classList.remove("open");
  };

  // Execution Handlers for Calculators
  window.runEquationBalancer = function() {
    const eq = document.getElementById("calcInputEq")?.value;
    const res = window.balanceEquation(eq);
    const out = document.getElementById("calcOutputArea");
    if (!out) return;

    if (res.success) {
      out.innerHTML = `
        <div class="calc-result-box">
          <div class="calc-result-header">
            <span class="chip chip-emerald">Balanced Successfully</span>
            <span style="font-family:var(--font-mono);font-size:0.8rem;color:var(--text-muted);">${res.derivation}</span>
          </div>
          <div class="calc-result-value" style="font-size:1.4rem;">${res.balanced}</div>
          <div class="calc-formula-display">Reactants: ${res.reactants.join(", ")} | Products: ${res.products.join(", ")}</div>
        </div>
      `;
    } else {
      out.innerHTML = `<div class="calc-result-box" style="border-color:var(--color-rose);"><span class="text-rose">Error:</span> ${res.error}</div>`;
    }
  };

  window.runMolarMassCalc = function() {
    const formula = document.getElementById("calcInputMassFormula")?.value;
    const res = window.calcMolarMass(formula);
    const out = document.getElementById("calcOutputArea");
    if (!out) return;

    if (res.success) {
      let compBars = "";
      res.elements.forEach((item) => {
        compBars += `
          <div class="composition-bar-row">
            <div class="comp-info">
              <span><strong>${item.element}</strong> (${item.count} × ${item.weight} g/mol)</span>
              <span><strong>${item.percentage}%</strong></span>
            </div>
            <div class="comp-bar-track">
              <div class="comp-bar-fill" style="width: ${item.percentage}%;"></div>
            </div>
          </div>
        `;
      });

      out.innerHTML = `
        <div class="calc-result-box">
          <div class="calc-result-header">
            <span class="chip chip-emerald">Formula: ${res.formula}</span>
            <span style="color:var(--text-muted);font-size:0.85rem;">Standard IUPAC Weights</span>
          </div>
          <div class="calc-result-value">${res.molarMass} <span style="font-size:1rem;color:var(--text-muted);">g/mol</span></div>
          <h5 style="margin: 1rem 0 0.5rem 0; color:var(--text-highlight);">Elemental Mass Composition:</h5>
          ${compBars}
        </div>
      `;
    } else {
      out.innerHTML = `<div class="calc-result-box" style="border-color:var(--color-rose);"><span class="text-rose">Error:</span> ${res.error}</div>`;
    }
  };

  window.runPHCalc = function() {
    const type = document.getElementById("calcPHType")?.value;
    const value = document.getElementById("calcPHVal")?.value;
    const res = window.calcPH({ type, value });
    const out = document.getElementById("calcOutputArea");
    if (!out) return;

    if (res.success) {
      out.innerHTML = `
        <div class="calc-result-box">
          <div class="calc-result-header">
            <span class="chip chip-emerald">${res.classification}</span>
            <span style="color:var(--text-muted);font-size:0.85rem;">T = 25°C (Kw = 1.0 × 10⁻¹⁴)</span>
          </div>
          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin:1rem 0;">
            <div>
              <div style="font-size:0.85rem;color:var(--text-muted);">pH:</div>
              <div class="calc-result-value" style="color:${res.color};">${res.pH}</div>
            </div>
            <div>
              <div style="font-size:0.85rem;color:var(--text-muted);">pOH:</div>
              <div class="calc-result-value">${res.pOH}</div>
            </div>
            <div>
              <div style="font-size:0.85rem;color:var(--text-muted);">[H⁺] Concentration:</div>
              <div style="font-family:var(--font-mono);font-size:1.1rem;color:var(--color-emerald);">${res.H} M</div>
            </div>
            <div>
              <div style="font-size:0.85rem;color:var(--text-muted);">[OH⁻] Concentration:</div>
              <div style="font-family:var(--font-mono);font-size:1.1rem;color:var(--color-cobalt);">${res.OH} M</div>
            </div>
          </div>
        </div>
      `;
    } else {
      out.innerHTML = `<div class="calc-result-box" style="border-color:var(--color-rose);"><span class="text-rose">Error:</span> ${res.error}</div>`;
    }
  };

  window.runDilutionCalc = function() {
    const m1 = document.getElementById("dilM1")?.value;
    const v1 = document.getElementById("dilV1")?.value;
    const m2 = document.getElementById("dilM2")?.value;
    const v2 = document.getElementById("dilV2")?.value;
    const res = window.calcDilution({ m1, v1, m2, v2 });
    const out = document.getElementById("calcOutputArea");
    if (!out) return;

    if (res.success) {
      out.innerHTML = `
        <div class="calc-result-box">
          <div class="calc-result-header">
            <span class="chip chip-emerald">Solved: ${res.target}</span>
          </div>
          <div class="calc-result-value">${res.result}</div>
          <div class="calc-formula-display">${res.explanation}</div>
        </div>
      `;
    } else {
      out.innerHTML = `<div class="calc-result-box" style="border-color:var(--color-rose);"><span class="text-rose">Error:</span> ${res.error}</div>`;
    }
  };

  window.runGasCalc = function() {
    const p = document.getElementById("gasP")?.value;
    const v = document.getElementById("gasV")?.value;
    const n = document.getElementById("gasN")?.value;
    const t = document.getElementById("gasT")?.value;
    const res = window.calcIdealGas({ p, v, n, t });
    const out = document.getElementById("calcOutputArea");
    if (!out) return;

    if (res.success) {
      out.innerHTML = `
        <div class="calc-result-box">
          <div class="calc-result-header">
            <span class="chip chip-emerald">Solved: ${res.target}</span>
          </div>
          <div class="calc-result-value">${res.result}</div>
          <div class="calc-formula-display">${res.formula}</div>
        </div>
      `;
    } else {
      out.innerHTML = `<div class="calc-result-box" style="border-color:var(--color-rose);"><span class="text-rose">Error:</span> ${res.error}</div>`;
    }
  };

  window.runThermoCalc = function() {
    const dH = document.getElementById("thermoH")?.value;
    const dS = document.getElementById("thermoS")?.value;
    const tempK = document.getElementById("thermoT")?.value;
    const res = window.calcThermodynamics({ dH, dS, tempK });
    const out = document.getElementById("calcOutputArea");
    if (!out) return;

    if (res.success) {
      out.innerHTML = `
        <div class="calc-result-box">
          <div class="calc-result-header">
            <span class="chip ${res.spontaneous ? 'chip-emerald' : 'chip-amber'}">${res.statusText}</span>
            <span style="font-family:var(--font-mono);font-size:0.85rem;color:var(--text-muted);">Eq Const K: ${res.K}</span>
          </div>
          <div class="calc-result-value">${res.dG}</div>
          <div class="calc-formula-display">Formula: ${res.formula} | Equilibrium Inversion Temp: ${res.crossoverTemp}</div>
        </div>
      `;
    } else {
      out.innerHTML = `<div class="calc-result-box" style="border-color:var(--color-rose);"><span class="text-rose">Error:</span> ${res.error}</div>`;
    }
  };

  window.runStoichiometryCalc = function() {
    const reactantA = document.getElementById("stochRA")?.value;
    const massA = document.getElementById("stochMA")?.value;
    const reactantB = document.getElementById("stochRB")?.value;
    const massB = document.getElementById("stochMB")?.value;
    const product = document.getElementById("stochP")?.value;

    const res = window.calcStoichiometry({ reactantA, massA, reactantB, massB, product });
    const out = document.getElementById("calcOutputArea");
    if (!out) return;

    if (res.success) {
      out.innerHTML = `
        <div class="calc-result-box">
          <div class="calc-result-header">
            <span class="chip chip-emerald">Limiting Reagent: ${res.limitingReagent}</span>
            <span style="font-size:0.85rem;color:var(--text-muted);">Excess Remaining: ${res.excessRemaining}</span>
          </div>
          <div class="calc-result-value">Theoretical Yield: ${res.theoreticalYield}</div>
          <div class="calc-formula-display">Moles ${reactantA}: ${res.molesA} | Moles ${reactantB}: ${res.molesB}</div>
        </div>
      `;
    } else {
      out.innerHTML = `<div class="calc-result-box" style="border-color:var(--color-rose);"><span class="text-rose">Error:</span> ${res.error}</div>`;
    }
  };

  window.runYieldCalc = function() {
    const actual = document.getElementById("yieldActual")?.value;
    const theoretical = document.getElementById("yieldTheo")?.value;
    const res = window.calcPercentageYield({ actual, theoretical });
    const out = document.getElementById("calcOutputArea");
    if (!out) return;

    if (res.success) {
      out.innerHTML = `
        <div class="calc-result-box">
          <div class="calc-result-header">
            <span class="chip chip-emerald">${res.evaluation}</span>
          </div>
          <div class="calc-result-value">${res.yield}</div>
          <div class="calc-formula-display">${res.formula}</div>
        </div>
      `;
    } else {
      out.innerHTML = `<div class="calc-result-box" style="border-color:var(--color-rose);"><span class="text-rose">Error:</span> ${res.error}</div>`;
    }
  };

  window.runElectronConfigCalc = function() {
    const input = document.getElementById("configInputEl")?.value;
    const res = window.calcElectronConfig(input);
    const out = document.getElementById("calcOutputArea");
    if (!out) return;

    if (res.success) {
      out.innerHTML = `
        <div class="calc-result-box">
          <div class="calc-result-header">
            <span class="chip chip-emerald">${res.element} (${res.symbol}) - Z = ${res.atomicNumber}</span>
            <span style="color:var(--text-muted);font-size:0.85rem;">${res.block}</span>
          </div>
          <div class="calc-result-value" style="font-size:1.4rem;">${res.configuration}</div>
          <div class="calc-formula-display">Valence Electrons: <strong>${res.valenceElectrons}</strong> · Aufbau & Hund's Rule Orbital Sequence</div>
        </div>
      `;
    } else {
      out.innerHTML = `<div class="calc-result-box" style="border-color:var(--color-rose);"><span class="text-rose">Error:</span> ${res.error}</div>`;
    }
  };

  // 4. Tools Directory Tab Filtering & Real-time Search
  function setupToolsFilter() {
    const tabs = document.querySelectorAll(".category-tab");
    const cards = document.querySelectorAll(".tool-card");
    const searchInput = document.getElementById("toolsSearchInput");

    let activeCat = "all";
    let searchVal = "";

    function filterCards() {
      cards.forEach((card) => {
        const cat = card.getAttribute("data-category");
        const name = card.querySelector("h3")?.innerText.toLowerCase() || "";
        const desc = card.querySelector("p")?.innerText.toLowerCase() || "";

        const matchCat = activeCat === "all" || cat === activeCat;
        const matchSearch = !searchVal || name.includes(searchVal) || desc.includes(searchVal);

        card.style.display = matchCat && matchSearch ? "flex" : "none";
      });
    }

    tabs.forEach((tab) => {
      tab.addEventListener("click", () => {
        tabs.forEach((t) => t.classList.remove("active"));
        tab.classList.add("active");
        activeCat = tab.getAttribute("data-category") || "all";
        filterCards();
      });
    });

    if (searchInput) {
      searchInput.addEventListener("input", (e) => {
        searchVal = e.target.value.trim().toLowerCase();
        filterCards();
      });
    }
  }

  // 5. Mobile Navigation Drawer Toggle
  window.toggleMobileMenu = function() {
    const navLinks = document.getElementById("siteNavLinks");
    if (navLinks) {
      navLinks.classList.toggle("mobile-open");
    }
  };

  // Keyboard shortcut listener for Ctrl+K
  window.addEventListener("keydown", (e) => {
    if ((e.ctrlKey || e.metaKey) && e.key.toLowerCase() === "k") {
      e.preventDefault();
      window.openSearchPalette();
    }
    if (e.key === "Escape") {
      window.closeSearchPalette();
      window.closeCalculatorModal();
    }
  });

  // Sticky Navbar scroll listener
  window.addEventListener("scroll", () => {
    const nav = document.querySelector(".site-nav");
    if (nav) {
      nav.classList.toggle("scrolled", window.scrollY > 30);
    }
  });

  window.addEventListener("DOMContentLoaded", () => {
    typeHeroLoop();
    setupToolsFilter();

    const searchInput = document.getElementById("searchPaletteInput");
    if (searchInput) {
      searchInput.addEventListener("input", (e) => {
        renderSearchResults(e.target.value.trim());
      });
    }

    const calcBackdrop = document.getElementById("calculatorModalBackdrop");
    if (calcBackdrop) {
      calcBackdrop.addEventListener("click", (e) => {
        if (e.target === calcBackdrop) window.closeCalculatorModal();
      });
    }

    const searchBackdrop = document.getElementById("searchModalBackdrop");
    if (searchBackdrop) {
      searchBackdrop.addEventListener("click", (e) => {
        if (e.target === searchBackdrop) window.closeSearchPalette();
      });
    }
  });
})();
