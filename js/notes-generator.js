/* ==========================================================================
   ChemAI Platform - AI Chemistry Notes Generator
   ========================================================================== */

(function initNotesGenerator() {
  const NOTES_TEMPLATES = {
    bonding: {
      title: "Chemical Bonding and Molecular Geometry",
      level: "AP / Undergraduate Chemistry",
      sections: [
        {
          heading: "1. Fundamental Bonding Concepts",
          body: "Chemical bonding represents the thermodynamic stabilization achieved when atoms share or transfer valence electrons to minimize electrostatic potential energy. Governed by Coulomb's law and quantum mechanical orbital overlap."
        },
        {
          heading: "2. Key Formulas & Equations",
          body: `<ul>
            <li><strong>Lattice Energy (Born-Landé):</strong> U₀ = - (N_A · M · z⁺ · z⁻ · e²) / (4πε₀r₀) · (1 - 1/n)</li>
            <li><strong>Formal Charge:</strong> FC = Valence e⁻ - Nonbonding e⁻ - 1/2(Bonding e⁻)</li>
            <li><strong>Dipole Moment:</strong> μ = Q · r (Debye units, 1 D = 3.336 × 10⁻³⁰ C·m)</li>
          </ul>`
        },
        {
          heading: "3. Molecular Geometry (VSEPR Theory)",
          body: `<ul>
            <li><strong>AX₂:</strong> Linear (180°), e.g., BeCl₂, CO₂</li>
            <li><strong>AX₃:</strong> Trigonal Planar (120°), e.g., BF₃, SO₃</li>
            <li><strong>AX₄:</strong> Tetrahedral (109.5°), e.g., CH₄, CCl₄</li>
            <li><strong>AX₃E:</strong> Trigonal Pyramidal (107.5°), e.g., NH₃</li>
            <li><strong>AX₂E₂:</strong> Bent (104.5°), e.g., H₂O, H₂S</li>
          </ul>`
        },
        {
          heading: "4. Summary & High-Yield Exam Tips",
          body: "Always check for resonance structures and octet rule exceptions (incomplete octet: B, Be; expanded octet: P, S, Xe via low-lying d-orbitals). Electronegativity difference > 1.7 generally denotes predominantly ionic character."
        }
      ]
    },
    thermodynamics: {
      title: "Thermodynamics & Spontaneity",
      level: "Classes 11-12 & College Chemistry",
      sections: [
        {
          heading: "1. The Three Laws of Thermodynamics",
          body: "1st Law: Energy conservation (ΔU = q + w). 2nd Law: Total universe entropy increases for spontaneous processes (ΔS_univ > 0). 3rd Law: Entropy of a pure perfect crystalline substance is 0 at absolute zero (0 K)."
        },
        {
          heading: "2. Gibbs Free Energy (ΔG)",
          body: `<div class="chem-equation-box">ΔG = ΔH - T · ΔS</div>
          <ul>
            <li><strong>ΔG < 0:</strong> Spontaneous (Exergonic process)</li>
            <li><strong>ΔG = 0:</strong> System at dynamic chemical equilibrium</li>
            <li><strong>ΔG > 0:</strong> Non-spontaneous (Endergonic process)</li>
          </ul>`
        },
        {
          heading: "3. Equilibrium Link",
          body: "ΔG° = - R · T · ln(K_eq). When K_eq > 1, ΔG° is negative (products favored at standard state)."
        }
      ]
    },
    acids: {
      title: "Acids, Bases & Buffer Equilibria",
      level: "General Chemistry / CBSE / AP",
      sections: [
        {
          heading: "1. Definitions & Dissociation",
          body: "Arrhenius: H⁺ / OH⁻ producers in water. Brønsted-Lowry: Proton donor / acceptor. Lewis: Electron pair acceptor / donor."
        },
        {
          heading: "2. Quantitative Expressions",
          body: `<ul>
            <li><strong>pH:</strong> -log₁₀[H⁺]</li>
            <li><strong>pOH:</strong> -log₁₀[OH⁻]</li>
            <li><strong>Autoionization:</strong> Kw = [H⁺][OH⁻] = 1.0 × 10⁻¹⁴ (at 25°C)</li>
            <li><strong>Henderson-Hasselbalch:</strong> pH = pKa + log₁₀([A⁻] / [HA])</li>
          </ul>`
        }
      ]
    }
  };

  window.generateAINotes = function() {
    const topic = document.getElementById("notesTopicSelect")?.value || "bonding";
    const level = document.getElementById("notesLevelSelect")?.value || "AP Chemistry";

    const tmpl = NOTES_TEMPLATES[topic] || NOTES_TEMPLATES.bonding;
    const outputContainer = document.getElementById("notesOutputContent");
    if (!outputContainer) return;

    let html = `
      <div style="border-bottom: 2px solid var(--border-emerald); padding-bottom: 1rem; margin-bottom: 1.5rem;">
        <span class="chip chip-emerald" style="margin-bottom: 0.5rem;">Study Guide & Revision Sheet</span>
        <h2 style="font-size: 1.75rem; color: #fff; margin-top: 0.25rem;">${tmpl.title}</h2>
        <p style="color: var(--text-muted); font-size: 0.9rem;">Target Standard: <strong>${level}</strong> · Verified ChemAI Laboratory Curriculum</p>
      </div>
    `;

    tmpl.sections.forEach((sec) => {
      html += `
        <div style="margin-bottom: 1.5rem;">
          <h3 style="color: var(--color-emerald); font-size: 1.15rem; margin-bottom: 0.5rem;">${sec.heading}</h3>
          <div style="color: var(--text-main); font-size: 0.95rem; line-height: 1.6;">${sec.body}</div>
        </div>
      `;
    });

    outputContainer.innerHTML = html;
  };

  window.copyNotesToClipboard = function() {
    const content = document.getElementById("notesOutputContent")?.innerText;
    if (!content) return;

    navigator.clipboard.writeText(content).then(() => {
      alert("Study notes copied to clipboard!");
    });
  };

  window.printNotes = function() {
    window.print();
  };
})();
