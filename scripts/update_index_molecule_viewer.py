import re

with open("index.html", "r", encoding="utf-8-sig") as f:
    content = f.read()

# Replace script tags to include molecules-data.js
old_scripts = """  <script src="js/molecule-viewer.js"></script>"""
new_scripts = """  <script src="js/molecules-data.js"></script>\n  <script src="js/molecule-viewer.js"></script>"""

if old_scripts in content and "js/molecules-data.js" not in content:
    content = content.replace(old_scripts, new_scripts)

# Replace the molecule-viewer section content
new_section = r'''    <!-- 3D Molecule Viewer Section -->
    <section class="sec-wrap" id="molecule-viewer">
      <div class="container">
        <div class="sec-head">
          <div class="sec-eyebrow">
            <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><line x1="12" y1="9" x2="19" y2="7"/><line x1="12" y1="15" x2="5" y2="17"/></svg>
            <span>3D Interactive Molecular Exploration</span>
          </div>
          <h2 class="sec-title">3D Molecular Structure &amp; Chemistry Explorer</h2>
          <p class="sec-subtitle">
            Explore 85+ validated molecular structures in interactive 3D WebGL with CPK coloring, bond geometry, hybridization, and full chemical properties.
          </p>
        </div>

        <div class="mol-explorer-container">
          <!-- Search & Filter Controls -->
          <div class="mol-filter-header">
            <div class="mol-search-row">
              <div class="mol-search-input-wrap">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
                <input type="text" id="molSearchInput" class="mol-search-input" placeholder="Search 88+ molecules by name, formula (e.g. H2O, C6H6, Aspirin), or common name..." oninput="handleMoleculeSearch(this.value)">
              </div>
              <select id="molSortSelect" class="mol-sort-select" onchange="handleMoleculeSort(this.value)">
                <option value="name-asc">Alphabetical (A → Z)</option>
                <option value="name-desc">Alphabetical (Z → A)</option>
                <option value="mw-asc">Molecular Mass (Low → High)</option>
                <option value="mw-desc">Molecular Mass (High → Low)</option>
              </select>
            </div>
            <div class="mol-category-pills">
              <button type="button" class="mol-category-pill active" data-category="all" onclick="filterMoleculesCategory('all')">
                All Molecules <span class="pill-count">88</span>
              </button>
              <button type="button" class="mol-category-pill" data-category="simple" onclick="filterMoleculesCategory('simple')">
                Simple <span class="pill-count">12</span>
              </button>
              <button type="button" class="mol-category-pill" data-category="organic" onclick="filterMoleculesCategory('organic')">
                Organic <span class="pill-count">18</span>
              </button>
              <button type="button" class="mol-category-pill" data-category="acids-bases" onclick="filterMoleculesCategory('acids-bases')">
                Acids &amp; Bases <span class="pill-count">13</span>
              </button>
              <button type="button" class="mol-category-pill" data-category="inorganic" onclick="filterMoleculesCategory('inorganic')">
                Inorganic <span class="pill-count">16</span>
              </button>
              <button type="button" class="mol-category-pill" data-category="biochemical" onclick="filterMoleculesCategory('biochemical')">
                Biochemical <span class="pill-count">14</span>
              </button>
              <button type="button" class="mol-category-pill" data-category="other" onclick="filterMoleculesCategory('other')">
                Other Major <span class="pill-count">15</span>
              </button>
            </div>
          </div>

          <!-- Main 2-Column Workspace -->
          <div class="mol-main-grid">
            <!-- 3D Canvas Column -->
            <div class="molecule-viewer-wrapper">
              <div class="mol-toolbar">
                <div class="mol-mode-toggles">
                  <button type="button" class="mol-mode-btn active" data-mode="ballStick" onclick="setMolDisplayMode('ballStick')">Ball &amp; Stick</button>
                  <button type="button" class="mol-mode-btn" data-mode="stick" onclick="setMolDisplayMode('stick')">Stick</button>
                  <button type="button" class="mol-mode-btn" data-mode="spaceFill" onclick="setMolDisplayMode('spaceFill')">Space-Filling</button>
                </div>
                <div style="display:flex;gap:0.4rem;align-items:center;">
                  <button type="button" class="mol-tool-btn" id="molToggleLabelsBtn" onclick="toggleMolLabels()" title="Toggle Atom Labels">
                    Labels
                  </button>
                  <button type="button" class="mol-tool-btn active" id="molToggleAutoRotateBtn" onclick="toggleMolAutoRotate()" title="Toggle Auto-Spin">
                    Spin ⟳
                  </button>
                  <button type="button" class="mol-tool-btn" onclick="resetMolCamera()" title="Reset View">
                    Reset
                  </button>
                </div>
              </div>

              <div class="mol-canvas-container" id="molCanvasContainer">
                <!-- Floating Badge -->
                <div class="mol-canvas-badge">
                  <div class="mol-badge-formula" id="molHudFormula">H₂O</div>
                  <div class="mol-badge-name" id="molHudName">Water</div>
                  <div class="mol-badge-cat" id="molHudCat">Simple Molecules</div>
                </div>
                <div class="mol-hud-hint">
                  Left drag = Rotate · Right drag / Shift = Pan · Scroll = Zoom
                </div>
              </div>
            </div>

            <!-- Molecular Properties Dashboard Column -->
            <div class="mol-details-card">
              <div class="mol-details-header">
                <div>
                  <h3 class="mol-details-title" id="molDashTitle">Water</h3>
                  <div class="mol-details-common" id="molDashCommon">Common: Dihydrogen Monoxide</div>
                </div>
                <span class="mol-metric-badge" id="molDashFormula">H₂O</span>
              </div>

              <!-- Stats Grid -->
              <div class="mol-stats-grid">
                <div class="mol-stat-box">
                  <span class="mol-stat-label">Molar Mass</span>
                  <span class="mol-stat-value text-emerald" id="molDashMw">18.015 g/mol</span>
                </div>
                <div class="mol-stat-box">
                  <span class="mol-stat-label">Geometry</span>
                  <span class="mol-stat-value text-cobalt" id="molDashGeom">Bent (~104.5°)</span>
                </div>
                <div class="mol-stat-box">
                  <span class="mol-stat-label">Bond Angle</span>
                  <span class="mol-stat-value" id="molDashAngle">104.45°</span>
                </div>
                <div class="mol-stat-box">
                  <span class="mol-stat-label">Hybridization</span>
                  <span class="mol-stat-value" id="molDashHybrid">sp³</span>
                </div>
                <div class="mol-stat-box">
                  <span class="mol-stat-label">Polarity</span>
                  <span class="mol-stat-value" id="molDashPolar">Polar (μ = 1.85 D)</span>
                </div>
                <div class="mol-stat-box">
                  <span class="mol-stat-label">Atom / Bond Count</span>
                  <span class="mol-stat-value" id="molDashCounts">3 Atoms · 2 Bonds</span>
                </div>
              </div>

              <!-- Detailed Info Sections -->
              <div class="mol-info-section">
                <div class="mol-info-title">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 16v-4M12 8h.01"/></svg>
                  Physical Properties
                </div>
                <p class="mol-info-text" id="molDashPhysical">Colorless liquid; mp 0°C, bp 100°C; density 1.00 g/cm³; high specific heat (4.184 J/g·K).</p>
              </div>

              <div class="mol-info-section">
                <div class="mol-info-title">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 2v7.31L4.62 18.27A2 2 0 0 0 6.35 21h11.3a2 2 0 0 0 1.73-2.73L14 9.31V2"/></svg>
                  Chemical Properties &amp; Bonding
                </div>
                <p class="mol-info-text" id="molDashChemical">Amphoteric; autoionizes Kw = 1.0 × 10⁻¹⁴; forms extensive 3D hydrogen bonding network.</p>
                <div style="font-size:0.78rem;color:var(--text-dim);margin-top:4px;">Bond Types: <span id="molDashBondTypes" style="color:var(--text-muted);font-weight:600;">Polar covalent σ bonds</span></div>
              </div>

              <div class="mol-info-section">
                <div class="mol-info-title">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
                  Common Uses &amp; Applications
                </div>
                <p class="mol-info-text" id="molDashUses">Universal solvent in biology and chemical syntheses, industrial coolant, baseline reference for temperature and density scales.</p>
              </div>

              <div class="mol-info-section" style="border-left: 3px solid var(--color-amber);">
                <div class="mol-info-title" style="color:var(--color-amber);">
                  <svg width="15" height="15" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 8v4M12 16h.01"/></svg>
                  Scientific Facts
                </div>
                <p class="mol-info-text" id="molDashFacts">Ice floats on liquid water because its hydrogen-bonded hexagonal crystal lattice holds molecules farther apart than the chaotic liquid state.</p>
              </div>
            </div>
          </div>

          <!-- Bottom Molecule Catalogue Roster -->
          <div class="mol-carousel-wrap">
            <div class="mol-carousel-title">
              <span>Quick Molecule Catalogue</span>
              <span id="molFilteredCount" style="font-size:0.82rem;font-weight:600;color:var(--color-emerald);">Showing 88 Molecules</span>
            </div>
            <div class="mol-cards-strip" id="molCardsStrip">
              <!-- Dynamically populated cards -->
            </div>
          </div>
        </div>
      </div>
    </section>'''

# Match existing molecule-viewer section
section_pattern = re.compile(r'<!-- 3D Molecule Viewer Section -->\s*<section class="sec-wrap" id="molecule-viewer">.*?</section>', re.DOTALL)
if section_pattern.search(content):
    content = section_pattern.sub(new_section, content)
    with open("index.html", "w", encoding="utf-8") as out:
        out.write(content)
    print("index.html successfully updated with upgraded 3D Molecule Explorer!")
else:
    print("Error: Could not locate molecule-viewer section in index.html")
