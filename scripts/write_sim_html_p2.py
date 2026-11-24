part2 = """
        <!-- 2. VSEPR 3D Shapes Pane -->
        <div class="sim-tab-pane" id="simPane_vsepr" style="display:none;">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;">
            <div>
              <h3 style="color:var(--text-highlight);margin:0;">VSEPR 3D Molecular Geometry Explorer</h3>
              <p style="color:var(--text-muted);font-size:0.85rem;margin:0.25rem 0 0;">Valence Shell Electron Pair Repulsion: adjust bonded ligands and lone pairs.</p>
            </div>
            <span class="chip chip-emerald" id="vseprGeomName">Tetrahedral</span>
          </div>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:1rem;">
            <div>
              <label class="calc-label" style="display:flex;justify-content:space-between;">
                <span>Bonding Pairs (Ligands):</span>
                <strong id="vseprBondVal" style="color:var(--color-emerald);">4</strong>
              </label>
              <input type="range" id="vseprBondSlider" min="1" max="6" value="4" style="width:100%;margin-top:0.4rem;" oninput="updateVSEPR()">
            </div>
            <div>
              <label class="calc-label" style="display:flex;justify-content:space-between;">
                <span>Lone Electron Pairs:</span>
                <strong id="vseprLoneVal" style="color:var(--color-amber);">0</strong>
              </label>
              <input type="range" id="vseprLoneSlider" min="0" max="3" value="0" style="width:100%;margin-top:0.4rem;" oninput="updateVSEPR()">
            </div>
          </div>

          <div class="sim-canvas-box" id="vseprCanvasContainer" style="height:360px;"></div>

          <div style="display:grid;grid-template-columns:repeat(3, 1fr);gap:1rem;background:var(--bg-deep);padding:1rem;border-radius:var(--radius-md);">
            <div><span style="color:var(--text-muted);font-size:0.85rem;">Electron Geometry:</span><br><strong id="vseprElectronGeom" style="color:#fff;">Tetrahedral</strong></div>
            <div><span style="color:var(--text-muted);font-size:0.85rem;">Ideal Bond Angle:</span><br><strong id="vseprAngle" style="color:var(--color-cyan);">109.5°</strong></div>
            <div><span style="color:var(--text-muted);font-size:0.85rem;">Hybridization:</span><br><strong id="vseprHybridization" style="color:var(--color-violet);">sp³</strong></div>
          </div>
        </div>

        <!-- 3. Chemical Bonding Pane -->
        <div class="sim-tab-pane" id="simPane_bonding" style="display:none;">
          <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">Electronegativity &amp; Chemical Bond Type</h3>
          <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Pauling Electronegativity Difference (ΔEN) determines bond polarity.</p>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:1rem;">
            <div class="calc-form-group">
              <label class="calc-label">Element A</label>
              <select id="bondElem1Select" class="calc-input" onchange="updateBondingSim()">
                <option value="H">Hydrogen (H, EN = 2.20)</option>
                <option value="C">Carbon (C, EN = 2.55)</option>
                <option value="Na">Sodium (Na, EN = 0.93)</option>
                <option value="K">Potassium (K, EN = 0.82)</option>
              </select>
            </div>
            <div class="calc-form-group">
              <label class="calc-label">Element B</label>
              <select id="bondElem2Select" class="calc-input" onchange="updateBondingSim()">
                <option value="Cl">Chlorine (Cl, EN = 3.16)</option>
                <option value="F">Fluorine (F, EN = 3.98)</option>
                <option value="O">Oxygen (O, EN = 3.44)</option>
                <option value="Br">Bromine (Br, EN = 2.96)</option>
              </select>
            </div>
          </div>

          <div class="sim-canvas-box" style="height:260px;">
            <canvas id="bondingCloudCanvas"></canvas>
          </div>

          <div style="background:var(--bg-deep);padding:1rem;border-radius:var(--radius-md);">
            <div style="display:flex;justify-content:space-between;margin-bottom:0.4rem;">
              <span style="color:var(--text-muted);">ΔEN (Difference):</span>
              <strong id="bondEnDiffDisplay" style="color:var(--color-cyan);font-size:1.15rem;">0.96</strong>
            </div>
            <div style="display:flex;justify-content:space-between;margin-bottom:0.4rem;">
              <span style="color:var(--text-muted);">Predicted Bond Character:</span>
              <strong id="bondTypeDisplay" style="color:var(--color-emerald);font-size:1.15rem;">Polar Covalent</strong>
            </div>
            <p id="bondTypeDesc" style="color:var(--text-dim);font-size:0.85rem;margin:0.25rem 0 0;"></p>
          </div>
        </div>

        <!-- 4. Aufbau Pane -->
        <div class="sim-tab-pane" id="simPane_aufbau" style="display:none;">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;">
            <div>
              <h3 style="color:var(--text-highlight);margin:0;">Aufbau Orbital Energy Level Animator</h3>
              <p style="color:var(--text-muted);font-size:0.85rem;margin:0.25rem 0 0;">Fills electron orbitals in order of increasing energy (n + l rule) adhering to Hund's Rule and Pauli Exclusion.</p>
            </div>
            <span class="chip chip-emerald" id="aufbauZDisplay">Z = 6</span>
          </div>

          <div style="margin-bottom:1.5rem;">
            <label class="calc-label">Atomic Number (Z = 1 to 30):</label>
            <input type="range" id="aufbauZSlider" min="1" max="30" value="6" style="width:100%;margin-top:0.4rem;" oninput="updateAufbauSim()">
          </div>

          <div style="background:var(--bg-deep);padding:1rem;border-radius:var(--radius-md);margin-bottom:1.25rem;">
            <span style="color:var(--text-muted);font-size:0.85rem;">Ground State Configuration:</span>
            <div id="aufbauConfigDisplay" style="font-size:1.2rem;color:var(--color-emerald);font-family:var(--font-mono);margin-top:0.25rem;">1s² 2s² 2p²</div>
          </div>

          <div class="aufbau-energy-levels" id="aufbauLevelsContainer"></div>
        </div>

        <!-- 5. Reaction Energy Diagram Pane -->
        <div class="sim-tab-pane" id="simPane_energy" style="display:none;">
          <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">Reaction Coordinate Energy Diagram</h3>
          <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Exothermic vs. Endothermic potential energy profile and catalytic activation barrier reduction.</p>

          <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:1rem;margin-bottom:1rem;align-items:center;">
            <div>
              <label class="calc-label">Activation Energy Ea (kJ/mol):</label>
              <input type="number" id="energyEaInput" class="calc-input" value="60" oninput="renderEnergyDiagram()">
            </div>
            <div>
              <label class="calc-label">Enthalpy Change ΔH (kJ/mol):</label>
              <input type="number" id="energyDhInput" class="calc-input" value="-30" oninput="renderEnergyDiagram()">
            </div>
            <div style="padding-top:1.5rem;">
              <label style="display:flex;align-items:center;gap:0.5rem;color:var(--color-emerald);cursor:pointer;font-weight:600;">
                <input type="checkbox" id="energyCatToggle" onchange="renderEnergyDiagram()">
                <span>Add Catalyst (Lowers Ea)</span>
              </label>
            </div>
          </div>

          <div class="sim-canvas-box" style="height:320px;">
            <canvas id="energyDiagramCanvas"></canvas>
          </div>
        </div>

        <!-- 6. Le Chatelier Pane -->
        <div class="sim-tab-pane" id="simPane_lechatelier" style="display:none;">
          <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">Le Chatelier's Principle Dynamic Simulator</h3>
          <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Exothermic Haber System: <strong>N₂ (g) + 3H₂ (g) ⇌ 2NH₃ (g) + 92 kJ</strong></p>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:1.5rem;">
            <div>
              <label class="calc-label" style="display:flex;justify-content:space-between;">
                <span>Temperature (K):</span>
                <strong id="leChatTempVal" style="color:var(--color-amber);">400 K</strong>
              </label>
              <input type="range" id="leChatTempSlider" min="250" max="700" value="400" style="width:100%;margin-top:0.4rem;" oninput="updateLeChatelier()">
            </div>
            <div>
              <label class="calc-label" style="display:flex;justify-content:space-between;">
                <span>Total Pressure (atm):</span>
                <strong id="leChatPressVal" style="color:var(--color-cyan);">1.0 atm</strong>
              </label>
              <input type="range" id="leChatPressSlider" min="0.5" max="5.0" step="0.1" value="1.0" style="width:100%;margin-top:0.4rem;" oninput="updateLeChatelier()">
            </div>
          </div>

          <div style="background:var(--bg-deep);padding:1.5rem;border-radius:var(--radius-md);border-left:3px solid var(--color-emerald);">
            <span style="color:var(--text-muted);font-size:0.85rem;">System Response:</span>
            <h4 id="leChatShiftResult" style="color:var(--color-emerald);font-size:1.25rem;margin:0.5rem 0 0;">Equilibrium Steady</h4>
          </div>
        </div>

        <!-- 7. Gas Laws Pane -->
        <div class="sim-tab-pane" id="simPane_gas" style="display:none;">
          <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">Gas Laws Particle Chamber (PV = nRT)</h3>
          <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Kinetic molecular theory: elastic collisions against piston chamber walls.</p>
          <div class="sim-canvas-box" style="height:320px;">
            <canvas id="gasSimCanvas"></canvas>
          </div>
        </div>

        <!-- 8. Galvanic Cell Pane -->
        <div class="sim-tab-pane" id="simPane_galvanic" style="display:none;">
          <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">Galvanic Daniell Cell Simulator</h3>
          <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Spontaneous redox electron transfer: Zn (s) + Cu²⁺ (aq) → Zn²⁺ (aq) + Cu (s), E° = 1.10 V.</p>
          <div class="sim-canvas-box" style="height:340px;">
            <canvas id="galvanicSimCanvas"></canvas>
          </div>
        </div>

        <!-- 9. Solubility Pane -->
        <div class="sim-tab-pane" id="simPane_solubility" style="display:none;">
          <h3 style="color:var(--text-highlight);margin-bottom:0.25rem;">Solubility Product &amp; Precipitation (Ksp)</h3>
          <p style="color:var(--text-muted);font-size:0.85rem;margin-bottom:1rem;">Mix aqueous ionic solutions to evaluate ion product Q vs. solubility product Ksp.</p>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:1.5rem;margin-bottom:1.5rem;">
            <div class="calc-form-group">
              <label class="calc-label">Cation Solution (0.05 M)</label>
              <select id="solCationSelect" class="calc-input" onchange="testPrecipitation()">
                <option value="Ag+">Silver Ion (Ag⁺)</option>
                <option value="Pb2+">Lead(II) Ion (Pb²⁺)</option>
                <option value="Ba2+">Barium Ion (Ba²⁺)</option>
                <option value="Na+">Sodium Ion (Na⁺)</option>
              </select>
            </div>
            <div class="calc-form-group">
              <label class="calc-label">Anion Solution (0.05 M)</label>
              <select id="solAnionSelect" class="calc-input" onchange="testPrecipitation()">
                <option value="Cl-">Chloride (Cl⁻)</option>
                <option value="I-">Iodide (I⁻)</option>
                <option value="SO42-">Sulfate (SO₄²⁻)</option>
                <option value="NO3-">Nitrate (NO₃⁻)</option>
              </select>
            </div>
          </div>

          <div style="background:var(--bg-deep);padding:1.5rem;border-radius:var(--radius-md);border-left:3px solid var(--color-emerald);">
            <span style="color:var(--text-muted);font-size:0.85rem;">Precipitation Outcome:</span>
            <h4 id="solPptResult" style="color:var(--color-rose);font-size:1.2rem;margin:0.5rem 0 0;">White Precipitate formed! AgCl (s) (Ksp = 1.8 × 10⁻¹⁰)</h4>
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

  <script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
  <script src="js/particles.js"></script>
  <script src="js/calculators.js"></script>
  <script src="js/simulations-hub.js"></script>
  <script src="js/app.js"></script>
</body>
</html>
"""

with open("simulations.html", "a", encoding="utf-8") as f:
    f.write(part2)
print("Appended Part 2 to simulations.html")
