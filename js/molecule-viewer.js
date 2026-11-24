/* ==========================================================================
   ChemAI Platform - Advanced 3D Molecular Visualization Engine
   Full interactive 3D rendering with 85+ validated molecules dataset
   Ball-and-Stick, Stick, Space-Filling, Atom Labels, Search & Filters
   ========================================================================== */

(function initAdvancedMoleculeViewer() {
  const CPK_COLORS = {
    H: 0xffffff,
    C: 0x334155,
    N: 0x3b82f6,
    O: 0xef4444,
    S: 0xfacc15,
    P: 0xf97316,
    F: 0x22c55e,
    Cl: 0x10b981,
    Br: 0x991b1b,
    I: 0x7c3aed,
    Na: 0x8b5cf6,
    K: 0x9333ea,
    Ca: 0x64748b,
    Mg: 0x14b8a6,
    Fe: 0xeab308,
    Cu: 0xf97316,
    Zn: 0x06b6d4,
    Ag: 0xd1d5db,
    Al: 0x94a3b8,
    Si: 0xca8a04,
    B: 0xf43f5e,
    Mn: 0xa855f7
  };

  const VDW_RADII = {
    H: 0.42,
    C: 0.78,
    N: 0.74,
    O: 0.72,
    F: 0.70,
    P: 0.88,
    S: 0.88,
    Cl: 0.86,
    Br: 0.94,
    I: 1.02,
    Na: 1.02,
    K: 1.25,
    Ca: 1.10,
    Mg: 0.95,
    Fe: 0.95,
    Cu: 0.90,
    Zn: 0.92,
    Ag: 1.05,
    Al: 0.90,
    Si: 0.88,
    B: 0.78,
    Mn: 0.92
  };

  let moleculesList = [];
  let currentMolId = "water";
  let displayMode = "ballStick"; // ballStick, stick, spaceFill
  let showAtomLabels = false;
  let autoRotate = true;
  let activeCategory = "all";
  let searchQuery = "";
  let sortBy = "name-asc";

  let scene, camera, renderer, molGroup, labelGroup;
  let isDragging = false;
  let isPanning = false;
  let previousMousePos = { x: 0, y: 0 };

  // Load molecules dataset
  function loadMolecules() {
    if (window.CHEMAI_MOLECULES && Array.isArray(window.CHEMAI_MOLECULES) && window.CHEMAI_MOLECULES.length > 0) {
      moleculesList = window.CHEMAI_MOLECULES;
    } else {
      moleculesList = [
        {
          id: "water", name: "Water", formula: "H₂O", commonName: "Dihydrogen Monoxide",
          category: "Simple Molecules", categoryKey: "simple", mw: "18.015 g/mol",
          geometry: "Bent (~104.5°)", bondAngles: "104.45°", bondTypes: "Polar covalent σ bonds",
          numAtoms: 3, numBonds: 2, hybridization: "sp³", polarity: "Polar (μ = 1.85 D)",
          physicalProps: "Colorless liquid; mp 0°C, bp 100°C; density 1.00 g/cm³; specific heat 4.184 J/g·K.",
          chemicalProps: "Amphoteric; autoionizes Kw = 1.0 × 10⁻¹⁴; forms extensive hydrogen-bonding network.",
          uses: "Universal solvent in biological and chemical syntheses, industrial coolant, density standard.",
          facts: "Solid ice is less dense than liquid water due to hexagonal open lattice hydrogen bonding.",
          atoms: [{"el":"O","x":0.0,"y":0.0,"z":0.0},{"el":"H","x":-0.757,"y":0.586,"z":0.0},{"el":"H","x":0.757,"y":0.586,"z":0.0}],
          bonds: [[0,1,1],[0,2,1]]
        }
      ];
    }
  }

  function getFilteredMolecules() {
    return moleculesList.filter((m) => {
      const matchCat = activeCategory === "all" || m.categoryKey === activeCategory;
      const q = searchQuery.toLowerCase().trim();
      const matchSearch = !q ||
        m.name.toLowerCase().includes(q) ||
        m.formula.toLowerCase().includes(q) ||
        (m.commonName && m.commonName.toLowerCase().includes(q)) ||
        m.category.toLowerCase().includes(q);
      return matchCat && matchSearch;
    }).sort((a, b) => {
      if (sortBy === "name-asc") return a.name.localeCompare(b.name);
      if (sortBy === "name-desc") return b.name.localeCompare(a.name);
      const mwA = parseFloat(a.mw) || 0;
      const mwB = parseFloat(b.mw) || 0;
      if (sortBy === "mw-asc") return mwA - mwB;
      if (sortBy === "mw-desc") return mwB - mwA;
      return 0;
    });
  }

  function getCurrentMolecule() {
    return moleculesList.find((m) => m.id === currentMolId) || moleculesList[0];
  }

  // 3D Scene Initialization
  function initThreeScene() {
    const container = document.getElementById("molCanvasContainer");
    if (!container) return;

    const width = container.clientWidth || 600;
    const height = container.clientHeight || 540;

    if (typeof THREE === "undefined") {
      renderFallback(container);
      return;
    }

    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.set(0, 0, 8);

    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(Math.min(window.devicePixelRatio || 1, 2));

    container.innerHTML = "";
    container.appendChild(renderer.domElement);

    // Lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.75);
    scene.add(ambientLight);

    const dirLight1 = new THREE.DirectionalLight(0xffffff, 0.85);
    dirLight1.position.set(6, 12, 8);
    scene.add(dirLight1);

    const dirLight2 = new THREE.DirectionalLight(0x00b4d8, 0.45);
    dirLight2.position.set(-6, -6, -6);
    scene.add(dirLight2);

    molGroup = new THREE.Group();
    labelGroup = new THREE.Group();
    scene.add(molGroup);
    scene.add(labelGroup);

    // Render current molecule
    renderMoleculeMesh(getCurrentMolecule());

    // Mouse & Touch Controls
    container.addEventListener("mousedown", (e) => {
      if (e.button === 2 || e.shiftKey) {
        isPanning = true;
      } else {
        isDragging = true;
      }
      previousMousePos = { x: e.clientX, y: e.clientY };
    });

    container.addEventListener("contextmenu", (e) => e.preventDefault());

    window.addEventListener("mouseup", () => {
      isDragging = false;
      isPanning = false;
    });

    container.addEventListener("mousemove", (e) => {
      if (!isDragging && !isPanning) return;
      const deltaX = e.clientX - previousMousePos.x;
      const deltaY = e.clientY - previousMousePos.y;

      if (isDragging && molGroup) {
        molGroup.rotation.y += deltaX * 0.008;
        molGroup.rotation.x += deltaY * 0.008;
        if (labelGroup) {
          labelGroup.rotation.y = molGroup.rotation.y;
          labelGroup.rotation.x = molGroup.rotation.x;
        }
      } else if (isPanning && camera) {
        camera.position.x -= deltaX * 0.01;
        camera.position.y += deltaY * 0.01;
      }

      previousMousePos = { x: e.clientX, y: e.clientY };
    });

    // Touch support for mobile devices
    container.addEventListener("touchstart", (e) => {
      if (e.touches.length === 1) {
        isDragging = true;
        previousMousePos = { x: e.touches[0].clientX, y: e.touches[0].clientY };
      }
    }, { passive: true });

    container.addEventListener("touchmove", (e) => {
      if (!isDragging || e.touches.length !== 1 || !molGroup) return;
      const deltaX = e.touches[0].clientX - previousMousePos.x;
      const deltaY = e.touches[0].clientY - previousMousePos.y;
      molGroup.rotation.y += deltaX * 0.008;
      molGroup.rotation.x += deltaY * 0.008;
      if (labelGroup) {
        labelGroup.rotation.y = molGroup.rotation.y;
        labelGroup.rotation.x = molGroup.rotation.x;
      }
      previousMousePos = { x: e.touches[0].clientX, y: e.touches[0].clientY };
    }, { passive: true });

    container.addEventListener("touchend", () => { isDragging = false; });

    // Wheel zoom
    container.addEventListener("wheel", (e) => {
      e.preventDefault();
      camera.position.z += e.deltaY * 0.005;
      camera.position.z = Math.max(2.5, Math.min(25, camera.position.z));
    }, { passive: false });

    // Window resize
    window.addEventListener("resize", () => {
      if (!container || !renderer || !camera) return;
      const nw = container.clientWidth;
      const nh = container.clientHeight;
      camera.aspect = nw / nh;
      camera.updateProjectionMatrix();
      renderer.setSize(nw, nh);
    });

    function animate() {
      requestAnimationFrame(animate);
      if (autoRotate && !isDragging && !isPanning && molGroup) {
        molGroup.rotation.y += 0.006;
        if (labelGroup) labelGroup.rotation.y = molGroup.rotation.y;
      }
      renderer.render(scene, camera);
    }
    animate();
  }

  // Create 2D Text Sprite for Atom Label
  function makeTextSprite(message) {
    const canvas = document.createElement("canvas");
    canvas.width = 128;
    canvas.height = 128;
    const ctx = canvas.getContext("2d");

    ctx.fillStyle = "rgba(6, 13, 26, 0.85)";
    ctx.beginPath();
    ctx.arc(64, 64, 48, 0, Math.PI * 2);
    ctx.fill();
    ctx.strokeStyle = "#10b981";
    ctx.lineWidth = 4;
    ctx.stroke();

    ctx.fillStyle = "#ffffff";
    ctx.font = "bold 52px monospace";
    ctx.textAlign = "center";
    ctx.textBaseline = "middle";
    ctx.fillText(message, 64, 64);

    const texture = new THREE.CanvasTexture(canvas);
    const spriteMaterial = new THREE.SpriteMaterial({ map: texture, depthTest: false });
    const sprite = new THREE.Sprite(spriteMaterial);
    sprite.scale.set(0.65, 0.65, 1);
    return sprite;
  }

  // Build 3D Molecular Geometry
  function renderMoleculeMesh(data) {
    if (!molGroup) return;

    while (molGroup.children.length > 0) {
      molGroup.remove(molGroup.children[0]);
    }
    if (labelGroup) {
      while (labelGroup.children.length > 0) {
        labelGroup.remove(labelGroup.children[0]);
      }
    }

    if (!data || !data.atoms) return;

    // Center of mass calculation to auto-center molecule
    let cx = 0, cy = 0, cz = 0;
    data.atoms.forEach((a) => { cx += a.x; cy += a.y; cz += a.z; });
    cx /= data.atoms.length;
    cy /= data.atoms.length;
    cz /= data.atoms.length;

    // Determine atom radius style
    data.atoms.forEach((atom, idx) => {
      const el = atom.el || "C";
      const color = CPK_COLORS[el] || 0xcccccc;

      let r = 0.35;
      if (displayMode === "spaceFill") {
        r = VDW_RADII[el] || 0.8;
      } else if (displayMode === "stick") {
        r = 0.16;
      } else {
        // Ball and stick
        r = (VDW_RADII[el] || 0.75) * 0.45;
        if (el === "H") r = 0.24;
      }

      const sphereGeom = new THREE.SphereGeometry(r, 32, 24);
      const mat = new THREE.MeshPhongMaterial({
        color,
        specular: 0x444444,
        shininess: 40
      });
      const atomMesh = new THREE.Mesh(sphereGeom, mat);
      const posX = atom.x - cx;
      const posY = atom.y - cy;
      const posZ = atom.z - cz;
      atomMesh.position.set(posX, posY, posZ);
      molGroup.add(atomMesh);

      // Labels
      if (showAtomLabels && labelGroup) {
        const sprite = makeTextSprite(el);
        sprite.position.set(posX, posY + r + 0.25, posZ);
        labelGroup.add(sprite);
      }
    });

    // Bonds
    if (displayMode !== "spaceFill" && data.bonds) {
      data.bonds.forEach((b) => {
        const idx1 = b[0];
        const idx2 = b[1];
        const order = b[2] || 1;
        const a1 = data.atoms[idx1];
        const a2 = data.atoms[idx2];
        if (!a1 || !a2) return;

        const p1 = new THREE.Vector3(a1.x - cx, a1.y - cy, a1.z - cz);
        const p2 = new THREE.Vector3(a2.x - cx, a2.y - cy, a2.z - cz);
        const dist = p1.distanceTo(p2);
        const bondRadius = displayMode === "stick" ? 0.08 : 0.07;

        if (order === 1) {
          const cylinder = new THREE.CylinderGeometry(bondRadius, bondRadius, dist, 16);
          const mat = new THREE.MeshPhongMaterial({ color: 0x94a3b8, shininess: 25 });
          const mesh = new THREE.Mesh(cylinder, mat);
          mesh.position.copy(p1.clone().add(p2).multiplyScalar(0.5));
          mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), p2.clone().sub(p1).normalize());
          molGroup.add(mesh);
        } else {
          // Multi-bond render (double or triple bond)
          const count = Math.min(order, 3);
          const offsetDist = 0.08;
          for (let k = 0; k < count; k++) {
            const shift = (k - (count - 1) / 2) * offsetDist;
            const cylinder = new THREE.CylinderGeometry(bondRadius * 0.8, bondRadius * 0.8, dist, 16);
            const mat = new THREE.MeshPhongMaterial({ color: 0x64748b, shininess: 25 });
            const mesh = new THREE.Mesh(cylinder, mat);
            const mid = p1.clone().add(p2).multiplyScalar(0.5);
            mesh.position.copy(mid).add(new THREE.Vector3(0, shift, 0));
            mesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), p2.clone().sub(p1).normalize());
            molGroup.add(mesh);
          }
        }
      });
    }

    updateUI(data);
  }

  // Update UI & Details Dashboard
  function updateUI(data) {
    if (!data) return;

    // HUD in canvas
    const hudFormula = document.getElementById("molHudFormula");
    const hudName = document.getElementById("molHudName");
    const hudCat = document.getElementById("molHudCat");
    if (hudFormula) hudFormula.textContent = data.formula;
    if (hudName) hudName.textContent = data.name;
    if (hudCat) hudCat.textContent = data.category;

    // Dashboard panel
    const dashTitle = document.getElementById("molDashTitle");
    const dashCommon = document.getElementById("molDashCommon");
    const dashFormula = document.getElementById("molDashFormula");
    const dashMw = document.getElementById("molDashMw");
    const dashGeom = document.getElementById("molDashGeom");
    const dashAngle = document.getElementById("molDashAngle");
    const dashHybrid = document.getElementById("molDashHybrid");
    const dashPolar = document.getElementById("molDashPolar");
    const dashCounts = document.getElementById("molDashCounts");
    const dashBondTypes = document.getElementById("molDashBondTypes");
    const dashPhysical = document.getElementById("molDashPhysical");
    const dashChemical = document.getElementById("molDashChemical");
    const dashUses = document.getElementById("molDashUses");
    const dashFacts = document.getElementById("molDashFacts");

    if (dashTitle) dashTitle.textContent = data.name;
    if (dashCommon) dashCommon.textContent = data.commonName ? `Common: ${data.commonName}` : "";
    if (dashFormula) dashFormula.textContent = data.formula;
    if (dashMw) dashMw.textContent = data.mw;
    if (dashGeom) dashGeom.textContent = data.geometry;
    if (dashAngle) dashAngle.textContent = data.bondAngles;
    if (dashHybrid) dashHybrid.textContent = data.hybridization;
    if (dashPolar) dashPolar.textContent = data.polarity;
    if (dashCounts) dashCounts.textContent = `${data.atoms.length} Atoms · ${data.bonds ? data.bonds.length : 0} Bonds`;
    if (dashBondTypes) dashBondTypes.textContent = data.bondTypes;
    if (dashPhysical) dashPhysical.textContent = data.physicalProps;
    if (dashChemical) dashChemical.textContent = data.chemicalProps;
    if (dashUses) dashUses.textContent = data.uses;
    if (dashFacts) dashFacts.textContent = data.facts;

    renderCarousel();
  }

  // Render bottom carousel / roster
  function renderCarousel() {
    const strip = document.getElementById("molCardsStrip");
    if (!strip) return;

    const filtered = getFilteredMolecules();
    strip.innerHTML = "";

    filtered.forEach((m) => {
      const card = document.createElement("button");
      card.type = "button";
      card.className = `mol-mini-card ${m.id === currentMolId ? "active" : ""}`;
      card.innerHTML = `
        <div class="mol-mini-formula">${m.formula}</div>
        <div class="mol-mini-name" title="${m.name}">${m.name}</div>
        <div class="mol-mini-cat">${m.category}</div>
      `;
      card.onclick = () => window.selectMoleculeById(m.id);
      strip.appendChild(card);
    });

    const counter = document.getElementById("molFilteredCount");
    if (counter) counter.textContent = `Showing ${filtered.length} of ${moleculesList.length} Molecules`;
  }

  function renderFallback(container) {
    const m = getCurrentMolecule();
    container.innerHTML = `
      <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;color:#94a3b8;text-align:center;padding:2rem;">
        <h3 style="color:#10b981;font-size:2rem;font-family:monospace;">${m.formula}</h3>
        <h4 style="margin-top:0.5rem;color:#e2e8f0;">${m.name}</h4>
        <p style="font-size:0.85rem;max-width:360px;margin-top:0.5rem;">${m.physicalProps}</p>
      </div>
    `;
    updateUI(m);
  }

  // Global Exposed Methods
  window.selectMoleculeById = function(id) {
    const mol = moleculesList.find((m) => m.id === id);
    if (mol) {
      currentMolId = id;
      if (molGroup) renderMoleculeMesh(mol);
      else renderFallback(document.getElementById("molCanvasContainer"));
    }
  };

  window.setMolDisplayMode = function(mode) {
    displayMode = mode;
    document.querySelectorAll(".mol-mode-btn").forEach((btn) => {
      btn.classList.toggle("active", btn.getAttribute("data-mode") === mode);
    });
    renderMoleculeMesh(getCurrentMolecule());
  };

  window.toggleMolLabels = function() {
    showAtomLabels = !showAtomLabels;
    const btn = document.getElementById("molToggleLabelsBtn");
    if (btn) btn.classList.toggle("active", showAtomLabels);
    renderMoleculeMesh(getCurrentMolecule());
  };

  window.toggleMolAutoRotate = function() {
    autoRotate = !autoRotate;
    const btn = document.getElementById("molToggleAutoRotateBtn");
    if (btn) btn.classList.toggle("active", autoRotate);
  };

  window.resetMolCamera = function() {
    if (camera && molGroup) {
      camera.position.set(0, 0, 8);
      molGroup.rotation.set(0, 0, 0);
      if (labelGroup) labelGroup.rotation.set(0, 0, 0);
    }
  };

  window.filterMoleculesCategory = function(catKey) {
    activeCategory = catKey;
    document.querySelectorAll(".mol-category-pill").forEach((pill) => {
      pill.classList.toggle("active", pill.getAttribute("data-category") === catKey);
    });
    renderCarousel();
  };

  window.handleMoleculeSearch = function(query) {
    searchQuery = query;
    renderCarousel();
  };

  window.handleMoleculeSort = function(sortValue) {
    sortBy = sortValue;
    renderCarousel();
  };

  window.addEventListener("DOMContentLoaded", () => {
    loadMolecules();
    initThreeScene();
    renderCarousel();
  });
})();
