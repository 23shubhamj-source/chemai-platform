part1 = """/* ==========================================================================
   ChemAI Platform - Virtual Chemistry Simulation Hub Engine
   Build-A-Molecule, VSEPR 3D Shapes, Bonding, Aufbau, Thermo, Gas & Cells
   ========================================================================== */

(function initSimulationHub() {
  let activeSimTab = "build";

  window.switchSimTab = function(tab) {
    activeSimTab = tab;
    document.querySelectorAll(".sim-nav-tab").forEach(btn => {
      btn.classList.toggle("active", btn.getAttribute("data-tab") === tab);
    });

    document.querySelectorAll(".sim-tab-pane").forEach(pane => {
      pane.style.display = pane.id === "simPane_" + tab ? "block" : "none";
    });

    if (tab === "build") initBuildMolecule();
    if (tab === "vsepr") initVSEPR3D();
    if (tab === "bonding") updateBondingSim();
    if (tab === "aufbau") updateAufbauSim();
    if (tab === "energy") renderEnergyDiagram();
    if (tab === "lechatelier") updateLeChatelier();
    if (tab === "gas") initGasSim();
    if (tab === "galvanic") initGalvanicSim();
    if (tab === "solubility") testPrecipitation();
  };

  const ATOM_VALENCIES = {
    H: { valency: 1, color: "#ffffff", radius: 14, name: "Hydrogen" },
    C: { valency: 4, color: "#475569", radius: 24, name: "Carbon" },
    O: { valency: 2, color: "#ef4444", radius: 22, name: "Oxygen" },
    N: { valency: 3, color: "#3b82f6", radius: 22, name: "Nitrogen" },
    Cl: { valency: 1, color: "#10b981", radius: 24, name: "Chlorine" },
    F: { valency: 1, color: "#22c55e", radius: 18, name: "Fluorine" },
    Br: { valency: 1, color: "#991b1b", radius: 26, name: "Bromine" },
    S: { valency: 2, color: "#eab308", radius: 24, name: "Sulfur" },
    P: { valency: 3, color: "#f97316", radius: 24, name: "Phosphorus" }
  };

  let buildAtoms = [];
  let buildBonds = [];
  let selectedAtomId = null;
  let currentPaletteSymbol = "C";
  let currentBondOrder = 1;
  let draggedAtom = null;

  function initBuildMolecule() {
    const canvas = document.getElementById("buildMolCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    canvas.width = canvas.parentElement.clientWidth;
    canvas.height = canvas.parentElement.clientHeight;

    if (buildAtoms.length === 0) loadBuildPreset("water");
    else renderBuildCanvas();

    canvas.onmousedown = (e) => {
      const rect = canvas.getBoundingClientRect();
      const mx = e.clientX - rect.left;
      const my = e.clientY - rect.top;

      const hit = buildAtoms.find(a => {
        const dx = a.x - mx;
        const dy = a.y - my;
        return Math.sqrt(dx*dx + dy*dy) <= a.radius + 6;
      });

      if (hit) {
        if (selectedAtomId !== null && selectedAtomId !== hit.id) {
          toggleBond(selectedAtomId, hit.id);
          selectedAtomId = null;
        } else {
          selectedAtomId = hit.id;
          draggedAtom = hit;
        }
      } else {
        const newId = Date.now() + Math.random();
        const conf = ATOM_VALENCIES[currentPaletteSymbol];
        buildAtoms.push({
          id: newId, symbol: currentPaletteSymbol,
          x: mx, y: my, radius: conf.radius, color: conf.color,
          targetValency: conf.valency
        });
        selectedAtomId = newId;
      }
      renderBuildCanvas();
    };

    canvas.onmousemove = (e) => {
      if (!draggedAtom) return;
      const rect = canvas.getBoundingClientRect();
      draggedAtom.x = e.clientX - rect.left;
      draggedAtom.y = e.clientY - rect.top;
      renderBuildCanvas();
    };

    window.onmouseup = () => { draggedAtom = null; };
  }

  function toggleBond(id1, id2) {
    const existing = buildBonds.find(b => (b.a1 === id1 && b.a2 === id2) || (b.a1 === id2 && b.a2 === id1));
    if (existing) {
      if (existing.order < 3) existing.order++;
      else buildBonds = buildBonds.filter(b => b !== existing);
    } else {
      buildBonds.push({ a1: id1, a2: id2, order: currentBondOrder });
    }
    renderBuildCanvas();
  }

  function renderBuildCanvas() {
    const canvas = document.getElementById("buildMolCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    buildBonds.forEach(b => {
      const a1 = buildAtoms.find(a => a.id === b.a1);
      const a2 = buildAtoms.find(a => a.id === b.a2);
      if (!a1 || !a2) return;
      ctx.strokeStyle = "rgba(255, 255, 255, 0.75)";
      ctx.lineWidth = b.order === 1 ? 3 : b.order === 2 ? 6 : 9;
      ctx.beginPath();
      ctx.moveTo(a1.x, a1.y);
      ctx.lineTo(a2.x, a2.y);
      ctx.stroke();
    });

    const atomBondCounts = {};
    buildAtoms.forEach(a => { atomBondCounts[a.id] = 0; });
    buildBonds.forEach(b => {
      if (atomBondCounts[b.a1] !== undefined) atomBondCounts[b.a1] += b.order;
      if (atomBondCounts[b.a2] !== undefined) atomBondCounts[b.a2] += b.order;
    });

    let allValenciesMet = true;
    let valencyIssues = [];

    buildAtoms.forEach(a => {
      const currentBonds = atomBondCounts[a.id] || 0;
      const isSatisfied = currentBonds === a.targetValency;
      if (!isSatisfied) {
        allValenciesMet = false;
        valencyIssues.push(a.symbol + " has " + currentBonds + "/" + a.targetValency + " bonds");
      }

      ctx.beginPath();
      ctx.arc(a.x, a.y, a.radius, 0, Math.PI * 2);
      ctx.fillStyle = a.color;
      ctx.fill();
      ctx.lineWidth = a.id === selectedAtomId ? 3 : 1.5;
      ctx.strokeStyle = isSatisfied ? "#10b981" : a.id === selectedAtomId ? "#38bdf8" : "#f43f5e";
      ctx.stroke();

      ctx.fillStyle = a.symbol === "H" ? "#0f172a" : "#ffffff";
      ctx.font = "bold 13px Inter, sans-serif";
      ctx.textAlign = "center";
      ctx.textBaseline = "middle";
      ctx.fillText(a.symbol, a.x, a.y);
    });

    const counts = {};
    buildAtoms.forEach(a => { counts[a.symbol] = (counts[a.symbol] || 0) + 1; });
    let formula = "";
    if (counts.C) formula += "C" + (counts.C > 1 ? counts.C : "");
    if (counts.H) formula += "H" + (counts.H > 1 ? counts.H : "");
    Object.keys(counts).sort().forEach(sym => {
      if (sym !== "C" && sym !== "H") formula += sym + (counts[sym] > 1 ? counts[sym] : "");
    });

    const formulaEl = document.getElementById("buildMolFormula");
    if (formulaEl) formulaEl.textContent = formula || "Empty Workspace";

    const statusEl = document.getElementById("buildMolStatus");
    if (statusEl) {
      if (buildAtoms.length === 0) {
        statusEl.textContent = "Click canvas to place atoms";
        statusEl.className = "chip";
      } else if (allValenciesMet) {
        statusEl.textContent = "✓ Stable Molecule (Valency Satisfied)";
        statusEl.className = "chip chip-emerald";
      } else {
        statusEl.textContent = "⚠ Incomplete: " + valencyIssues[0];
        statusEl.className = "chip chip-rose";
      }
    }
  }

  window.selectPaletteAtom = function(sym) {
    currentPaletteSymbol = sym;
    document.querySelectorAll(".atom-palette-btn").forEach(b => {
      b.classList.toggle("active", b.getAttribute("data-sym") === sym);
    });
  };

  window.setBuildBondOrder = function(order) {
    currentBondOrder = order;
    document.querySelectorAll(".bond-tool-btn").forEach(b => {
      b.classList.toggle("active", parseInt(b.getAttribute("data-order")) === order);
    });
  };

  window.clearBuildCanvas = function() {
    buildAtoms = [];
    buildBonds = [];
    selectedAtomId = null;
    renderBuildCanvas();
  };

  window.deleteSelectedBuildAtom = function() {
    if (!selectedAtomId) return;
    buildAtoms = buildAtoms.filter(a => a.id !== selectedAtomId);
    buildBonds = buildBonds.filter(b => b.a1 !== selectedAtomId && b.a2 !== selectedAtomId);
    selectedAtomId = null;
    renderBuildCanvas();
  };

  window.loadBuildPreset = function(name) {
    buildAtoms = [];
    buildBonds = [];
    selectedAtomId = null;
    const cx = 350, cy = 200;

    if (name === "water") {
      buildAtoms.push({ id: 1, symbol: "O", x: cx, y: cy, radius: 22, color: "#ef4444", targetValency: 2 });
      buildAtoms.push({ id: 2, symbol: "H", x: cx - 60, y: cy + 45, radius: 14, color: "#ffffff", targetValency: 1 });
      buildAtoms.push({ id: 3, symbol: "H", x: cx + 60, y: cy + 45, radius: 14, color: "#ffffff", targetValency: 1 });
      buildBonds.push({ a1: 1, a2: 2, order: 1 });
      buildBonds.push({ a1: 1, a2: 3, order: 1 });
    } else if (name === "methane") {
      buildAtoms.push({ id: 1, symbol: "C", x: cx, y: cy, radius: 24, color: "#475569", targetValency: 4 });
      [0, Math.PI/2, Math.PI, 3*Math.PI/2].forEach((rad, i) => {
        buildAtoms.push({ id: i+2, symbol: "H", x: cx + Math.cos(rad)*75, y: cy + Math.sin(rad)*75, radius: 14, color: "#ffffff", targetValency: 1 });
        buildBonds.push({ a1: 1, a2: i+2, order: 1 });
      });
    } else if (name === "carbon_dioxide") {
      buildAtoms.push({ id: 1, symbol: "C", x: cx, y: cy, radius: 24, color: "#475569", targetValency: 4 });
      buildAtoms.push({ id: 2, symbol: "O", x: cx - 90, y: cy, radius: 22, color: "#ef4444", targetValency: 2 });
      buildAtoms.push({ id: 3, symbol: "O", x: cx + 90, y: cy, radius: 22, color: "#ef4444", targetValency: 2 });
      buildBonds.push({ a1: 1, a2: 2, order: 2 });
      buildBonds.push({ a1: 1, a2: 3, order: 2 });
    }
    renderBuildCanvas();
  };
"""

with open("js/simulations-hub.js", "w", encoding="utf-8") as f:
    f.write(part1)
print("Wrote Part 1")
