js_code = r'''/* ==========================================================================
   ChemAI Platform - Upgraded 3D Interactive Periodic Table Controller
   Includes all 118 IUPAC elements with 3D tilt, Bohr shell model, and properties
   ========================================================================== */

(function initPeriodicTable() {
  const elements = window.PERIODIC_TABLE_DATA || [];
  let activeCategory = 'all';
  let searchTerm = '';
  let sortBy = 'num-asc';
  let bohrAnimFrame = null;
  let bohrAngle = 0;

  // Render 118-Element Periodic Grid
  function renderTable() {
    const grid = document.getElementById('ptableGrid');
    const fBlock = document.getElementById('ptableFBlock');
    if (!grid) return;

    grid.innerHTML = '';
    if (fBlock) fBlock.innerHTML = '';

    // Standard Layout: 7 periods x 18 groups
    const matrix = Array.from({ length: 7 }, () => Array(18).fill(null));

    elements.forEach((el) => {
      // f-block elements: Lanthanides (57-71) & Actinides (89-103)
      if ((el.num >= 57 && el.num <= 71) || (el.num >= 89 && el.num <= 103)) {
        return;
      }
      const r = el.per - 1;
      const c = el.grp - 1;
      if (r >= 0 && r < 7 && c >= 0 && c < 18) {
        matrix[r][c] = el;
      }
    });

    // Populate main 18x7 grid
    for (let r = 0; r < 7; r++) {
      for (let c = 0; c < 18; c++) {
        const el = matrix[r][c];
        if (el) {
          grid.appendChild(createElementCell(el));
        } else if (r === 5 && c === 2) {
          // Lanthanide placeholder 57-71
          const ph = document.createElement('div');
          ph.className = 'element-cell cat-lanthanide';
          ph.innerHTML = `
            <div class="cell-top"><span>57-71</span></div>
            <div class="cell-symbol" style="font-size:1.05rem;">La-Lu</div>
            <div class="cell-name">Lanthanoids</div>
          `;
          ph.onclick = () => window.filterPeriodicCategory('lanthanide');
          grid.appendChild(ph);
        } else if (r === 6 && c === 2) {
          // Actinide placeholder 89-103
          const ph = document.createElement('div');
          ph.className = 'element-cell cat-actinide';
          ph.innerHTML = `
            <div class="cell-top"><span>89-103</span></div>
            <div class="cell-symbol" style="font-size:1.05rem;">Ac-Lr</div>
            <div class="cell-name">Actinoids</div>
          `;
          ph.onclick = () => window.filterPeriodicCategory('actinide');
          grid.appendChild(ph);
        } else {
          const spacer = document.createElement('div');
          spacer.className = 'ptable-spacer';
          grid.appendChild(spacer);
        }
      }
    }

    // Populate f-block below (Lanthanides & Actinides)
    if (fBlock) {
      // Row 1: Lanthanides (57 to 71)
      const lLabel = document.createElement('div');
      lLabel.className = 'f-block-label text-rose';
      lLabel.textContent = 'Lanthanides';
      fBlock.appendChild(lLabel);

      elements.filter((e) => e.num >= 57 && e.num <= 71).forEach((el) => {
        fBlock.appendChild(createElementCell(el));
      });

      // Row 2: Actinides (89 to 103)
      const aLabel = document.createElement('div');
      aLabel.className = 'f-block-label text-rose';
      aLabel.textContent = 'Actinides';
      fBlock.appendChild(aLabel);

      elements.filter((e) => e.num >= 89 && e.num <= 103).forEach((el) => {
        fBlock.appendChild(createElementCell(el));
      });
    }
  }

  // Create single interactive element cell with 3D tilt
  function createElementCell(el) {
    const cell = document.createElement('div');
    cell.className = `element-cell cat-${el.cat}`;
    cell.setAttribute('data-num', el.num);
    cell.setAttribute('data-sym', el.sym.toLowerCase());
    cell.setAttribute('data-name', el.name.toLowerCase());
    cell.setAttribute('data-cat', el.cat);

    const matchesSearch = !searchTerm ||
      el.name.toLowerCase().includes(searchTerm) ||
      el.sym.toLowerCase().includes(searchTerm) ||
      el.num.toString() === searchTerm;

    const matchesCategory = activeCategory === 'all' || el.cat === activeCategory;

    if (!matchesSearch || !matchesCategory) {
      cell.classList.add('dimmed');
    }

    const massFormatted = el.mass ? (typeof el.mass === 'number' ? el.mass.toFixed(1) : el.mass) : '';

    cell.innerHTML = `
      <div class="cell-top">
        <span>${el.num}</span>
        <span>${massFormatted}</span>
      </div>
      <div class="cell-symbol">${el.sym}</div>
      <div class="cell-name">${el.name}</div>
    `;

    // 3D Parallax Tilt Effect on Mouse Move
    cell.addEventListener('mousemove', (e) => {
      const rect = cell.getBoundingClientRect();
      const x = e.clientX - rect.left - rect.width / 2;
      const y = e.clientY - rect.top - rect.height / 2;
      const rotX = -(y / rect.height) * 16;
      const rotY = (x / rect.width) * 16;
      cell.style.transform = `perspective(600px) translateY(-5px) rotateX(${rotX}deg) rotateY(${rotY}deg) scale(1.08)`;
    });

    cell.addEventListener('mouseleave', () => {
      cell.style.transform = '';
    });

    cell.addEventListener('click', () => openElementDetail(el));
    return cell;
  }

  // Open Full-Featured Element Modal
  function openElementDetail(el) {
    const modal = document.getElementById('elementModalBackdrop');
    if (!modal) return;

    // Header info
    const symEl = document.getElementById('modalElementSymbol');
    if (symEl) {
      symEl.textContent = el.sym;
      symEl.className = `element-big-symbol text-${el.cat ? el.cat.split('-')[0] : 'emerald'}`;
    }

    const titleEl = document.getElementById('modalElementTitle') || document.getElementById('modalElementName');
    if (titleEl) titleEl.textContent = `${el.name} (Z = ${el.num})`;

    const massEl = document.getElementById('modalElementMass');
    if (massEl) massEl.textContent = `Atomic Mass: ${el.mass} u`;

    const catEl = document.getElementById('modalElementCat');
    if (catEl) catEl.textContent = (el.cat || 'Element').replace(/-/g, ' ').toUpperCase();

    // Key properties
    const setProp = (id, val) => {
      const dom = document.getElementById(id);
      if (dom) dom.textContent = val !== null && val !== undefined ? val : 'N/A';
    };

    setProp('modalElementConfig', el.config);
    setProp('modalElementProtons', el.protons || el.num);
    setProp('modalElementElectrons', el.electrons || el.num);
    setProp('modalElementNeutrons', el.neutrons || Math.round(parseFloat(el.mass) || el.num * 2) - el.num);
    setProp('modalElementGroup', el.grp ? `Group ${el.grp}` : 'f-block');
    setProp('modalElementPeriod', `Period ${el.per}`);
    setProp('modalElementBlock', `${(el.block || 's').toUpperCase()}-Block`);
    setProp('modalElementEN', el.en !== null ? el.en : 'N/A (Noble gas / Synthetic)');
    setProp('modalElementIonization', el.ionization ? `${el.ionization} kJ/mol` : 'N/A');
    setProp('modalElementRadius', el.radius ? `${el.radius} pm` : 'N/A');
    setProp('modalElementState', el.state || 'Solid');
    setProp('modalElementMelt', el.melt !== undefined ? `${el.melt} °C` : 'N/A');
    setProp('modalElementBoil', el.boil !== undefined ? `${el.boil} °C` : 'N/A');
    setProp('modalElementDensity', el.density || 'N/A');
    setProp('modalElementOxidation', el.oxidation || 'N/A');
    setProp('modalElementHistory', el.history || 'Known since scientific records.');
    setProp('modalElementUses', el.uses || 'Industrial and laboratory research applications.');
    setProp('modalElementFacts', el.facts || `Element ${el.num} (${el.name}) exhibits distinctive quantum electron configurations.`);

    // Start animated Bohr Shell Model
    startBohrAnimation(el);

    modal.classList.add('open');
  }

  // Draw Animated Bohr Electron Shell Model on Canvas
  function startBohrAnimation(el) {
    if (bohrAnimFrame) cancelAnimationFrame(bohrAnimFrame);

    const canvas = document.getElementById('bohrModelCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const size = canvas.width = canvas.height = 200;
    const center = size / 2;

    const shells = el.shells && el.shells.length > 0 ? el.shells : [el.num];
    const numShells = Math.min(shells.length, 7);
    const maxRadius = center - 12;
    const shellGap = (maxRadius - 20) / Math.max(1, numShells);

    function frame() {
      bohrAngle += 0.02;
      ctx.clearRect(0, 0, size, size);

      // Nucleus
      ctx.beginPath();
      ctx.arc(center, center, 15, 0, Math.PI * 2);
      ctx.fillStyle = '#ef4444';
      ctx.shadowBlur = 12;
      ctx.shadowColor = '#ef4444';
      ctx.fill();
      ctx.shadowBlur = 0;

      ctx.fillStyle = '#ffffff';
      ctx.font = 'bold 9px monospace';
      ctx.textAlign = 'center';
      ctx.textBaseline = 'middle';
      ctx.fillText(`${el.num}+`, center, center);

      // Draw Orbit Shells & Electrons
      for (let s = 0; s < numShells; s++) {
        const radius = 22 + (s + 1) * shellGap;
        const eCount = shells[s];

        // Orbit path
        ctx.beginPath();
        ctx.arc(center, center, radius, 0, Math.PI * 2);
        ctx.strokeStyle = 'rgba(59, 130, 246, 0.35)';
        ctx.lineWidth = 1;
        ctx.setLineDash([3, 3]);
        ctx.stroke();
        ctx.setLineDash([]);

        // Shell direction alternating
        const dir = s % 2 === 0 ? 1 : -1;
        const speed = 0.8 / (s + 1);

        for (let i = 0; i < eCount; i++) {
          const angle = bohrAngle * dir * speed + (i / eCount) * Math.PI * 2;
          const ex = center + Math.cos(angle) * radius;
          const ey = center + Math.sin(angle) * radius;

          ctx.beginPath();
          ctx.arc(ex, ey, 3.5, 0, Math.PI * 2);
          ctx.fillStyle = '#10b981';
          ctx.shadowBlur = 6;
          ctx.shadowColor = '#10b981';
          ctx.fill();
          ctx.shadowBlur = 0;
        }
      }

      bohrAnimFrame = requestAnimationFrame(frame);
    }

    frame();
  }

  // Global Exposed Filters
  window.filterPeriodicCategory = function(catKey) {
    activeCategory = catKey;
    document.querySelectorAll('.legend-pill').forEach((pill) => {
      pill.classList.toggle('active', pill.getAttribute('data-cat') === catKey);
    });
    renderTable();
  };

  window.handlePeriodicSearch = function(query) {
    searchTerm = query.trim().toLowerCase();
    renderTable();
  };

  window.closeElementModal = function() {
    const modal = document.getElementById('elementModalBackdrop');
    if (modal) modal.classList.remove('open');
    if (bohrAnimFrame) cancelAnimationFrame(bohrAnimFrame);
  };

  window.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('ptableSearchInput');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        searchTerm = e.target.value.trim().toLowerCase();
        renderTable();
      });
    }

    document.querySelectorAll('.legend-pill').forEach((pill) => {
      pill.addEventListener('click', () => {
        const cat = pill.getAttribute('data-cat') || 'all';
        window.filterPeriodicCategory(cat);
      });
    });

    const closeBtn = document.getElementById('closeElementModalBtn');
    const modalBackdrop = document.getElementById('elementModalBackdrop');
    if (closeBtn) closeBtn.addEventListener('click', window.closeElementModal);
    if (modalBackdrop) {
      modalBackdrop.addEventListener('click', (e) => {
        if (e.target === modalBackdrop) window.closeElementModal();
      });
    }

    renderTable();
  });
})();
'''

with open("js/periodic-table.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("js/periodic-table.js successfully updated!")
