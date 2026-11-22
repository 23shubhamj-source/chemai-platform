/* ==========================================================================
   ChemAI Platform - AI Chemistry Assistant Engine
   Intelligent problem solver, equation renderer & conversational tutor
   ========================================================================== */

(function initAIAssistant() {
  const KNOWLEDGE_BASE = [
    {
      keywords: ["balance", "equation", "reaction"],
      title: "Chemical Equation Balancing",
      response: `To balance a chemical equation, ensure the number of atoms of each element is equal on both sides according to the **Law of Conservation of Mass**:

<div class="chem-equation-box">4Fe (s) + 3O₂ (g) → 2Fe₂O₃ (s)</div>

<div class="step-box">
  <div class="step-box-title">Step 1: Count Initial Atoms</div>
  Reactants: Fe = 1, O = 2<br>
  Products: Fe = 2, O = 3
</div>

<div class="step-box">
  <div class="step-box-title">Step 2: Balance Oxygen First</div>
  LCM of 2 and 3 is 6. Add coefficient 3 to O₂ and 2 to Fe₂O₃:<br>
  <code>Fe + 3O₂ → 2Fe₂O₃</code>
</div>

<div class="step-box">
  <div class="step-box-title">Step 3: Balance Metal Atoms</div>
  Products now have 4 Fe. Add coefficient 4 to reactant Fe:<br>
  <strong class="text-emerald">Balanced: 4Fe + 3O₂ → 2Fe₂O₃ (ΔH° = -1648 kJ/mol)</strong>
</div>`
    },
    {
      keywords: ["sn1", "sn2", "nucleophilic", "substitution"],
      title: "SN1 vs SN2 Reaction Mechanisms",
      response: `Here is a side-by-side comparison of **S<sub>N</sub>1** and **S<sub>N</sub>2** nucleophilic substitution:

<table class="element-props-table" style="margin: 0.75rem 0;">
  <thead>
    <tr style="color: var(--color-emerald); border-bottom: 1px solid var(--border-subtle);">
      <th style="text-align: left; padding: 4px 0;">Property</th>
      <th style="text-align: left;">S<sub>N</sub>1</th>
      <th style="text-align: left;">S<sub>N</sub>2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Mechanism</td><td>Two steps (Carbocation intermediate)</td><td>One step (Concerted transition state)</td></tr>
    <tr><td>Kinetics</td><td>First order: Rate = k[R-X]</td><td>Second order: Rate = k[R-X][Nu⁻]</td></tr>
    <tr><td>Substrate</td><td>3° > 2° >> 1° (Steric stability)</td><td>CH₃ > 1° > 2° >> 3° (Steric hindrance)</td></tr>
    <tr><td>Stereochemistry</td><td>Racemization (inversion + retention)</td><td>Complete Walden Inversion (100% backside attack)</td></tr>
    <tr><td>Solvent</td><td>Polar protic (H₂O, EtOH, MeOH stabilizes carbocation)</td><td>Polar aprotic (Acetone, DMSO, DMF maximizes Nu⁻ nucleophilicity)</td></tr>
  </tbody>
</table>`
    },
    {
      keywords: ["bond", "bonding", "covalent", "ionic"],
      title: "Chemical Bonding Principles",
      response: `Chemical bonds form to achieve stable low-energy octet electron configurations:

<div class="step-box">
  <div class="step-box-title">1. Ionic Bonding (ΔEN > 1.7)</div>
  Complete transfer of valence electrons from an electropositive metal to an electronegative nonmetal.<br>
  Example: <strong>Na (3s¹) + Cl (3p⁵) → Na⁺ [Ne] + Cl⁻ [Ar]</strong> forming a 3D crystal lattice.
</div>

<div class="step-box">
  <div class="step-box-title">2. Covalent Bonding (ΔEN < 1.7)</div>
  Valence electron sharing between nonmetals. Single (σ), double (σ + π), and triple (σ + 2π) bonds.<br>
  Example: <strong>H₂O</strong> (sp³ hybridized, 104.5° bent geometry due to two lone pairs).
</div>

<div class="step-box">
  <div class="step-box-title">3. Intermolecular Forces (IMFs)</div>
  London Dispersion < Dipole-Dipole < Hydrogen Bonding (H bonded to N, O, or F).
</div>`
    },
    {
      keywords: ["molar", "mass", "molecular", "weight"],
      title: "Molar Mass Determination",
      response: `Molar mass ($M$) represents the mass in grams of one mole ($6.022 \\times 10^{23}$) of particles.

For hydrated copper sulfate <strong>CuSO₄ · 5H₂O</strong>:
<ul>
  <li>Cu: 1 × 63.546 = 63.546 g/mol</li>
  <li>S: 1 × 32.060 = 32.060 g/mol</li>
  <li>O: (4 + 5) × 15.999 = 143.991 g/mol</li>
  <li>H: (5 × 2) × 1.008 = 10.080 g/mol</li>
</ul>
<div class="chem-equation-box">Total Molar Mass = 249.677 g/mol</div>
Elemental Composition: <strong>57.67% Oxygen, 25.45% Copper, 12.84% Sulfur, 4.04% Hydrogen</strong>.`
    },
    {
      keywords: ["stoichiometry", "limiting", "reagent", "yield"],
      title: "Stoichiometry & Limiting Reagents",
      response: `Stoichiometry relates mole quantities of reactants and products:

<div class="step-box">
  <div class="step-box-title">Example Problem</div>
  How much water is produced when <strong>16.0 g of O₂</strong> reacts with <strong>4.0 g of H₂</strong>?<br>
  Reaction: <code>2H₂ + O₂ → 2H₂O</code>
</div>

<div class="step-box">
  <div class="step-box-title">Step 1: Convert Grams to Moles</div>
  Moles H₂ = 4.0 g / 2.016 g/mol = <strong>1.984 mol</strong><br>
  Moles O₂ = 16.0 g / 31.998 g/mol = <strong>0.500 mol</strong>
</div>

<div class="step-box">
  <div class="step-box-title">Step 2: Determine Limiting Reagent</div>
  1 mol O₂ requires 2 mol H₂. So 0.500 mol O₂ requires 1.00 mol H₂.<br>
  Since we have 1.984 mol H₂, <strong>O₂ is the limiting reagent</strong>.
</div>

<div class="step-box">
  <div class="step-box-title">Step 3: Theoretical Yield</div>
  Moles H₂O formed = 2 × 0.500 mol = 1.00 mol H₂O<br>
  <strong class="text-emerald">Mass H₂O = 1.00 mol × 18.015 g/mol = 18.02 grams</strong>
</div>`
    },
    {
      keywords: ["electrochemistry", "nernst", "galvanic", "redox"],
      title: "Electrochemistry & Galvanic Cells",
      response: `Electrochemistry bridges electrical potential and chemical free energy:

<div class="chem-equation-box">ΔG° = -n F E°cell</div>

<div class="step-box">
  <div class="step-box-title">Daniell Cell Example</div>
  <strong>Anode (Oxidation):</strong> Zn (s) → Zn²⁺ (aq) + 2e⁻ (E° = +0.76 V)<br>
  <strong>Cathode (Reduction):</strong> Cu²⁺ (aq) + 2e⁻ → Cu (s) (E° = +0.34 V)<br>
  <span class="text-emerald">E°cell = E°cathode - E°anode = 0.34 - (-0.76) = <strong>+1.10 V</strong></span>
</div>

<div class="step-box">
  <div class="step-box-title">Nernst Equation (Non-Standard Conditions)</div>
  <code>E = E° - (0.0592 / n) · log₁₀(Q) at 298 K</code><br>
  When reaction reaches equilibrium: Q = K and E = 0.
</div>`
    }
  ];

  let chatHistory = [];

  function appendMessage(sender, htmlContent) {
    const container = document.getElementById("chatMessagesArea");
    if (!container) return;

    const msg = document.createElement("div");
    msg.className = `chat-message ${sender}`;

    const avatar = document.createElement("div");
    avatar.className = "chat-avatar";
    avatar.innerHTML = sender === "bot" ? "AI" : "You";

    const bubble = document.createElement("div");
    bubble.className = "chat-bubble";
    bubble.innerHTML = htmlContent;

    msg.appendChild(avatar);
    msg.appendChild(bubble);
    container.appendChild(msg);

    container.scrollTop = container.scrollHeight;
  }

  function generateAIResponse(query) {
    const lower = query.toLowerCase().trim();

    // Check pre-computed knowledge base
    for (const item of KNOWLEDGE_BASE) {
      if (item.keywords.some((k) => lower.includes(k))) {
        return item.response;
      }
    }

    // Check element lookup
    if (window.PERIODIC_TABLE_DATA) {
      const el = window.PERIODIC_TABLE_DATA.find(
        (e) => lower.includes(e.name.toLowerCase()) || lower.split(" ").includes(e.sym.toLowerCase())
      );
      if (el) {
        return `Here is information on <strong>${el.name} (${el.sym})</strong>:
<ul>
  <li><strong>Atomic Number:</strong> ${el.num}</li>
  <li><strong>Atomic Mass:</strong> ${el.mass} u</li>
  <li><strong>Category:</strong> ${el.cat.replace(/-/g, " ").toUpperCase()}</li>
  <li><strong>Electron Configuration:</strong> ${el.config}</li>
  <li><strong>Electronegativity:</strong> ${el.en || "N/A"}</li>
  <li><strong>Standard State:</strong> ${el.state}</li>
  <li><strong>Key Applications:</strong> ${el.uses}</li>
</ul>`;
      }
    }

    // Default intelligent tutor fallback
    return `I received your chemistry question: "<em>${query}</em>"

To explore this concept in detail:
<ul>
  <li><strong>Key Principle:</strong> Chemistry reactions proceed toward lower enthalpy (ΔH < 0) and higher system entropy (ΔS > 0).</li>
  <li><strong>Interactive Tools:</strong> You can model this in the <a href="#tools" class="text-emerald">Tools Dashboard</a> or run a live simulation in the <a href="#virtual-lab" class="text-emerald">Virtual Chemistry Lab</a>.</li>
  <li><strong>Next step:</strong> Try asking about specific reaction equations, bonding geometries, or pH calculations.</li>
</ul>`;
  }

  window.handleChatSubmit = function(e) {
    if (e) e.preventDefault();
    const input = document.getElementById("chatUserInput");
    if (!input) return;
    const text = input.value.trim();
    if (!text) return;

    appendMessage("user", text);
    input.value = "";

    // Show typing status indicator
    setTimeout(() => {
      const responseHtml = generateAIResponse(text);
      appendMessage("bot", responseHtml);
    }, 400);
  };

  window.sendQuickPrompt = function(promptText) {
    appendMessage("user", promptText);
    setTimeout(() => {
      const responseHtml = generateAIResponse(promptText);
      appendMessage("bot", responseHtml);
    }, 350);
  };

  window.clearChatHistory = function() {
    const container = document.getElementById("chatMessagesArea");
    if (container) {
      container.innerHTML = `
        <div class="chat-message bot">
          <div class="chat-avatar">AI</div>
          <div class="chat-bubble">
            <p><strong>Hello! I am ChemAI, your intelligent chemistry assistant.</strong></p>
            <p>I can help you balance equations, analyze 3D molecules, compute molar masses, solve stoichiometry, and guide virtual experiments. What would you like to explore today?</p>
          </div>
        </div>
      `;
    }
  };

  // Text-To-Speech Reader
  window.speakLastMessage = function() {
    if (!("speechSynthesis" in window)) {
      alert("Text-to-speech is not supported on this browser.");
      return;
    }
    const bubbles = document.querySelectorAll(".bot .chat-bubble");
    if (bubbles.length === 0) return;
    const lastText = bubbles[bubbles.length - 1].innerText;
    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(lastText);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;
    window.speechSynthesis.speak(utterance);
  };

  // Image Upload Analysis Simulation
  window.triggerImageUpload = function() {
    const input = document.getElementById("chatImageUploadInput");
    if (input) input.click();
  };

  window.handleImageSelected = function(event) {
    const file = event.target.files[0];
    if (!file) return;

    appendMessage("user", `<svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" style="vertical-align:middle;margin-right:6px;"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg> Uploaded image: <em>${file.name}</em>`);

    setTimeout(() => {
      appendMessage("bot", `
<div class="step-box">
  <div class="step-box-title">📷 Visual OCR Chemistry Problem Solved</div>
  Detected Equation: <strong>Fe₂O₃ + 3CO → 2Fe + 3CO₂</strong><br>
  Process: <strong>Blast Furnace Blast Reduction of Hematite Iron Ore</strong><br>
  Redox Analysis: Iron is reduced from Fe(III) to Fe(0); Carbon is oxidized from C(+2) to C(+4).
</div>`);
    }, 600);
  };

  window.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("chatForm");
    if (form) form.addEventListener("submit", window.handleChatSubmit);

    const clearBtn = document.getElementById("chatClearBtn");
    if (clearBtn) clearBtn.addEventListener("click", window.clearChatHistory);

    const ttsBtn = document.getElementById("chatTtsBtn");
    if (ttsBtn) ttsBtn.addEventListener("click", window.speakLastMessage);
  });
})();
