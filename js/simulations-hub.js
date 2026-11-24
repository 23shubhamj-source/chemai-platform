/* ==========================================================================
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

  /* ==========================================================================
     2. MOLECULE SHAPES 3D (VSEPR THEORY)
     ========================================================================== */
  let vseprScene, vseprCamera, vseprRenderer, vseprGroup;

  function initVSEPR3D() {
    const container = document.getElementById("vseprCanvasContainer");
    if (!container || vseprRenderer) return;

    const width = container.clientWidth;
    const height = container.clientHeight;

    vseprScene = new THREE.Scene();
    vseprCamera = new THREE.PerspectiveCamera(45, width / height, 0.1, 100);
    vseprCamera.position.set(0, 0, 7);

    vseprRenderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    vseprRenderer.setSize(width, height);
    vseprRenderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));
    container.innerHTML = "";
    container.appendChild(vseprRenderer.domElement);

    const amb = new THREE.AmbientLight(0xffffff, 0.8);
    vseprScene.add(amb);

    const dir1 = new THREE.DirectionalLight(0xffffff, 0.9);
    dir1.position.set(5, 10, 7);
    vseprScene.add(dir1);

    vseprGroup = new THREE.Group();
    vseprScene.add(vseprGroup);

    let isDown = false;
    let prev = { x: 0, y: 0 };
    container.onmousedown = (e) => { isDown = true; prev = { x: e.clientX, y: e.clientY }; };
    window.addEventListener("mouseup", () => { isDown = false; });
    container.onmousemove = (e) => {
      if (!isDown || !vseprGroup) return;
      const dx = e.clientX - prev.x;
      const dy = e.clientY - prev.y;
      vseprGroup.rotation.y += dx * 0.01;
      vseprGroup.rotation.x += dy * 0.01;
      prev = { x: e.clientX, y: e.clientY };
    };

    function animate() {
      requestAnimationFrame(animate);
      if (vseprGroup && !isDown) vseprGroup.rotation.y += 0.005;
      vseprRenderer.render(vseprScene, vseprCamera);
    }
    animate();
    updateVSEPR();
  }

  window.updateVSEPR = function() {
    const bonds = parseInt(document.getElementById("vseprBondSlider")?.value || "4", 10);
    const lone = parseInt(document.getElementById("vseprLoneSlider")?.value || "0", 10);

    const bondValEl = document.getElementById("vseprBondVal");
    if (bondValEl) bondValEl.textContent = bonds;

    const loneValEl = document.getElementById("vseprLoneVal");
    if (loneValEl) loneValEl.textContent = lone;

    const totalSteric = bonds + lone;

    let geomName = "Tetrahedral", electronGeom = "Tetrahedral", angle = "109.5°", hyb = "sp³";
    if (totalSteric === 2) {
      electronGeom = "Linear"; hyb = "sp"; geomName = "Linear"; angle = "180°";
    } else if (totalSteric === 3) {
      electronGeom = "Trigonal Planar"; hyb = "sp²";
      geomName = lone === 0 ? "Trigonal Planar" : "Bent"; angle = lone === 0 ? "120°" : "~118°";
    } else if (totalSteric === 4) {
      electronGeom = "Tetrahedral"; hyb = "sp³";
      if (lone === 0) { geomName = "Tetrahedral"; angle = "109.5°"; }
      else if (lone === 1) { geomName = "Trigonal Pyramidal"; angle = "107°"; }
      else { geomName = "Bent"; angle = "104.5°"; }
    } else if (totalSteric === 5) {
      electronGeom = "Trigonal Bipyramidal"; hyb = "sp³d";
      if (lone === 0) { geomName = "Trigonal Bipyramidal"; angle = "90°, 120°"; }
      else if (lone === 1) { geomName = "Seesaw"; angle = "~88°, ~116°"; }
      else if (lone === 2) { geomName = "T-shaped"; angle = "~87.5°"; }
      else { geomName = "Linear"; angle = "180°"; }
    } else if (totalSteric >= 6) {
      electronGeom = "Octahedral"; hyb = "sp³d²";
      if (lone === 0) { geomName = "Octahedral"; angle = "90°, 180°"; }
      else if (lone === 1) { geomName = "Square Pyramidal"; angle = "~88°"; }
      else { geomName = "Square Planar"; angle = "90°"; }
    }

    const gEl = document.getElementById("vseprGeomName"); if (gEl) gEl.textContent = geomName;
    const egEl = document.getElementById("vseprElectronGeom"); if (egEl) egEl.textContent = electronGeom;
    const aEl = document.getElementById("vseprAngle"); if (aEl) aEl.textContent = angle;
    const hEl = document.getElementById("vseprHybridization"); if (hEl) hEl.textContent = hyb;

    if (!vseprGroup) return;
    while (vseprGroup.children.length > 0) vseprGroup.remove(vseprGroup.children[0]);

    // Central Atom
    const centerMat = new THREE.MeshPhongMaterial({ color: 0x3b82f6 });
    const centerGeo = new THREE.SphereGeometry(0.65, 32, 32);
    vseprGroup.add(new THREE.Mesh(centerGeo, centerMat));

    const positions = getVSEPRVectors(totalSteric);

    for (let i = 0; i < bonds && i < positions.length; i++) {
      const pos = positions[i].clone().multiplyScalar(2.0);
      const cylGeo = new THREE.CylinderGeometry(0.08, 0.08, 2.0, 16);
      const cylMat = new THREE.MeshPhongMaterial({ color: 0x94a3b8 });
      const cyl = new THREE.Mesh(cylGeo, cylMat);
      cyl.position.copy(pos.clone().multiplyScalar(0.5));
      cyl.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), pos.clone().normalize());
      vseprGroup.add(cyl);

      const ligMat = new THREE.MeshPhongMaterial({ color: 0x22c55e });
      const ligGeo = new THREE.SphereGeometry(0.42, 24, 24);
      const lig = new THREE.Mesh(ligGeo, ligMat);
      lig.position.copy(pos);
      vseprGroup.add(lig);
    }

    for (let j = 0; j < lone && (bonds + j) < positions.length; j++) {
      const pos = positions[bonds + j].clone().multiplyScalar(1.6);
      const loneMat = new THREE.MeshPhongMaterial({ color: 0xfacc15, transparent: true, opacity: 0.6 });
      const loneGeo = new THREE.SphereGeometry(0.35, 16, 16);
      const loneMesh = new THREE.Mesh(loneGeo, loneMat);
      loneMesh.position.copy(pos);
      vseprGroup.add(loneMesh);
    }
  };

  function getVSEPRVectors(n) {
    if (n === 2) return [new THREE.Vector3(1, 0, 0), new THREE.Vector3(-1, 0, 0)];
    if (n === 3) return [
      new THREE.Vector3(0, 1, 0),
      new THREE.Vector3(Math.cos(-Math.PI/6), Math.sin(-Math.PI/6), 0),
      new THREE.Vector3(Math.cos(-5*Math.PI/6), Math.sin(-5*Math.PI/6), 0)
    ];
    if (n === 4) return [
      new THREE.Vector3(1, 1, 1).normalize(), new THREE.Vector3(-1, -1, 1).normalize(),
      new THREE.Vector3(-1, 1, -1).normalize(), new THREE.Vector3(1, -1, -1).normalize()
    ];
    if (n === 5) return [
      new THREE.Vector3(0, 1, 0), new THREE.Vector3(0, -1, 0),
      new THREE.Vector3(1, 0, 0), new THREE.Vector3(-0.5, 0, 0.866),
      new THREE.Vector3(-0.5, 0, -0.866)
    ];
    return [
      new THREE.Vector3(1, 0, 0), new THREE.Vector3(-1, 0, 0),
      new THREE.Vector3(0, 1, 0), new THREE.Vector3(0, -1, 0),
      new THREE.Vector3(0, 0, 1), new THREE.Vector3(0, 0, -1)
    ];
  }

  /* ==========================================================================
     3. BONDING & ELECTRONEGATIVITY
     ========================================================================== */
  const ELEM_EN = { H: 2.20, C: 2.55, N: 3.04, O: 3.44, F: 3.98, Na: 0.93, Cl: 3.16, K: 0.82, Br: 2.96, Ca: 1.00 };

  window.updateBondingSim = function() {
    const e1 = document.getElementById("bondElem1Select")?.value || "H";
    const e2 = document.getElementById("bondElem2Select")?.value || "Cl";
    const en1 = ELEM_EN[e1] || 2.20;
    const en2 = ELEM_EN[e2] || 3.16;
    const diff = Math.abs(en1 - en2);

    const diffEl = document.getElementById("bondEnDiffDisplay"); if (diffEl) diffEl.textContent = diff.toFixed(2);
    let type = "Nonpolar Covalent", desc = "Equal sharing of electrons.";
    if (diff > 1.7) { type = "Ionic Bond"; desc = "Electron transfer from electropositive cation to electronegative anion."; }
    else if (diff >= 0.4) { type = "Polar Covalent Bond"; desc = "Asymmetric electron density producing partial dipole charges."; }

    const tEl = document.getElementById("bondTypeDisplay"); if (tEl) tEl.textContent = type;
    const dEl = document.getElementById("bondTypeDesc"); if (dEl) dEl.textContent = desc;

    const canvas = document.getElementById("bondingCloudCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const width = canvas.width = canvas.parentElement.clientWidth;
    const height = canvas.height = canvas.parentElement.clientHeight;
    ctx.clearRect(0, 0, width, height);

    const cx = width / 2, cy = height / 2;
    ctx.beginPath(); ctx.arc(cx - 90, cy, 32, 0, Math.PI * 2); ctx.fillStyle = "#3b82f6"; ctx.fill();
    ctx.fillStyle = "#fff"; ctx.font = "bold 15px Inter, sans-serif"; ctx.textAlign = "center";
    ctx.fillText(`${e1} (${en1})`, cx - 90, cy + 5);

    ctx.beginPath(); ctx.arc(cx + 90, cy, 32, 0, Math.PI * 2); ctx.fillStyle = "#ef4444"; ctx.fill();
    ctx.fillStyle = "#fff"; ctx.fillText(`${e2} (${en2})`, cx + 90, cy + 5);

    const shift = (en2 - en1) * 15;
    ctx.beginPath(); ctx.ellipse(cx + shift, cy, 75, 25, 0, 0, Math.PI * 2);
    ctx.fillStyle = "rgba(16, 185, 129, 0.25)"; ctx.fill();
    ctx.strokeStyle = "#10b981"; ctx.lineWidth = 2; ctx.stroke();
  };

  /* ==========================================================================
     4. AUFBAU SIMULATOR
     ========================================================================== */
  window.updateAufbauSim = function() {
    const z = parseInt(document.getElementById("aufbauZSlider")?.value || "6", 10);
    const zDisp = document.getElementById("aufbauZDisplay"); if (zDisp) zDisp.textContent = "Z = " + z;

    const orbitalCapacities = [
      { name: "1s", max: 2 }, { name: "2s", max: 2 }, { name: "2p", max: 6, boxes: 3 },
      { name: "3s", max: 2 }, { name: "3p", max: 6, boxes: 3 }, { name: "4s", max: 2 }, { name: "3d", max: 10, boxes: 5 }
    ];

    let remaining = z;
    let configStr = "";
    const container = document.getElementById("aufbauLevelsContainer");
    if (container) container.innerHTML = "";

    orbitalCapacities.forEach(orb => {
      const numBoxes = orb.boxes || 1;
      const count = Math.min(remaining, orb.max);
      remaining -= count;
      if (count > 0) configStr += `${orb.name}<sup>${count}</sup> `;

      let boxesHtml = "";
      for (let b = 0; b < numBoxes; b++) {
        let arrows = "";
        let inBox = 0;
        if (numBoxes === 1) inBox = count;
        else {
          if (count > b) inBox++;
          if (count > numBoxes + b) inBox++;
        }
        if (inBox === 1) arrows = "↑";
        else if (inBox === 2) arrows = "↑↓";
        boxesHtml += `<div class="orbital-box ${inBox > 0 ? 'occupied' : ''}">${arrows}</div>`;
      }

      if (container) {
        const row = document.createElement("div");
        row.className = "aufbau-level-row";
        row.innerHTML = `<span class="aufbau-label">${orb.name}</span><div class="orbital-boxes-group">${boxesHtml}</div>`;
        container.appendChild(row);
      }
    });

    const cfgEl = document.getElementById("aufbauConfigDisplay");
    if (cfgEl) cfgEl.innerHTML = configStr || "1s<sup>0</sup>";
  };

  /* ==========================================================================
     5. REACTION ENERGY DIAGRAM
     ========================================================================== */
  window.renderEnergyDiagram = function() {
    const canvas = document.getElementById("energyDiagramCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const width = canvas.width = canvas.parentElement.clientWidth;
    const height = canvas.height = canvas.parentElement.clientHeight;
    ctx.clearRect(0, 0, width, height);

    const ea = parseFloat(document.getElementById("energyEaInput")?.value || "60");
    const dh = parseFloat(document.getElementById("energyDhInput")?.value || "-30");
    const hasCat = document.getElementById("energyCatToggle")?.checked || false;

    const baseY = height - 60;
    const reactantY = baseY - 120;
    const productY = reactantY + (dh * 2);
    const tsY = reactantY - (ea * 2);
    const catTsY = reactantY - (ea * 1.3);

    ctx.strokeStyle = "rgba(255,255,255,0.2)"; ctx.lineWidth = 2;
    ctx.beginPath(); ctx.moveTo(50, 30); ctx.lineTo(50, baseY); ctx.lineTo(width - 40, baseY); ctx.stroke();

    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(60, reactantY); ctx.lineTo(130, reactantY); ctx.stroke();
    ctx.fillStyle = "#fff"; ctx.fillText("Reactants", 65, reactantY - 10);

    ctx.strokeStyle = "#f43f5e"; ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(130, reactantY);
    ctx.bezierCurveTo(width * 0.35, reactantY, width * 0.45, tsY, width * 0.5, tsY);
    ctx.bezierCurveTo(width * 0.55, tsY, width * 0.65, productY, width * 0.75, productY);
    ctx.stroke();

    if (hasCat) {
      ctx.strokeStyle = "#10b981"; ctx.setLineDash([5, 5]);
      ctx.beginPath();
      ctx.moveTo(130, reactantY);
      ctx.bezierCurveTo(width * 0.35, reactantY, width * 0.45, catTsY, width * 0.5, catTsY);
      ctx.bezierCurveTo(width * 0.55, catTsY, width * 0.65, productY, width * 0.75, productY);
      ctx.stroke();
      ctx.setLineDash([]);
      ctx.fillStyle = "#10b981";
      ctx.fillText("Catalyzed (Lower Ea)", width * 0.52, catTsY - 10);
    }

    ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
    ctx.beginPath(); ctx.moveTo(width * 0.75, productY); ctx.lineTo(width - 50, productY); ctx.stroke();
    ctx.fillStyle = "#fff"; ctx.fillText("Products", width * 0.78, productY - 10);
  };

  /* ==========================================================================
     6. LE CHATELIER
     ========================================================================== */
  window.updateLeChatelier = function() {
    const temp = parseInt(document.getElementById("leChatTempSlider")?.value || "400", 10);
    const press = parseFloat(document.getElementById("leChatPressSlider")?.value || "1.0");

    const tEl = document.getElementById("leChatTempVal"); if (tEl) tEl.textContent = temp + " K";
    const pEl = document.getElementById("leChatPressVal"); if (pEl) pEl.textContent = press.toFixed(1) + " atm";

    let shift = "Equilibrium Steady", shiftColor = "var(--color-emerald)";
    if (temp > 500 && press < 2.0) {
      shift = "Shift Left ← (Reactants N₂ & H₂ favored by endothermic reverse)";
      shiftColor = "var(--color-rose)";
    } else if (press >= 3.0 && temp <= 450) {
      shift = "Shift Right → (Product NH₃ favored by volume compression)";
      shiftColor = "var(--color-cyan)";
    }
    const res = document.getElementById("leChatShiftResult");
    if (res) { res.textContent = shift; res.style.color = shiftColor; }
  };

  /* ==========================================================================
     7. GAS LAWS
     ========================================================================== */
  function initGasSim() {
    const canvas = document.getElementById("gasSimCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const width = canvas.width = canvas.parentElement.clientWidth;
    const height = canvas.height = canvas.parentElement.clientHeight;

    const particles = [];
    for (let i = 0; i < 40; i++) {
      particles.push({
        x: 60 + Math.random() * (width - 120),
        y: 100 + Math.random() * (height - 180),
        vx: (Math.random() - 0.5) * 4,
        vy: (Math.random() - 0.5) * 4
      });
    }

    function loop() {
      if (activeSimTab !== "gas") return;
      ctx.clearRect(0, 0, width, height);

      const pistonY = 70;
      ctx.fillStyle = "rgba(100, 116, 139, 0.4)";
      ctx.fillRect(50, pistonY, width - 100, 20);

      ctx.strokeStyle = "#38bdf8"; ctx.lineWidth = 3;
      ctx.strokeRect(50, pistonY + 20, width - 100, height - 140);

      ctx.fillStyle = "#10b981";
      particles.forEach(p => {
        p.x += p.vx; p.y += p.vy;
        if (p.x < 55 || p.x > width - 55) p.vx *= -1;
        if (p.y < pistonY + 25 || p.y > height - 125) p.vy *= -1;
        ctx.beginPath(); ctx.arc(p.x, p.y, 4, 0, Math.PI * 2); ctx.fill();
      });
      requestAnimationFrame(loop);
    }
    loop();
  }

  /* ==========================================================================
     8. GALVANIC CELL
     ========================================================================== */
  function initGalvanicSim() {
    const canvas = document.getElementById("galvanicSimCanvas");
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    const width = canvas.width = canvas.parentElement.clientWidth;
    const height = canvas.height = canvas.parentElement.clientHeight;
    ctx.clearRect(0, 0, width, height);

    ctx.fillStyle = "rgba(59, 130, 246, 0.2)"; ctx.fillRect(80, 150, 160, 180);
    ctx.strokeStyle = "#3b82f6"; ctx.strokeRect(80, 150, 160, 180);

    ctx.fillStyle = "#94a3b8"; ctx.fillRect(140, 100, 35, 180);
    ctx.fillStyle = "#fff"; ctx.fillText("Zn Anode (-)", 130, 90);

    ctx.fillStyle = "rgba(16, 185, 129, 0.2)"; ctx.fillRect(width - 240, 150, 160, 180);
    ctx.strokeStyle = "#10b981"; ctx.strokeRect(width - 240, 150, 160, 180);

    ctx.fillStyle = "#f97316"; ctx.fillRect(width - 180, 100, 35, 180);
    ctx.fillStyle = "#fff"; ctx.fillText("Cu Cathode (+)", width - 195, 90);

    ctx.strokeStyle = "#facc15"; ctx.lineWidth = 3;
    ctx.beginPath();
    ctx.moveTo(157, 100); ctx.lineTo(157, 40); ctx.lineTo(width - 162, 40); ctx.lineTo(width - 162, 100);
    ctx.stroke();

    const vx = width / 2;
    ctx.beginPath(); ctx.arc(vx, 40, 28, 0, Math.PI * 2); ctx.fillStyle = "#0f172a"; ctx.fill();
    ctx.strokeStyle = "#10b981"; ctx.stroke();
    ctx.fillStyle = "#10b981"; ctx.font = "bold 13px Inter, sans-serif"; ctx.textAlign = "center";
    ctx.fillText("1.10 V", vx, 45);

    ctx.fillStyle = "rgba(255, 255, 255, 0.25)";
    ctx.fillRect(200, 130, width - 400, 30);
    ctx.fillRect(200, 130, 30, 120);
    ctx.fillRect(width - 230, 130, 30, 120);
    ctx.fillStyle = "#fff"; ctx.fillText("KNO3 Salt Bridge", width / 2, 120);
  }

  /* ==========================================================================
     9. SOLUBILITY
     ========================================================================== */
  window.testPrecipitation = function() {
    const cation = document.getElementById("solCationSelect")?.value || "Ag+";
    const anion = document.getElementById("solAnionSelect")?.value || "Cl-";

    let ppt = "No precipitate (Soluble aqueous ions)";
    let pptColor = "var(--color-emerald)";

    if (cation === "Ag+" && anion === "Cl-") {
      ppt = "White Precipitate formed! AgCl (s) (Ksp = 1.8 × 10⁻¹⁰)";
      pptColor = "var(--color-rose)";
    } else if (cation === "Pb2+" && anion === "I-") {
      ppt = "Bright Yellow Precipitate formed! PbI₂ (s) (Ksp = 9.8 × 10⁻⁹)";
      pptColor = "var(--color-amber)";
    } else if (cation === "Ba2+" && anion === "SO42-") {
      ppt = "Dense White Precipitate formed! BaSO₄ (s) (Ksp = 1.1 × 10⁻¹⁰)";
      pptColor = "var(--color-rose)";
    }

    const out = document.getElementById("solPptResult");
    if (out) { out.textContent = ppt; out.style.color = pptColor; }
  };

  window.addEventListener("DOMContentLoaded", () => {
    initBuildMolecule();
  });
})();
