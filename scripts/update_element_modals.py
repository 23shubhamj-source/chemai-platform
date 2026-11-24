import re

modal_html = """  <!-- Element Detail Inspector Modal -->
  <div class="modal-backdrop" id="elementModalBackdrop" role="dialog" aria-modal="true" aria-labelledby="modalElementName">
    <div class="modal-container" style="max-width:820px;max-height:90vh;overflow-y:auto;">
      <div class="modal-header">
        <h3 id="modalElementName">Element Inspector</h3>
        <button type="button" class="modal-close-btn" id="closeElementModalBtn" onclick="closeElementModal()" aria-label="Close modal">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
        </button>
      </div>
      <div class="modal-body" style="padding:1.5rem;">
        <div class="ptable-modal-grid">
          <!-- Left Column: Big Symbol & Bohr Model -->
          <div class="element-big-card">
            <span class="chip chip-emerald" id="modalElementCat" style="margin-bottom:0.25rem;">Category</span>
            <div class="element-big-symbol" id="modalElementSymbol">H</div>
            <div style="font-size:1.15rem;font-weight:700;color:var(--text-highlight);" id="modalElementMass">1.008 u</div>
            <div style="display:flex;gap:0.4rem;font-size:0.75rem;margin:0.25rem 0;">
              <span class="mono" style="background:rgba(239,68,68,0.2);color:#fca5a5;padding:2px 6px;border-radius:4px;"><span id="modalElementProtons">1</span> p⁺</span>
              <span class="mono" style="background:rgba(16,185,129,0.2);color:#6ee7b7;padding:2px 6px;border-radius:4px;"><span id="modalElementElectrons">1</span> e⁻</span>
              <span class="mono" style="background:rgba(59,130,246,0.2);color:#93c5fd;padding:2px 6px;border-radius:4px;"><span id="modalElementNeutrons">0</span> n⁰</span>
            </div>
            <canvas id="bohrModelCanvas" class="bohr-model-canvas" width="200" height="200"></canvas>
            <div style="font-size:0.72rem;color:var(--text-dim);letter-spacing:0.02em;">Concentric Bohr Quantum Shells</div>
          </div>

          <!-- Right Column: Full Scientific Properties -->
          <div style="display:flex;flex-direction:column;gap:1rem;">
            <table class="element-props-table">
              <tr><td>Group &amp; Period:</td><td><span id="modalElementGroup">Group 1</span>, <span id="modalElementPeriod">Period 1</span> (<span id="modalElementBlock">s-block</span>)</td></tr>
              <tr><td>Electron Config:</td><td id="modalElementConfig" class="mono text-emerald" style="font-weight:700;">1s¹</td></tr>
              <tr><td>Oxidation States:</td><td id="modalElementOxidation">+1, -1</td></tr>
              <tr><td>Pauling Electronegativity:</td><td id="modalElementEN">2.20</td></tr>
              <tr><td>1st Ionization Energy:</td><td id="modalElementIonization">1312 kJ/mol</td></tr>
              <tr><td>Atomic Radius:</td><td id="modalElementRadius">53 pm</td></tr>
              <tr><td>Melting / Boiling Point:</td><td><span id="modalElementMelt">-259.2 °C</span> / <span id="modalElementBoil">-252.9 °C</span></td></tr>
              <tr><td>Density &amp; State:</td><td><span id="modalElementDensity">0.089 g/L</span> (<span id="modalElementState">Gas</span> at STP)</td></tr>
            </table>

            <div style="background:var(--bg-deep);border:1px solid var(--border-subtle);border-radius:var(--radius-md);padding:0.75rem;">
              <div style="font-size:0.72rem;color:var(--color-emerald);font-weight:700;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:3px;">Discovery History</div>
              <p id="modalElementHistory" style="font-size:0.84rem;color:var(--text-main);line-height:1.4;margin:0;">Discovered in 1766 by Henry Cavendish (UK).</p>
            </div>

            <div style="background:var(--bg-deep);border:1px solid var(--border-subtle);border-radius:var(--radius-md);padding:0.75rem;">
              <div style="font-size:0.72rem;color:var(--color-cobalt);font-weight:700;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:3px;">Primary Applications</div>
              <p id="modalElementUses" style="font-size:0.84rem;color:var(--text-main);line-height:1.4;margin:0;">Clean hydrogen fuel cells, Haber-Bosch ammonia synthesis, rocket propulsion.</p>
            </div>

            <div style="background:var(--bg-deep);border:1px solid var(--border-subtle);border-left:3px solid var(--color-amber);border-radius:var(--radius-md);padding:0.75rem;">
              <div style="font-size:0.72rem;color:var(--color-amber);font-weight:700;text-transform:uppercase;letter-spacing:0.05em;margin-bottom:3px;">Scientific Facts</div>
              <p id="modalElementFacts" style="font-size:0.84rem;color:var(--text-main);line-height:1.4;margin:0;">Hydrogen accounts for 75% of all normal elemental baryonic mass in the universe.</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>"""

for filename in ["index.html", "periodic-table.html"]:
    with open(filename, "r", encoding="utf-8-sig") as f:
        content = f.read()
    
    pattern = re.compile(r'<!-- Element Detail Inspector Modal -->\s*<div class="modal-backdrop" id="elementModalBackdrop"[^>]*>.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(modal_html, content)
        with open(filename, "w", encoding="utf-8") as out:
            out.write(content)
        print(f"{filename} element modal updated!")
    else:
        # Fallback regex
        pattern2 = re.compile(r'<div class="modal-backdrop" id="elementModalBackdrop"[^>]*>.*?</div>\s*</div>\s*</div>\s*</div>', re.DOTALL)
        if pattern2.search(content):
            content = pattern2.sub(modal_html, content)
            with open(filename, "w", encoding="utf-8") as out:
                out.write(content)
            print(f"{filename} element modal updated via pattern2!")
        else:
            print(f"Could not find element modal in {filename}")
