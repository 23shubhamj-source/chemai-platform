# ChemAI Platform ⚗️ - AI-Powered Chemistry Web Suite

A premium, modern, fully responsive AI-powered chemistry platform inspired by the visual design, layout architecture, dark scientific theme, and feature organization of **[chemai.in](https://chemai.in/)**.

## 🌟 Key Features

### 1. Modern Dark Scientific Interface
- **Theme**: Deep navy `#0a192f` and charcoal backgrounds, glowing emerald (`#10b981`), electric cobalt (`#3b82f6`), amber (`#f59e0b`), and violet (`#8b5cf6`) accents.
- **Glassmorphism**: Translucent cards, subtle border glows, and glowing ambient light gradients.
- **Background**: Dynamic floating atoms and chemical bonds particle canvas.
- **Typography**: Inter for modern readability and JetBrains Mono for chemical equations and formulas.
- **Command Palette**: `Ctrl + K` quick search across all tools, calculators, elements, and simulations.

### 2. Conversational AI Chemistry Assistant
- Full conversational interface with conversation history and clear chat capabilities.
- Pre-loaded intelligent prompts:
  - *Balance this chemical equation*
  - *Explain chemical bonding (VSEPR, ionic, covalent, IMFs)*
  - *Calculate molar mass of hydrated compounds*
  - *Solve a stoichiometry problem with limiting reagents*
  - *Explain electrochemistry & Nernst equation*
  - *What is the difference between SN1 and SN2?*
- Visual OCR image problem upload simulation.
- Audio speech synthesis (Text-to-Speech) readout.

### 3. Scientific Chemistry Calculators (Real Algorithms)
- **Chemical Equation Balancer**: Solves algebraic mass conservation coefficients.
- **Molar Mass & Composition Calculator**: Recursive parser for parentheses and hydrates with elemental percentage bars.
- **Stoichiometry & Limiting Reagent Calculator**: Computes mole ratios and theoretical yields.
- **pH & pOH Calculator**: Interconverts pH, pOH, [H⁺], and [OH⁻] with dynamic color acidity bar.
- **Solution Dilution Calculator**: $M_1V_1 = M_2V_2$ solver.
- **Ideal Gas Law**: $PV = nRT$ solving for any variable.
- **Thermodynamics**: Gibbs free energy $\Delta G = \Delta H - T\Delta S$, spontaneity, and equilibrium constant $K$.
- **Percentage Yield Calculator**: Evaluates synthesis efficiency.
- **Electron Configuration**: Generates Aufbau sequences, noble gas condensations, and orbital blocks.

### 4. Interactive Periodic Table (118 Elements)
- Standard IUPAC 18-column × 7-period grid + detached Lanthanide & Actinide f-blocks.
- Real atomic masses, electronegativities, electron configurations, and applications.
- Real-time search and chemical category filters.
- Detailed element inspector drawer with Bohr electron shell model diagrams.

### 5. Dedicated Virtual Chemistry Lab
- Interactive laboratory workbench with apparatus:
  - **Acid-Base Titration**: Stopcock valve control, animated burette drops, Erlenmeyer flask phenolphthalein color transition, and real-time Canvas titration curve ($pH$ vs volume).
  - **Universal pH Indicator**: Colorimetric tests across the 0-14 pH scale.
  - **Precipitation Reactions**: Mixing ionic salts with net ionic equations ($AgCl\downarrow, PbI_2\downarrow, Cu(OH)_2\downarrow$).

### 6. 3D Molecular Structure Visualizer
- WebGL 3D molecular viewer with Ball-and-Stick, Space-Filling, and Wireframe modes.
- Orbit rotation, zoom, auto-spin toggle, and CPK standard atom coloring.
- Preloaded molecules: Water ($H_2O$), Methane ($CH_4$), Carbon Dioxide ($CO_2$), Ethanol ($C_2H_5OH$), Benzene ($C_6H_6$), Caffeine ($C_8H_{10}N_4O_2$), Aspirin ($C_9H_8O_4$).

### 7. Chemistry Study Hub
- **Quiz Generator**: Topic and difficulty filters, immediate explanation feedback, and final score evaluation.
- **AI Notes Generator**: Generates high-yield study revision sheets with one-click copy and print/PDF export.

### 8. Spectroscopy & Research Hub
- Diagnostic FT-IR wavenumber peak identifiers ($C=O, O-H, N-H, C\equiv C$).
- Laboratory GHS safety standards and risk classifications.

---

## 🚀 How to Run Locally

You can serve the directory using Python's built-in HTTP server:

```powershell
python -m http.server 8080 --directory "C:\Users\shubh\.gemini\antigravity\scratch\chemai-platform"
```

Then open your browser at:
`http://localhost:8080` (or open `index.html` directly).

---

## 📂 Project Architecture

```
chemai-platform/
├── index.html                   # Master platform page
├── virtual-lab.html             # Dedicated Virtual Lab workstation
├── periodic-table.html          # Dedicated IUPAC Periodic Table
├── tools.html                   # All-in-one Calculators Dashboard
├── study-hub.html               # Dedicated Study Hub & Quiz Engine
├── css/
│   ├── main.css                 # Theme variables, glassmorphism, animations
│   ├── components.css           # Chatbot, modals, calculator cards, search palette
│   ├── virtual-lab.css          # Apparatus, burette, test tubes, titration curve
│   ├── periodic-table.css       # IUPAC 18x7 grid, category color codes
│   └── molecule-viewer.css      # 3D canvas viewport, HUD overlay
└── js/
    ├── periodic-table-data.js   # 118 elements data with quantum properties
    ├── particles.js             # Canvas atom & bond background animation
    ├── calculators.js           # 10 mathematical chemistry calculators
    ├── periodic-table.js        # Periodic table rendering and Bohr drawer
    ├── virtual-lab.js           # 5 educational lab experiment simulations
    ├── molecule-viewer.js       # Three.js 3D molecular renderer
    ├── ai-assistant.js          # Conversational chatbot with step-by-step solver
    ├── quiz-engine.js           # Interactive multi-topic quiz generator
    ├── notes-generator.js       # AI study sheet & revision notes builder
    └── app.js                   # Master coordinator, typing hero, search palette
```
