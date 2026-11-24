import os

content = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Spectroscopy & Research Hub - ChemAI Platform</title>
  <meta name="description" content="Interactive Infrared (IR), 1H/13C NMR, UV-Vis Beer-Lambert Law, Mass Spectrometry (m/z), and Chemical Research Assistant.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/spectroscopy.css">
</head>
<body>
  <canvas id="particle-canvas" aria-hidden="true"></canvas>
  <div class="ambient-glow ambient-glow-1"></div>
  <div class="ambient-glow ambient-glow-2"></div>

  <!-- Sticky Modern Navigation Bar -->
  <header class="site-nav" role="banner">
    <div class="container">
      <div class="nav-container">
        <a href="index.html" class="nav-brand" aria-label="ChemAI Home">
          <div class="brand-icon-box">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
              <path d="M10 2v7.31L4.62 18.27A2 2 0 0 0 6.35 21h11.3a2 2 0 0 0 1.73-2.73L14 9.31V2"/>
              <line x1="8.5" y1="2" x2="15.5" y2="2"/>
              <path d="M14 9.3a6.5 6.5 0 0 0-4 0"/>
            </svg>
          </div>
          <span>Chem<span class="brand-text-ai">AI</span></span>
        </a>
        <nav class="nav-links" id="siteNavLinks">
          <a href="index.html" class="nav-link">Home</a>
          <a href="index.html#ai-assistant" class="nav-link">AI Assistant</a>
          <a href="tools.html" class="nav-link">Tools</a>
          <a href="virtual-lab.html" class="nav-link">Virtual Lab</a>
          <a href="simulations.html" class="nav-link">Simulations</a>
          <a href="periodic-table.html" class="nav-link">Periodic Table</a>
          <a href="index.html#molecule-viewer" class="nav-link">3D Molecules</a>
          <a href="study-hub.html" class="nav-link">Study Hub</a>
          <a href="spectroscopy.html" class="nav-link active">Spectroscopy</a>
        </nav>
        <div class="nav-actions">
          <button type="button" class="btn-icon theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()" aria-label="Toggle dark/light theme" title="Toggle theme">
            <span class="theme-toggle-icon">☀️</span>
          </button>
          <button type="button" class="nav-search-btn" onclick="openSearchPalette()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <span>Search</span>
            <kbd>Ctrl K</kbd>
          </button>
          <a href="virtual-lab.html" class="btn btn-primary btn-sm">Launch Lab</a>
        </div>
      </div>
    </div>
  </header>

  <main class="container" style="padding-top:2.5rem;padding-bottom:5rem;">
    <div class="sec-head">
      <span class="sec-eyebrow">Structural Elucidation & Analytics</span>
      <h1 class="sec-title">Spectroscopy &amp; Research Hub</h1>
      <p class="sec-subtitle">Interactive spectra for Infrared (IR), Nuclear Magnetic Resonance (NMR), UV-Vis Beer-Lambert law, and Mass Spectrometry.</p>
    </div>

    <div class="spectroscopy-layout">
      <!-- Sidebar Navigation -->
      <aside class="spec-sidebar">
        <button class="spec-nav-tab active" data-tab="ir" onclick="switchSpecTab('ir')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
          <span>Infrared (IR) Spectra</span>
        </button>
        <button class="spec-nav-tab" data-tab="nmr" onclick="switchSpecTab('nmr')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><line x1="12" y1="9" x2="19" y2="7"/><line x1="12" y1="15" x2="5" y2="17"/></svg>
          <span>1H &amp; 13C NMR Shifts</span>
        </button>
        <button class="spec-nav-tab" data-tab="uvvis" onclick="switchSpecTab('uvvis')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="m4.93 4.93 4.24 4.24M14.83 9.17l4.24-4.24M14.83 14.83l4.24 4.24M9.17 14.83l-4.24 4.24"/></svg>
          <span>UV-Vis &amp; Beer-Lambert</span>
        </button>
        <button class="spec-nav-tab" data-tab="mass" onclick="switchSpecTab('mass')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><line x1="18" y1="20" x2="18" y2="10"/><line x1="12" y1="20" x2="12" y2="4"/><line x1="6" y1="20" x2="6" y2="14"/></svg>
          <span>Mass Spectrometry</span>
        </button>
        <button class="spec-nav-tab" data-tab="research" onclick="switchSpecTab('research')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"/></svg>
          <span>Research Assistant</span>
        </button>
      </aside>

      <!-- Main Display Area -->
      <div class="glass-card" style="padding:1.75rem;">
        <!-- Pane 1: IR Spectroscopy -->
        <div class="spec-tab-pane" id="specPane_ir">
          <div class="spec-controls-bar">
            <div>
              <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">Fourier-Transform Infrared (FTIR) Spectrum</h3>
              <p style="color:var(--text-muted);font-size:0.85rem;margin:0;">Wavenumber (4000 to 400 cm⁻¹) vs. Transmittance (%)</p>
            </div>
            <div style="display:flex;gap:0.5rem;align-items:center;">
              <label style="font-size:0.85rem;color:var(--text-muted);">Compound:</label>
              <select class="calc-input" style="width:auto;padding:0.4rem 0.8rem;" onchange="selectIRCompound(this.value)">
                <option value="ethanol">Ethanol (CH3CH2OH)</option>
                <option value="acetone">Acetone (CH3COCH3)</option>
                <option value="acetic_acid">Acetic Acid (CH3COOH)</option>
                <option value="benzaldehyde">Benzaldehyde (C6H5CHO)</option>
              </select>
            </div>
          </div>
          <div class="spec-canvas-container">
            <canvas id="irSpectrumCanvas"></canvas>
          </div>
          <h4 style="color:var(--color-emerald);font-size:1.05rem;margin:1.25rem 0 0.5rem;">Diagnostic Functional Group Peaks</h4>
          <table class="spec-peak-table">
            <thead>
              <tr>
                <th>Wavenumber</th>
                <th>Absorption</th>
                <th>Vibrational Mode</th>
                <th>Diagnostic Interpretation</th>
              </tr>
            </thead>
            <tbody id="irPeakTableBody"></tbody>
          </table>
        </div>

        <!-- Pane 2: NMR Spectroscopy -->
        <div class="spec-tab-pane" id="specPane_nmr" style="display:none;">
          <div class="spec-controls-bar">
            <div>
              <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">Proton (¹H) Nuclear Magnetic Resonance</h3>
              <p style="color:var(--text-muted);font-size:0.85rem;margin:0;">Chemical Shifts (δ 0 to 10 ppm) &amp; J-Coupling Multiplets</p>
            </div>
            <div style="display:flex;gap:0.5rem;align-items:center;">
              <label style="font-size:0.85rem;color:var(--text-muted);">Sample:</label>
              <select class="calc-input" style="width:auto;padding:0.4rem 0.8rem;" onchange="selectNMRCompound(this.value)">
                <option value="ethanol">Ethanol</option>
                <option value="ethyl_acetate">Ethyl Acetate</option>
                <option value="toluene">Toluene</option>
              </select>
            </div>
          </div>
          <div class="spec-canvas-container">
            <canvas id="nmrSpectrumCanvas"></canvas>
          </div>
          <h4 style="color:var(--color-cyan);font-size:1.05rem;margin:1.25rem 0 0.5rem;">Resonance Chemical Shifts &amp; Spin-Spin Coupling</h4>
          <table class="spec-peak-table">
            <thead>
              <tr>
                <th>Chemical Shift (δ)</th>
                <th>Integration</th>
                <th>Multiplicity (n+1)</th>
                <th>J-Coupling</th>
                <th>Proton Environment Assignment</th>
              </tr>
            </thead>
            <tbody id="nmrPeakTableBody"></tbody>
          </table>
        </div>

        <!-- Pane 3: UV-Vis & Beer-Lambert Law -->
        <div class="spec-tab-pane" id="specPane_uvvis" style="display:none;">
          <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">UV-Vis Absorption &amp; Beer-Lambert Law</h3>
          <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1.5rem;">Equation: <strong>A = ε · c · l</strong> (Absorbance = Molar Absorptivity × Concentration × Pathlength)</p>

          <div class="beer-lambert-grid">
            <div>
              <div class="calc-form-group" style="margin-bottom:1rem;">
                <label class="calc-label">Molar Absorptivity ε (L·mol⁻¹·cm⁻¹)</label>
                <div class="calc-input-wrapper">
                  <input type="number" id="beerEpsilonInput" class="calc-input" value="12000" oninput="updateBeerLambert()">
                </div>
              </div>
              <div class="calc-form-group" style="margin-bottom:1rem;">
                <label class="calc-label">Concentration c (M = mol/L)</label>
                <div class="calc-input-wrapper">
                  <input type="number" id="beerConcInput" class="calc-input" step="0.00001" value="0.00005" oninput="updateBeerLambert()">
                </div>
              </div>
              <div class="calc-form-group" style="margin-bottom:1.25rem;">
                <label class="calc-label">Pathlength l (cm)</label>
                <div class="calc-input-wrapper">
                  <input type="number" id="beerPathInput" class="calc-input" step="0.1" value="1.0" oninput="updateBeerLambert()">
                </div>
              </div>
              <div style="background:var(--bg-deep);padding:1rem;border-radius:var(--radius-md);border:1px solid var(--border-subtle);">
                <div style="display:flex;justify-content:space-between;margin-bottom:0.5rem;">
                  <span style="color:var(--text-muted);">Absorbance (A):</span>
                  <strong id="beerAbsorbanceDisplay" style="color:var(--color-emerald);font-size:1.25rem;">0.600</strong>
                </div>
                <div style="display:flex;justify-content:space-between;">
                  <span style="color:var(--text-muted);">Transmittance (%T):</span>
                  <strong id="beerTransmittanceDisplay" style="color:var(--color-cyan);font-size:1.1rem;">25.12%</strong>
                </div>
              </div>
            </div>

            <!-- Cuvette Visualizer -->
            <div style="text-align:center;">
              <div class="cuvette-preview">
                <div class="cuvette-liquid" id="beerCuvetteLiquid"></div>
              </div>
              <p style="font-size:0.85rem;color:var(--text-muted);margin-top:0.75rem;">Simulated Spectrophotometer Cuvette (1 cm quartz cell)</p>
            </div>
          </div>
        </div>

        <!-- Pane 4: Mass Spectrometry -->
        <div class="spec-tab-pane" id="specPane_mass" style="display:none;">
          <div class="spec-controls-bar">
            <div>
              <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">Electron Ionization Mass Spectrometry (EI-MS)</h3>
              <p style="color:var(--text-muted);font-size:0.85rem;margin:0;">Mass-to-charge ratio (m/z) vs. Relative Abundance (%)</p>
            </div>
            <div style="display:flex;gap:0.5rem;align-items:center;">
              <label style="font-size:0.85rem;color:var(--text-muted);">Analyte:</label>
              <select class="calc-input" style="width:auto;padding:0.4rem 0.8rem;" onchange="selectMassCompound(this.value)">
                <option value="acetone">Acetone (MW = 58)</option>
                <option value="ethanol">Ethanol (MW = 46)</option>
              </select>
            </div>
          </div>
          <div class="spec-canvas-container">
            <canvas id="massSpectrumCanvas"></canvas>
          </div>
          <h4 style="color:var(--color-violet);font-size:1.05rem;margin:1.25rem 0 0.5rem;">Mass Fragmentation Peaks &amp; Isotopes</h4>
          <table class="spec-peak-table">
            <thead>
              <tr>
                <th>m/z Ratio</th>
                <th>Relative Abundance (%)</th>
                <th>Fragment Ion Formula</th>
              </tr>
            </thead>
            <tbody id="massPeakTableBody"></tbody>
          </table>
        </div>

        <!-- Pane 5: Research Assistant -->
        <div class="spec-tab-pane" id="specPane_research" style="display:none;">
          <h3 style="color:var(--text-highlight);margin-bottom:0.5rem;">Chemical Literature &amp; Research Assistant</h3>
          <p style="color:var(--text-muted);font-size:0.88rem;margin-bottom:1.25rem;">Query reaction mechanisms, synthesis routes, or spectroscopy literature.</p>
          <div style="display:flex;gap:0.75rem;margin-bottom:1.5rem;">
            <input type="text" id="researchQueryInput" class="calc-input" placeholder="e.g. Diels-Alder endo stereospecificity or Suzuki coupling mechanism..." style="flex:1;">
            <button class="btn btn-primary btn-sm" onclick="askResearchAssistant()">Search Literature</button>
          </div>
          <div id="researchOutputBox">
            <div style="color:var(--text-dim);font-style:italic;padding:1.5rem;background:var(--bg-deep);border-radius:var(--radius-md);">
              Type a topic above to query peer-reviewed chemical insights.
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>

  <!-- Universal Calculator Modal -->
  <div class="modal-backdrop" id="calculatorModalBackdrop" role="dialog" aria-modal="true">
    <div class="modal-container">
      <div class="modal-header">
        <h3 id="calcModalTitle">Chemistry Calculator</h3>
        <button type="button" class="modal-close-btn" onclick="closeCalculatorModal()"><kbd>ESC</kbd></button>
      </div>
      <div class="modal-body" id="calcModalBody"></div>
    </div>
  </div>

  <!-- Search Modal -->
  <div class="modal-backdrop" id="searchModalBackdrop" role="dialog" aria-modal="true">
    <div class="modal-container search-modal-container">
      <div class="search-input-header">
        <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="var(--color-emerald)" stroke-width="2.5"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input type="text" id="searchPaletteInput" class="search-main-input" placeholder="Search any calculator, element or simulation..." autocomplete="off">
        <button type="button" class="modal-close-btn" onclick="closeSearchPalette()"><kbd>ESC</kbd></button>
      </div>
      <ul class="search-results-list" id="searchResultsList"></ul>
    </div>
  </div>

  <footer class="site-footer">
    <div class="container">
      <div class="footer-bottom">
        <div>&copy; 2026 ChemAI Laboratory. Free Interactive Chemistry Educational Suite.</div>
        <div><a href="index.html" class="text-emerald">Return to Main Platform →</a></div>
      </div>
    </div>
  </footer>

  <script src="js/particles.js"></script>
  <script src="js/calculators.js"></script>
  <script src="js/spectroscopy-hub.js"></script>
  <script src="js/app.js"></script>
</body>
</html>
"""

with open("spectroscopy.html", "w", encoding="utf-8") as f:
    f.write(content)
print("Wrote spectroscopy.html")
