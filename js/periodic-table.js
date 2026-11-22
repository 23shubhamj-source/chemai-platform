/* ==========================================================================
   ChemAI Platform - Interactive Periodic Table Controller
   ========================================================================== */

(function initPeriodicTable() {
  const elements = window.PERIODIC_TABLE_DATA || [];
  let activeCategory = 'all';
  let searchTerm = '';

  // Render Table Grid
  function renderTable() {
    const grid = document.getElementById('ptableGrid');
    const fBlock = document.getElementById('ptableFBlock');
    if (!grid) return;

    grid.innerHTML = '';
    if (fBlock) fBlock.innerHTML = '';

    // Standard Layout: 7 rows x 18 cols
    // Create matrix 7 x 18
    const matrix = Array.from({ length: 7 }, () => Array(18).fill(null));

    // Place main block elements
    elements.forEach(el => {
      // Lanthanides (57-71) and Actinides (89-103) go to f-block
      if ((el.num >= 57 && el.num <= 71) || (el.num >= 89 && el.num <= 103)) {
        return;
      }
      const r = el.per - 1;
      const c = el.grp - 1;
      if (r >= 0 && r < 7 && c >= 0 && c < 18) {
        matrix[r][c] = el;
      }
    });

    // Populate main grid
    for (let r = 0; r < 7; r++) {
      for (let c = 0; c < 18; c++) {
        const el = matrix[r][c];
        if (el) {
          grid.appendChild(createElementCell(el));
        } else if (r === 5 && c === 2) {
          // Lanthanide placeholder 57-71
          const ph = document.createElement('div');
          ph.className = 'element-cell cat-lanthanide';
          ph.innerHTML = '<span class="cell-top">57-71</span><span class="cell-symbol">La-Lu</span><span class="cell-name">Lanthanoids</span>';
          grid.appendChild(ph);
        } else if (r === 6 && c === 2) {
          // Actinide placeholder 89-103
          const ph = document.createElement('div');
          ph.className = 'element-cell cat-actinide';
          ph.innerHTML = '<span class="cell-top">89-103</span><span class="cell-symbol">Ac-Lr</span><span class="cell-name">Actinoids</span>';
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
      // Row 1: Lanthanides
      const lLabel = document.createElement('div');
      lLabel.className = 'f-block-label text-rose';
      lLabel.textContent = 'Lanthanides 57-71';
      fBlock.appendChild(lLabel);

      elements.filter(e => e.num >= 57 && e.num <= 71).forEach(el => {
        fBlock.appendChild(createElementCell(el));
      });

      // Row 2: Actinides
      const aLabel = document.createElement('div');
      aLabel.className = 'f-block-label text-rose';
      aLabel.textContent = 'Actinides 89-103';
      fBlock.appendChild(aLabel);

      elements.filter(e => e.num >= 89 && e.num <= 103).forEach(el => {
        fBlock.appendChild(createElementCell(el));
      });
    }
  }

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

    cell.innerHTML = `
      <div class="cell-top">
        <span>${el.num}</span>
        <span>${el.mass ? (typeof el.mass === 'number' ? el.mass.toFixed(1) : el.mass) : ''}</span>
      </div>
      <div class="cell-symbol">${el.sym}</div>
      <div class="cell-name">${el.name}</div>
    `;

    cell.addEventListener('click', () => openElementDetail(el));
    return cell;
  }

  // Open Element Modal with Bohr electron shells
  function openElementDetail(el) {
    const modal = document.getElementById('elementModalBackdrop');
    if (!modal) return;

    document.getElementById('modalElementSymbol').textContent = el.sym;
    document.getElementById('modalElementName').textContent = `${el.name} (${el.num})`;
    document.getElementById('modalElementMass').textContent = `${el.mass} u`;
    document.getElementById('modalElementCat').textContent = el.cat.replace(/-/g, ' ').toUpperCase();
    document.getElementById('modalElementConfig').textContent = el.config;
    document.getElementById('modalElementEN').textContent = el.en !== null ? el.en : 'N/A (Noble gas / Synthetic)';
    document.getElementById('modalElementState').textContent = el.state || 'Solid';
    document.getElementById('modalElementUses').textContent = el.uses || 'Industrial and laboratory research';

    // Draw Bohr Shell model
    drawBohrModel(el.num);

    modal.classList.add('open');
  }

  // Draw Bohr Model on Canvas
  function drawBohrModel(atomicNumber) {
    const canvas = document.getElementById('bohrModelCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const size = canvas.width = canvas.height = 160;
    const center = size / 2;

    ctx.clearRect(0, 0, size, height = size);

    // Nucleus
    ctx.beginPath();
    ctx.arc(center, center, 14, 0, Math.PI * 2);
    ctx.fillStyle = '#ef4444';
    ctx.shadowBlur = 10;
    ctx.shadowColor = '#ef4444';
    ctx.fill();
    ctx.shadowBlur = 0;

    ctx.fillStyle = '#fff';
    ctx.font = 'bold 9px monospace';
    ctx.textAlign = 'center';
    ctx.textBaseline = 'middle';
    ctx.fillText(`${atomicNumber}+`, center, center);

    // Shell capacities: 2, 8, 18, 32
    const shellCapacities = [2, 8, 18, 32];
    let remaining = atomicNumber;
    let shellIndex = 0;

    while (remaining > 0 && shellIndex < 4) {
      const radius = 24 + shellIndex * 15;
      const countInShell = Math.min(remaining, shellCapacities[shellIndex]);
      remaining -= countInShell;

      // Draw orbit circle
      ctx.beginPath();
      ctx.arc(center, center, radius, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(59, 130, 246, 0.35)';
      ctx.lineWidth = 1;
      ctx.stroke();

      // Draw electrons
      for (let i = 0; i < countInShell; i++) {
        const angle = (i / countInShell) * Math.PI * 2;
        const ex = center + Math.cos(angle) * radius;
        const ey = center + Math.sin(angle) * radius;

        ctx.beginPath();
        ctx.arc(ex, ey, 3, 0, Math.PI * 2);
        ctx.fillStyle = '#10b981';
        ctx.shadowBlur = 5;
        ctx.shadowColor = '#10b981';
        ctx.fill();
        ctx.shadowBlur = 0;
      }

      shellIndex++;
    }
  }

  // Setup search & filter event listeners
  window.addEventListener('DOMContentLoaded', () => {
    const searchInput = document.getElementById('ptableSearchInput');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        searchTerm = e.target.value.trim().toLowerCase();
        renderTable();
      });
    }

    document.querySelectorAll('.legend-pill').forEach(pill => {
      pill.addEventListener('click', (e) => {
        document.querySelectorAll('.legend-pill').forEach(p => p.classList.remove('active'));
        pill.classList.add('active');
        activeCategory = pill.getAttribute('data-cat') || 'all';
        renderTable();
      });
    });

    // Close modal listener
    const closeBtn = document.getElementById('closeElementModalBtn');
    const modalBackdrop = document.getElementById('elementModalBackdrop');
    if (closeBtn && modalBackdrop) {
      closeBtn.addEventListener('click', () => modalBackdrop.classList.remove('open'));
      modalBackdrop.addEventListener('click', (e) => {
        if (e.target === modalBackdrop) modalBackdrop.classList.remove('open');
      });
    }

    renderTable();
  });
})();
