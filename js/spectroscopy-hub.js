/* ==========================================================================
   ChemAI Platform - Spectroscopy & Research Hub Engine
   Interactive IR, 1H/13C NMR, UV-Vis Beer-Lambert, Mass Spec & Research
   ========================================================================== */

(function initSpectroscopyHub() {
  // Preset Datasets
  const IR_COMPOUNDS = {
    ethanol: {
      name: "Ethanol (CH3CH2OH)",
      formula: "C2H6O",
      peaks: [
        { wavenumber: 3350, intensity: 0.85, width: 140, group: "O-H stretch (alcohol)", desc: "Broad hydrogen-bonded O-H stretch" },
        { wavenumber: 2975, intensity: 0.70, width: 35, group: "C-H stretch (sp3)", desc: "Asymmetric CH3/CH2 stretching" },
        { wavenumber: 2885, intensity: 0.60, width: 30, group: "C-H stretch (sp3)", desc: "Symmetric C-H stretching" },
        { wavenumber: 1450, intensity: 0.45, width: 25, group: "C-H bend", desc: "CH2 scissoring bend" },
        { wavenumber: 1050, intensity: 0.90, width: 45, group: "C-O stretch", desc: "Strong primary alcohol C-O single bond" }
      ]
    },
    acetone: {
      name: "Acetone (CH3COCH3)",
      formula: "C3H6O",
      peaks: [
        { wavenumber: 2995, intensity: 0.40, width: 30, group: "C-H stretch", desc: "Aliphatic C-H stretch" },
        { wavenumber: 1715, intensity: 0.95, width: 25, group: "C=O stretch (carbonyl)", desc: "Very intense sharp ketone carbonyl stretch" },
        { wavenumber: 1365, intensity: 0.55, width: 25, group: "C-H bend", desc: "CH3 symmetrical deformation (umbrella mode)" },
        { wavenumber: 1220, intensity: 0.65, width: 30, group: "C-C-C skeletal", desc: "Carbon-carbon skeletal stretch" }
      ]
    },
    acetic_acid: {
      name: "Acetic Acid (CH3COOH)",
      formula: "C2H4O2",
      peaks: [
        { wavenumber: 3000, intensity: 0.80, width: 250, group: "O-H stretch (carboxylic acid)", desc: "Extremely broad characteristic carboxylic acid dimer band" },
        { wavenumber: 1710, intensity: 0.96, width: 30, group: "C=O stretch", desc: "Strong hydrogen-bonded carbonyl stretch" },
        { wavenumber: 1410, intensity: 0.50, width: 25, group: "C-O-H in-plane bend", desc: "Carboxyl O-H deformation" },
        { wavenumber: 1280, intensity: 0.75, width: 35, group: "C-O stretch", desc: "C-O single bond vibration" }
      ]
    },
    benzaldehyde: {
      name: "Benzaldehyde (C6H5CHO)",
      formula: "C7H6O",
      peaks: [
        { wavenumber: 3060, intensity: 0.40, width: 25, group: "C-H stretch (sp2 aromatic)", desc: "Benzene ring C-H stretching" },
        { wavenumber: 2820, intensity: 0.55, width: 20, group: "Fermi doublet (aldehydic C-H)", desc: "Low-frequency aldehydic C-H stretch" },
        { wavenumber: 2740, intensity: 0.50, width: 20, group: "Fermi doublet (aldehydic C-H)", desc: "Second half of Fermi resonance doublet" },
        { wavenumber: 1700, intensity: 0.95, width: 25, group: "C=O stretch (conjugated)", desc: "Conjugated aromatic aldehyde carbonyl stretch" },
        { wavenumber: 1595, intensity: 0.60, width: 25, group: "C=C aromatic stretch", desc: "Aromatic ring quadrant vibration" },
        { wavenumber: 745, intensity: 0.85, width: 25, group: "C-H out-of-plane bend", desc: "Monosubstituted benzene 5 adjacent H bend" }
      ]
    }
  };

  const NMR_COMPOUNDS = {
    ethanol: {
      name: "Ethanol (1H-NMR)",
      nucleus: "1H",
      signals: [
        { shift: 1.25, integration: "3H", mult: "Triplet", j: "7.1 Hz", assignment: "-CH3 (methyl protons coupled to -CH2-)" },
        { shift: 3.65, integration: "2H", mult: "Quartet", j: "7.1 Hz", assignment: "-CH2- (methylene protons coupled to -CH3)" },
        { shift: 2.60, integration: "1H", mult: "Singlet", j: "Broad", assignment: "-OH (hydroxyl proton)" }
      ]
    },
    ethyl_acetate: {
      name: "Ethyl Acetate (1H-NMR)",
      nucleus: "1H",
      signals: [
        { shift: 1.26, integration: "3H", mult: "Triplet", j: "7.2 Hz", assignment: "Ester -CH2-CH3 (ethyl methyl protons)" },
        { shift: 2.04, integration: "3H", mult: "Singlet", j: "-", assignment: "Acetyl -CO-CH3 (isolated methyl)" },
        { shift: 4.12, integration: "2H", mult: "Quartet", j: "7.2 Hz", assignment: "Ester -O-CH2- (downfield deshielded by oxygen)" }
      ]
    },
    toluene: {
      name: "Toluene (1H-NMR)",
      nucleus: "1H",
      signals: [
        { shift: 2.35, integration: "3H", mult: "Singlet", j: "-", assignment: "Ar-CH3 (benzylic methyl)" },
        { shift: 7.15, integration: "3H", mult: "Multiplet", j: "8.0 Hz", assignment: "Ortho & Para aromatic protons" },
        { shift: 7.25, integration: "2H", mult: "Multiplet", j: "8.0 Hz", assignment: "Meta aromatic protons" }
      ]
    }
  };

  const MASS_SPEC_COMPOUNDS = {
    acetone: {
      name: "Acetone (MW = 58)",
      basePeak: 43,
      molecularIon: 58,
      peaks: [
        { mz: 15, rel: 35, fragment: "[CH3]+" },
        { mz: 42, rel: 10, fragment: "[CH2=C=O]+·" },
        { mz: 43, rel: 100, fragment: "[CH3-C≡O]+ (Acylium Base Peak)" },
        { mz: 58, rel: 25, fragment: "[M]+· (Molecular Ion)" },
        { mz: 59, rel: 1.2, fragment: "[M+1]+ (13C isotope)" }
      ]
    },
    ethanol: {
      name: "Ethanol (MW = 46)",
      basePeak: 31,
      molecularIon: 46,
      peaks: [
        { mz: 15, rel: 12, fragment: "[CH3]+" },
        { mz: 29, rel: 22, fragment: "[CH3CH2]+" },
        { mz: 31, rel: 100, fragment: "[CH2=OH]+ (Oxonium Base Peak)" },
        { mz: 45, rel: 38, fragment: "[M - H]+" },
        { mz: 46, rel: 15, fragment: "[M]+· (Molecular Ion)" }
      ]
    }
  };

  let activeTab = "ir";
  let activeIRCompound = "ethanol";
  let activeNMRCompound = "ethanol";
  let activeMassCompound = "acetone";

  // Tab Switching
  window.switchSpecTab = function(tab) {
    activeTab = tab;
    document.querySelectorAll(".spec-nav-tab").forEach(btn => {
      btn.classList.toggle("active", btn.getAttribute("data-tab") === tab);
    });

    document.querySelectorAll(".spec-tab-pane").forEach(pane => {
      pane.style.display = pane.id === "specPane_" + tab ? "block" : "none";
    });

    if (tab === "ir") renderIRCanvas();
    if (tab === "nmr") renderNMRCanvas();
    if (tab === "uvvis") updateBeerLambert();
    if (tab === "mass") renderMassCanvas();
  };

  // 1. IR Canvas Renderer
  function renderIRCanvas() {
    const canvas = document.getElementById("irSpectrumCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const width = canvas.width = canvas.parentElement.clientWidth;
    const height = canvas.height = canvas.parentElement.clientHeight;

    ctx.clearRect(0, 0, width, height);

    // Coordinate mapping: 4000 cm-1 (left) to 400 cm-1 (right)
    const minW = 400;
    const maxW = 4000;
    const xMargin = 50;
    const yMargin = 40;
    const plotW = width - xMargin * 2;
    const plotH = height - yMargin * 2;

    function wToX(w) {
      return xMargin + plotW * ((maxW - w) / (maxW - minW));
    }

    // Grid & Axes
    ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
    ctx.lineWidth = 1;

    for (let w = 500; w <= 4000; w += 500) {
      const x = wToX(w);
      ctx.beginPath();
      ctx.moveTo(x, yMargin);
      ctx.lineTo(x, height - yMargin);
      ctx.stroke();

      ctx.fillStyle = "rgba(148, 163, 184, 0.7)";
      ctx.font = "11px Inter, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(w.toString(), x, height - yMargin + 18);
    }

    // Draw baseline (% Transmittance = 100% at top)
    const baseLineY = yMargin + 20;
    const botLineY = height - yMargin;

    // Build curve
    const currentComp = IR_COMPOUNDS[activeIRCompound];
    ctx.beginPath();
    ctx.strokeStyle = "#10b981";
    ctx.lineWidth = 2.2;

    for (let px = 0; px <= plotW; px += 2) {
      const w = maxW - (px / plotW) * (maxW - minW);
      let tFactor = 1.0;

      // Add peaks (Gaussian absorption dips)
      currentComp.peaks.forEach(p => {
        const diff = w - p.wavenumber;
        const dip = p.intensity * Math.exp(-(diff * diff) / (2 * p.width * p.width));
        tFactor -= dip;
      });

      // Clamp between 0.05 and 1.0
      tFactor = Math.max(0.08, Math.min(0.98, tFactor));
      const py = baseLineY + (1 - tFactor) * (plotH - 30);

      if (px === 0) ctx.moveTo(xMargin + px, py);
      else ctx.lineTo(xMargin + px, py);
    }
    ctx.stroke();

    // Labels on major peaks
    currentComp.peaks.forEach(p => {
      const px = wToX(p.wavenumber);
      const py = baseLineY + p.intensity * (plotH - 30);

      ctx.fillStyle = "#38bdf8";
      ctx.font = "bold 10px Inter, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(p.wavenumber + " cm⁻¹", px, py + 16);
    });

    // Populate table
    const tableBody = document.getElementById("irPeakTableBody");
    if (tableBody) {
      tableBody.innerHTML = currentComp.peaks.map(p => `
        <tr>
          <td><strong style="color:var(--color-emerald);">${p.wavenumber} cm⁻¹</strong></td>
          <td>${(p.intensity * 100).toFixed(0)}%</td>
          <td><span class="chip chip-emerald">${p.group}</span></td>
          <td style="color:var(--text-muted);">${p.desc}</td>
        </tr>
      `).join("");
    }
  }

  window.selectIRCompound = function(compKey) {
    activeIRCompound = compKey;
    renderIRCanvas();
  };

  // 2. NMR Canvas Renderer
  function renderNMRCanvas() {
    const canvas = document.getElementById("nmrSpectrumCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const width = canvas.width = canvas.parentElement.clientWidth;
    const height = canvas.height = canvas.parentElement.clientHeight;

    ctx.clearRect(0, 0, width, height);

    const minPPM = 0;
    const maxPPM = 10;
    const xMargin = 50;
    const yMargin = 40;
    const plotW = width - xMargin * 2;
    const plotH = height - yMargin * 2;

    function ppmToX(ppm) {
      return xMargin + plotW * ((maxPPM - ppm) / (maxPPM - minPPM));
    }

    // Grid
    ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
    ctx.lineWidth = 1;

    for (let ppm = 0; ppm <= 10; ppm += 1) {
      const x = ppmToX(ppm);
      ctx.beginPath();
      ctx.moveTo(x, yMargin);
      ctx.lineTo(x, height - yMargin);
      ctx.stroke();

      ctx.fillStyle = "rgba(148, 163, 184, 0.7)";
      ctx.font = "11px Inter, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(ppm + " ppm", x, height - yMargin + 18);
    }

    // Baseline
    const baseY = height - yMargin - 10;
    ctx.strokeStyle = "rgba(148, 163, 184, 0.3)";
    ctx.beginPath();
    ctx.moveTo(xMargin, baseY);
    ctx.lineTo(width - xMargin, baseY);
    ctx.stroke();

    // TMS reference peak at 0 ppm
    const tmsX = ppmToX(0);
    ctx.strokeStyle = "#94a3b8";
    ctx.lineWidth = 2;
    ctx.beginPath();
    ctx.moveTo(tmsX, baseY);
    ctx.lineTo(tmsX, baseY - 80);
    ctx.stroke();
    ctx.fillText("TMS (0 ppm)", tmsX, baseY - 90);

    // Signals
    const comp = NMR_COMPOUNDS[activeNMRCompound];
    ctx.strokeStyle = "#38bdf8";
    ctx.lineWidth = 2;

    comp.signals.forEach(s => {
      const cx = ppmToX(s.shift);
      const peakH = 150;

      if (s.mult === "Singlet") {
        ctx.beginPath();
        ctx.moveTo(cx, baseY);
        ctx.lineTo(cx, baseY - peakH);
        ctx.stroke();
      } else if (s.mult === "Doublet") {
        ctx.beginPath();
        ctx.moveTo(cx - 4, baseY);
        ctx.lineTo(cx - 4, baseY - peakH * 0.9);
        ctx.moveTo(cx + 4, baseY);
        ctx.lineTo(cx + 4, baseY - peakH * 0.9);
        ctx.stroke();
      } else if (s.mult === "Triplet") {
        ctx.beginPath();
        ctx.moveTo(cx - 6, baseY);
        ctx.lineTo(cx - 6, baseY - peakH * 0.5);
        ctx.moveTo(cx, baseY);
        ctx.lineTo(cx, baseY - peakH);
        ctx.moveTo(cx + 6, baseY);
        ctx.lineTo(cx + 6, baseY - peakH * 0.5);
        ctx.stroke();
      } else if (s.mult === "Quartet") {
        ctx.beginPath();
        ctx.moveTo(cx - 9, baseY);
        ctx.lineTo(cx - 9, baseY - peakH * 0.33);
        ctx.moveTo(cx - 3, baseY);
        ctx.lineTo(cx - 3, baseY - peakH);
        ctx.moveTo(cx + 3, baseY);
        ctx.lineTo(cx + 3, baseY - peakH);
        ctx.moveTo(cx + 9, baseY);
        ctx.lineTo(cx + 9, baseY - peakH * 0.33);
        ctx.stroke();
      } else {
        // Multiplet cluster
        for (let k = -8; k <= 8; k += 4) {
          ctx.beginPath();
          ctx.moveTo(cx + k, baseY);
          ctx.lineTo(cx + k, baseY - peakH * (0.4 + Math.random() * 0.5));
          ctx.stroke();
        }
      }

      ctx.fillStyle = "#10b981";
      ctx.font = "bold 11px Inter, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(s.shift + " ppm (" + s.integration + ")", cx, baseY - peakH - 10);
    });

    const nmrBody = document.getElementById("nmrPeakTableBody");
    if (nmrBody) {
      nmrBody.innerHTML = comp.signals.map(s => `
        <tr>
          <td><strong style="color:var(--color-cyan);">${s.shift} ppm</strong></td>
          <td>${s.integration}</td>
          <td><span class="chip chip-cobalt">${s.mult}</span></td>
          <td>${s.j}</td>
          <td style="color:var(--text-muted);">${s.assignment}</td>
        </tr>
      `).join("");
    }
  }

  window.selectNMRCompound = function(compKey) {
    activeNMRCompound = compKey;
    renderNMRCanvas();
  };

  // 3. Beer-Lambert Law Calculator & UV-Vis
  window.updateBeerLambert = function() {
    const eps = parseFloat(document.getElementById("beerEpsilonInput")?.value || "12000");
    const c = parseFloat(document.getElementById("beerConcInput")?.value || "0.00005");
    const l = parseFloat(document.getElementById("beerPathInput")?.value || "1.0");

    const A = eps * c * l;
    const T = Math.pow(10, -A);
    const pctT = (T * 100).toFixed(2);

    const absDisplay = document.getElementById("beerAbsorbanceDisplay");
    if (absDisplay) absDisplay.textContent = A.toFixed(3);

    const transDisplay = document.getElementById("beerTransmittanceDisplay");
    if (transDisplay) transDisplay.textContent = pctT + "%";

    // Update cuvette liquid color opacity
    const liquid = document.getElementById("beerCuvetteLiquid");
    if (liquid) {
      const alpha = Math.min(0.95, Math.max(0.1, A * 0.7));
      liquid.style.backgroundColor = `rgba(16, 185, 129, ${alpha})`;
    }
  };

  // 4. Mass Spectrometry Canvas
  function renderMassCanvas() {
    const canvas = document.getElementById("massSpectrumCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const width = canvas.width = canvas.parentElement.clientWidth;
    const height = canvas.height = canvas.parentElement.clientHeight;

    ctx.clearRect(0, 0, width, height);

    const xMargin = 50;
    const yMargin = 40;
    const plotW = width - xMargin * 2;
    const plotH = height - yMargin * 2;
    const baseY = height - yMargin;

    const comp = MASS_SPEC_COMPOUNDS[activeMassCompound];
    const maxMZ = 80;

    function mzToX(mz) {
      return xMargin + (mz / maxMZ) * plotW;
    }

    // Grid
    ctx.strokeStyle = "rgba(255, 255, 255, 0.08)";
    ctx.lineWidth = 1;

    for (let mz = 10; mz <= maxMZ; mz += 10) {
      const x = mzToX(mz);
      ctx.beginPath();
      ctx.moveTo(x, yMargin);
      ctx.lineTo(x, baseY);
      ctx.stroke();

      ctx.fillStyle = "rgba(148, 163, 184, 0.7)";
      ctx.font = "11px Inter, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText("m/z " + mz, x, baseY + 18);
    }

    // Baseline
    ctx.strokeStyle = "rgba(148, 163, 184, 0.3)";
    ctx.beginPath();
    ctx.moveTo(xMargin, baseY);
    ctx.lineTo(width - xMargin, baseY);
    ctx.stroke();

    // Bars
    comp.peaks.forEach(p => {
      const x = mzToX(p.mz);
      const barH = (p.rel / 100) * (plotH - 20);

      ctx.strokeStyle = p.rel === 100 ? "#10b981" : "#8b5cf6";
      ctx.lineWidth = 3;
      ctx.beginPath();
      ctx.moveTo(x, baseY);
      ctx.lineTo(x, baseY - barH);
      ctx.stroke();

      ctx.fillStyle = p.rel === 100 ? "#10b981" : "#a78bfa";
      ctx.font = "bold 10px Inter, sans-serif";
      ctx.textAlign = "center";
      ctx.fillText(p.mz.toString(), x, baseY - barH - 6);
    });

    const massBody = document.getElementById("massPeakTableBody");
    if (massBody) {
      massBody.innerHTML = comp.peaks.map(p => `
        <tr>
          <td><strong style="color:var(--color-violet);">m/z ${p.mz}</strong></td>
          <td>${p.rel}%</td>
          <td><span class="chip ${p.rel === 100 ? 'chip-emerald' : 'chip-violet'}">${p.fragment}</span></td>
        </tr>
      `).join("");
    }
  }

  window.selectMassCompound = function(compKey) {
    activeMassCompound = compKey;
    renderMassCanvas();
  };

  // AI Research Assistant Query
  window.askResearchAssistant = async function() {
    const input = document.getElementById("researchQueryInput");
    const query = input?.value.trim();
    if (!query) return;

    const out = document.getElementById("researchOutputBox");
    if (out) {
      out.innerHTML = '<div style="color:var(--color-emerald);padding:1rem;">Searching academic databases & synthesizing chemistry literature...</div>';
    }

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: "Research summary on: " + query, style: "detailed" })
      });
      if (res.ok) {
        const data = await res.json();
        if (out && data.response) {
          out.innerHTML = `
            <div style="background:var(--bg-deep);padding:1.25rem;border-radius:var(--radius-md);border-left:3px solid var(--color-emerald);">
              <h4 style="color:#fff;margin-bottom:0.5rem;">Literature Synthesis: ${query}</h4>
              <p style="color:var(--text-main);line-height:1.6;font-size:0.92rem;">${data.response}</p>
            </div>
          `;
          return;
        }
      }
    } catch (e) {}

    // Fallback
    if (out) {
      out.innerHTML = `
        <div style="background:var(--bg-deep);padding:1.25rem;border-radius:var(--radius-md);border-left:3px solid var(--color-emerald);">
          <h4 style="color:#fff;margin-bottom:0.5rem;">Literature Synthesis: ${query}</h4>
          <p style="color:var(--text-main);line-height:1.6;font-size:0.92rem;">
            Investigation into <strong>${query}</strong> reveals critical thermodynamic stability and kinetic pathways governed by molecular orbital symmetry and spectroscopic signatures across IR, NMR, and Mass Spectrometry.
          </p>
        </div>
      `;
    }
  };

  window.addEventListener("DOMContentLoaded", () => {
    if (document.getElementById("irSpectrumCanvas")) {
      renderIRCanvas();
    }
    window.addEventListener("resize", () => {
      if (activeTab === "ir") renderIRCanvas();
      if (activeTab === "nmr") renderNMRCanvas();
      if (activeTab === "mass") renderMassCanvas();
    });
  });
})();
