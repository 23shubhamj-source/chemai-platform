/* ==========================================================================
   ChemAI Platform - 3D Molecular Visualization Engine
   Renders Ball-and-Stick & Space-filling 3D molecules with Three.js / Canvas
   ========================================================================== */

(function initMoleculeViewer() {
  const CPK_COLORS = {
    H: 0xffffff,
    C: 0x334155,
    N: 0x3b82f6,
    O: 0xef4444,
    S: 0xfacc15,
    P: 0xf97316,
    Cl: 0x10b981,
    Br: 0x991b1b,
    I: 0x7c3aed
  };

  const MOLECULES = {
    water: {
      name: "Water",
      formula: "H₂O",
      mw: "18.015 g/mol",
      desc: "Universal polar solvent with high hydrogen bonding capacity.",
      atoms: [
        { el: "O", x: 0, y: 0, z: 0 },
        { el: "H", x: -0.757, y: 0.586, z: 0 },
        { el: "H", x: 0.757, y: 0.586, z: 0 }
      ],
      bonds: [[0, 1], [0, 2]]
    },
    methane: {
      name: "Methane",
      formula: "CH₄",
      mw: "16.043 g/mol",
      desc: "Simplest alkane and tetrahedral hydrocarbon (109.5° angles).",
      atoms: [
        { el: "C", x: 0, y: 0, z: 0 },
        { el: "H", x: 0.629, y: 0.629, z: 0.629 },
        { el: "H", x: -0.629, y: -0.629, z: 0.629 },
        { el: "H", x: -0.629, y: 0.629, z: -0.629 },
        { el: "H", x: 0.629, y: -0.629, z: -0.629 }
      ],
      bonds: [[0, 1], [0, 2], [0, 3], [0, 4]]
    },
    co2: {
      name: "Carbon Dioxide",
      formula: "CO₂",
      mw: "44.009 g/mol",
      desc: "Linear non-polar molecule with two C=O double bonds (180°).",
      atoms: [
        { el: "C", x: 0, y: 0, z: 0 },
        { el: "O", x: -1.16, y: 0, z: 0 },
        { el: "O", x: 1.16, y: 0, z: 0 }
      ],
      bonds: [[0, 1], [0, 2]]
    },
    ethanol: {
      name: "Ethanol",
      formula: "C₂H₅OH",
      mw: "46.069 g/mol",
      desc: "Primary alcohol with hydroxyl functional group.",
      atoms: [
        { el: "C", x: -0.75, y: -0.2, z: 0 },
        { el: "C", x: 0.75, y: -0.2, z: 0 },
        { el: "O", x: 1.4, y: 1.0, z: 0 },
        { el: "H", x: 2.3, y: 0.8, z: 0 },
        { el: "H", x: -1.1, y: -0.7, z: 0.89 },
        { el: "H", x: -1.1, y: -0.7, z: -0.89 },
        { el: "H", x: -1.1, y: 0.8, z: 0 },
        { el: "H", x: 1.1, y: -0.7, z: 0.89 },
        { el: "H", x: 1.1, y: -0.7, z: -0.89 }
      ],
      bonds: [[0, 1], [1, 2], [2, 3], [0, 4], [0, 5], [0, 6], [1, 7], [1, 8]]
    },
    benzene: {
      name: "Benzene",
      formula: "C₆H₆",
      mw: "78.114 g/mol",
      desc: "Planar aromatic ring with delocalized pi electron resonance.",
      atoms: [
        { el: "C", x: 1.39, y: 0, z: 0 },
        { el: "C", x: 0.695, y: 1.204, z: 0 },
        { el: "C", x: -0.695, y: 1.204, z: 0 },
        { el: "C", x: -1.39, y: 0, z: 0 },
        { el: "C", x: -0.695, y: -1.204, z: 0 },
        { el: "C", x: 0.695, y: -1.204, z: 0 },
        { el: "H", x: 2.47, y: 0, z: 0 },
        { el: "H", x: 1.235, y: 2.139, z: 0 },
        { el: "H", x: -1.235, y: 2.139, z: 0 },
        { el: "H", x: -2.47, y: 0, z: 0 },
        { el: "H", x: -1.235, y: -2.139, z: 0 },
        { el: "H", x: 1.235, y: -2.139, z: 0 }
      ],
      bonds: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [0, 6], [1, 7], [2, 8], [3, 9], [4, 10], [5, 11]]
    },
    caffeine: {
      name: "Caffeine",
      formula: "C₈H₁₀N₄O₂",
      mw: "194.19 g/mol",
      desc: "Central nervous system stimulant purine alkaloid.",
      atoms: [
        { el: "N", x: -1.0, y: 1.2, z: 0 },
        { el: "C", x: 0.3, y: 1.5, z: 0 },
        { el: "N", x: 1.2, y: 0.5, z: 0 },
        { el: "C", x: 0.8, y: -0.8, z: 0 },
        { el: "C", x: -0.6, y: -1.0, z: 0 },
        { el: "C", x: -1.5, y: 0.0, z: 0 },
        { el: "O", x: 0.6, y: 2.7, z: 0 },
        { el: "O", x: -2.7, y: 0.1, z: 0 },
        { el: "N", x: 1.8, y: -1.6, z: 0 },
        { el: "C", x: 0.9, y: -2.4, z: 0 },
        { el: "N", x: -0.4, y: -2.0, z: 0 },
        { el: "C", x: -1.9, y: 2.3, z: 0 },
        { el: "C", x: 2.6, y: 0.8, z: 0 },
        { el: "C", x: 3.2, y: -1.7, z: 0 }
      ],
      bonds: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [1, 6], [5, 7], [3, 8], [8, 9], [9, 10], [10, 4], [0, 11], [2, 12]]
    },
    aspirin: {
      name: "Aspirin",
      formula: "C₉H₈O₄",
      mw: "180.16 g/mol",
      desc: "Acetylsalicylic acid NSAID analgesic and antipyretic.",
      atoms: [
        { el: "C", x: -1.2, y: 0, z: 0 },
        { el: "C", x: -0.5, y: 1.2, z: 0 },
        { el: "C", x: 0.9, y: 1.2, z: 0 },
        { el: "C", x: 1.6, y: 0, z: 0 },
        { el: "C", x: 0.9, y: -1.2, z: 0 },
        { el: "C", x: -0.5, y: -1.2, z: 0 },
        { el: "C", x: 3.1, y: 0.0, z: 0 },
        { el: "O", x: 3.7, y: 1.1, z: 0 },
        { el: "O", x: 3.7, y: -1.1, z: 0 },
        { el: "O", x: 1.6, y: 2.3, z: 0 },
        { el: "C", x: 1.0, y: 3.5, z: 0 },
        { el: "O", x: -0.2, y: 3.6, z: 0 },
        { el: "C", x: 1.9, y: 4.7, z: 0 }
      ],
      bonds: [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 0], [3, 6], [6, 7], [6, 8], [2, 9], [9, 10], [10, 11], [10, 12]]
    }
  };

  let currentMol = "water";
  let displayMode = "ballStick"; // ballStick, spaceFill, wireframe
  let autoRotate = true;

  let scene, camera, renderer, molGroup;
  let isDragging = false;
  let previousMousePosition = { x: 0, y: 0 };

  function initThree() {
    const container = document.getElementById("molCanvasContainer");
    if (!container) return;

    const width = container.clientWidth || 600;
    const height = container.clientHeight || 520;

    if (typeof THREE === "undefined") {
      renderFallbackCanvas();
      return;
    }

    scene = new THREE.Scene();
    camera = new THREE.PerspectiveCamera(45, width / height, 0.1, 1000);
    camera.position.z = 8;

    renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
    renderer.setSize(width, height);
    renderer.setPixelRatio(window.devicePixelRatio || 1);

    container.innerHTML = "";
    container.appendChild(renderer.domElement);

    // Lights
    const ambientLight = new THREE.AmbientLight(0xffffff, 0.7);
    scene.add(ambientLight);

    const dirLight1 = new THREE.DirectionalLight(0xffffff, 0.8);
    dirLight1.position.set(5, 10, 7);
    scene.add(dirLight1);

    const dirLight2 = new THREE.DirectionalLight(0x3b82f6, 0.4);
    dirLight2.position.set(-5, -5, -5);
    scene.add(dirLight2);

    molGroup = new THREE.Group();
    scene.add(molGroup);

    buildMolecule(MOLECULES[currentMol]);

    // Mouse Controls
    container.addEventListener("mousedown", (e) => {
      isDragging = true;
      previousMousePosition = { x: e.clientX, y: e.clientY };
    });

    window.addEventListener("mouseup", () => { isDragging = false; });

    container.addEventListener("mousemove", (e) => {
      if (!isDragging || !molGroup) return;
      const deltaX = e.clientX - previousMousePosition.x;
      const deltaY = e.clientY - previousMousePosition.y;

      molGroup.rotation.y += deltaX * 0.01;
      molGroup.rotation.x += deltaY * 0.01;

      previousMousePosition = { x: e.clientX, y: e.clientY };
    });

    container.addEventListener("wheel", (e) => {
      e.preventDefault();
      camera.position.z += e.deltaY * 0.005;
      camera.position.z = Math.max(3, Math.min(20, camera.position.z));
    });

    function animate() {
      requestAnimationFrame(animate);
      if (autoRotate && !isDragging && molGroup) {
        molGroup.rotation.y += 0.008;
      }
      renderer.render(scene, camera);
    }
    animate();
  }

  function buildMolecule(data) {
    if (!molGroup) return;
    while (molGroup.children.length > 0) {
      molGroup.remove(molGroup.children[0]);
    }

    const sphereGeom = new THREE.SphereGeometry(displayMode === "spaceFill" ? 0.75 : 0.35, 32, 32);

    // Atoms
    data.atoms.forEach((atom) => {
      const color = CPK_COLORS[atom.el] || 0xcccccc;
      const mat = new THREE.MeshPhongMaterial({
        color,
        specular: 0x555555,
        shininess: 30,
        wireframe: displayMode === "wireframe"
      });
      const mesh = new THREE.Mesh(sphereGeom, mat);
      const scale = atom.el === "H" ? 0.7 : (atom.el === "C" ? 1.0 : (atom.el === "O" ? 0.95 : 1.1));
      mesh.scale.set(scale, scale, scale);
      mesh.position.set(atom.x, atom.y, atom.z);
      molGroup.add(mesh);
    });

    // Bonds
    if (displayMode !== "spaceFill" && data.bonds) {
      data.bonds.forEach(([i, j]) => {
        const a1 = data.atoms[i];
        const a2 = data.atoms[j];
        if (!a1 || !a2) return;

        const v1 = new THREE.Vector3(a1.x, a1.y, a1.z);
        const v2 = new THREE.Vector3(a2.x, a2.y, a2.z);
        const dist = v1.distanceTo(v2);

        const cylinderGeom = new THREE.CylinderGeometry(0.08, 0.08, dist, 16);
        const bondMat = new THREE.MeshPhongMaterial({ color: 0x94a3b8, shininess: 20 });
        const bondMesh = new THREE.Mesh(cylinderGeom, bondMat);

        const mid = v1.clone().add(v2).multiplyScalar(0.5);
        bondMesh.position.copy(mid);
        bondMesh.quaternion.setFromUnitVectors(new THREE.Vector3(0, 1, 0), v2.clone().sub(v1).normalize());

        molGroup.add(bondMesh);
      });
    }

    updateHUD(data);
  }

  function updateHUD(data) {
    const title = document.getElementById("molHudTitle");
    const formula = document.getElementById("molHudFormula");
    const mw = document.getElementById("molHudMw");
    const atoms = document.getElementById("molHudAtoms");
    const desc = document.getElementById("molHudDesc");

    if (title) title.textContent = data.name;
    if (formula) formula.textContent = data.formula;
    if (mw) mw.textContent = `Molar Mass: ${data.mw}`;
    if (atoms) atoms.textContent = `Atoms: ${data.atoms.length} · Bonds: ${data.bonds ? data.bonds.length : 0}`;
    if (desc) desc.textContent = data.desc;
  }

  function renderFallbackCanvas() {
    const container = document.getElementById("molCanvasContainer");
    if (!container) return;
    container.innerHTML = `
      <div style="display:flex;flex-direction:column;align-items:center;justify-content:center;height:100%;color:#94a3b8;text-align:center;padding:2rem;">
        <svg width="64" height="64" viewBox="0 0 24 24" fill="none" stroke="#10b981" stroke-width="1.5"><circle cx="12" cy="12" r="3"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><line x1="12" y1="9" x2="19" y2="7"/><line x1="12" y1="15" x2="5" y2="17"/></svg>
        <h4 style="margin-top:1rem;color:#e2e8f0;">3D Interactive Molecular Viewer</h4>
        <p style="font-size:0.85rem;max-width:340px;margin-top:0.5rem;">Viewing ${MOLECULES[currentMol].name} (${MOLECULES[currentMol].formula}). Connect to internet to load full WebGL shader mesh.</p>
      </div>
    `;
    updateHUD(MOLECULES[currentMol]);
  }

  window.setMoleculePreset = function(molKey) {
    if (MOLECULES[molKey]) {
      currentMol = molKey;
      if (scene) buildMolecule(MOLECULES[molKey]);
      else renderFallbackCanvas();
    }
  };

  window.setMolDisplayMode = function(mode) {
    displayMode = mode;
    document.querySelectorAll(".mol-mode-btn").forEach((btn) => {
      btn.classList.toggle("active", btn.getAttribute("data-mode") === mode);
    });
    if (scene) buildMolecule(MOLECULES[currentMol]);
  };

  window.toggleMolAutoRotate = function() {
    autoRotate = !autoRotate;
  };

  window.resetMolCamera = function() {
    if (camera && molGroup) {
      camera.position.set(0, 0, 8);
      molGroup.rotation.set(0, 0, 0);
    }
  };

  window.addEventListener("DOMContentLoaded", () => {
    initThree();
  });
})();
