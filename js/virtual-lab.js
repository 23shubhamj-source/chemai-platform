/* ==========================================================================
   ChemAI Platform - Virtual Chemistry Laboratory Simulations
   Interactive, state-driven laboratory experiments
   ========================================================================== */

(function initVirtualLab() {
  // State variables for experiments
  const state = {
    currentExp: 'titration', // titration, indicator, precipitation, gas, calorimeter
    // Titration
    titration: {
      addedVolume: 0.0,
      maxVolume: 50.0,
      analyteM: 0.100, // M HCl
      analyteVol: 25.0, // mL
      titrantM: 0.100, // M NaOH
      isRunning: false,
      intervalId: null,
      history: []
    },
    // Indicator
    indicator: {
      activeSubstance: null
    },
    // Precipitation
    precipitation: {
      reagentA: 'AgNO3',
      reagentB: 'NaCl',
      reacted: false
    },
    // Gas Evolution
    gas: {
      metal: 'Zn',
      acid: 'HCl',
      effervescing: false,
      flameTested: false
    },
    // Calorimeter
    calorimeter: {
      temp: 22.0,
      initialTemp: 22.0,
      reacted: false
    }
  };

  // 1. Calculate pH curve for strong acid - strong base titration
  function calculateTitrationPH(vAdded) {
    const Va = state.titration.analyteVol / 1000.0;
    const Ma = state.titration.analyteM;
    const Mb = state.titration.titrantM;
    const Vb = vAdded / 1000.0;

    const molesAcid = Ma * Va;
    const molesBase = Mb * Vb;
    const totalV = Va + Vb;

    if (Math.abs(molesAcid - molesBase) < 1e-6) {
      return 7.00; // Equivalence point
    } else if (molesAcid > molesBase) {
      const excessH = (molesAcid - molesBase) / totalV;
      const ph = -Math.log10(excessH);
      return Math.max(ph, 1.0);
    } else {
      const excessOH = (molesBase - molesAcid) / totalV;
      const poh = -Math.log10(excessOH);
      const ph = 14.0 - poh;
      return Math.min(ph, 13.5);
    }
  }

  // Draw Titration Chart on HTML5 Canvas
  function renderTitrationChart() {
    const canvas = document.getElementById('titrationCurveCanvas');
    if (!canvas) return;
    const ctx = canvas.getContext('2d');
    const w = canvas.width = canvas.parentElement.clientWidth;
    const h = canvas.height = 140;

    ctx.clearRect(0, 0, w, h);

    // Grid lines
    ctx.strokeStyle = 'rgba(226, 232, 240, 0.08)';
    ctx.lineWidth = 1;
    for (let y = 0; y <= 14; y += 3.5) {
      const yPos = h - (y / 14) * (h - 20) - 10;
      ctx.beginPath();
      ctx.moveTo(35, yPos);
      ctx.lineTo(w - 10, yPos);
      ctx.stroke();

      ctx.fillStyle = '#64748b';
      ctx.font = '10px monospace';
      ctx.fillText(y.toFixed(0), 10, yPos + 3);
    }

    // Equivalence mark line at V = 25 mL
    const eqX = 35 + (25.0 / state.titration.maxVolume) * (w - 45);
    ctx.setLineDash([4, 4]);
    ctx.strokeStyle = 'rgba(236, 72, 153, 0.4)';
    ctx.beginPath();
    ctx.moveTo(eqX, 5);
    ctx.lineTo(eqX, h - 10);
    ctx.stroke();
    ctx.setLineDash([]);

    // Curve line
    if (state.titration.history.length > 1) {
      ctx.beginPath();
      ctx.strokeStyle = '#10b981';
      ctx.lineWidth = 2.5;

      state.titration.history.forEach((pt, idx) => {
        const x = 35 + (pt.v / state.titration.maxVolume) * (w - 45);
        const y = h - (pt.ph / 14.0) * (h - 20) - 10;
        if (idx === 0) ctx.moveTo(x, y);
        else ctx.lineTo(x, y);
      });
      ctx.stroke();

      // Current point dot
      const lastPt = state.titration.history[state.titration.history.length - 1];
      const curX = 35 + (lastPt.v / state.titration.maxVolume) * (w - 45);
      const curY = h - (lastPt.ph / 14.0) * (h - 20) - 10;

      ctx.beginPath();
      ctx.arc(curX, curY, 5, 0, Math.PI * 2);
      ctx.fillStyle = lastPt.ph > 8.2 ? '#ec4899' : '#10b981';
      ctx.shadowBlur = 8;
      ctx.shadowColor = ctx.fillStyle;
      ctx.fill();
      ctx.shadowBlur = 0;
    }
  }

  // Update Titration UI Elements
  function updateTitrationUI() {
    const v = state.titration.addedVolume;
    const ph = calculateTitrationPH(v);

    // Save in history
    if (!state.titration.history.some(p => Math.abs(p.v - v) < 0.1)) {
      state.titration.history.push({ v, ph });
      state.titration.history.sort((a, b) => a.v - b.v);
    }

    // Update readouts
    const vReadout = document.getElementById('vlabAddedVol');
    if (vReadout) vReadout.textContent = v.toFixed(2) + ' mL';

    const phReadout = document.getElementById('vlabPHReadout');
    if (phReadout) phReadout.textContent = ph.toFixed(2);

    // Burette liquid level
    const buretteLiquid = document.getElementById('buretteLiquid');
    if (buretteLiquid) {
      const remPct = Math.max(0, 100 - (v / state.titration.maxVolume) * 100);
      buretteLiquid.style.height = `${remPct}%`;
    }

    // Flask solution color
    const flaskSolution = document.getElementById('flaskSolution');
    if (flaskSolution) {
      if (ph < 8.2) {
        flaskSolution.style.backgroundColor = 'rgba(240, 249, 255, 0.4)';
        flaskSolution.classList.remove('pink');
      } else if (ph <= 9.0) {
        flaskSolution.style.backgroundColor = 'rgba(244, 114, 182, 0.75)';
        flaskSolution.classList.add('pink');
      } else {
        flaskSolution.style.backgroundColor = 'rgba(219, 39, 119, 0.9)';
        flaskSolution.classList.add('pink');
      }
    }

    renderTitrationChart();
  }

  // Start / Pause Titration valve
  window.toggleBuretteValve = function() {
    const valveBtn = document.getElementById('valveHandle');
    const droplet = document.getElementById('dropletEmitter');

    if (state.titration.isRunning) {
      clearInterval(state.titration.intervalId);
      state.titration.isRunning = false;
      if (valveBtn) valveBtn.classList.remove('open');
      if (droplet) droplet.classList.remove('dripping');
      logVlabEvent('Titration valve closed.');
    } else {
      if (state.titration.addedVolume >= state.titration.maxVolume) {
        alert('Burette is empty! Reset to run again.');
        return;
      }
      state.titration.isRunning = true;
      if (valveBtn) valveBtn.classList.add('open');
      if (droplet) droplet.classList.add('dripping');
      logVlabEvent('Titration valve opened. Dispensing 0.1M NaOH...');

      state.titration.intervalId = setInterval(() => {
        state.titration.addedVolume += 0.25;
        if (state.titration.addedVolume >= state.titration.maxVolume) {
          window.toggleBuretteValve();
        }
        updateTitrationUI();

        // Check equivalence trigger
        if (Math.abs(state.titration.addedVolume - 25.0) < 0.2) {
          logVlabEvent('⭐ Equivalence Point Reached! pH = 7.00. Phenolphthalein turns pale pink.');
        }
      }, 150);
    }
  };

  // Add a single drop (0.05 mL)
  window.dispenseSingleDrop = function() {
    if (state.titration.addedVolume < state.titration.maxVolume) {
      state.titration.addedVolume += 0.1;
      updateTitrationUI();
      logVlabEvent(`Added single drop (+0.10 mL). Volume: ${state.titration.addedVolume.toFixed(2)} mL`);
    }
  };

  // Reset Titration
  window.resetTitration = function() {
    if (state.titration.isRunning) window.toggleBuretteValve();
    state.titration.addedVolume = 0.0;
    state.titration.history = [{ v: 0.0, ph: calculateTitrationPH(0.0) }];
    updateTitrationUI();
    logVlabEvent('Burette refilled and Erlenmeyer flask reset.');
  };

  // 2. Universal Indicator Simulation
  const SUBSTANCES = {
    hcl: { name: '1 M HCl (Hydrochloric Acid)', ph: 0.5, color: '#ef4444', desc: 'Gastric acid equivalent. Red universal indicator.' },
    lemon: { name: 'Lemon Juice (Citric Acid)', ph: 2.3, color: '#f97316', desc: 'Natural organic triprotic acid. Orange color.' },
    vinegar: { name: 'Vinegar (5% Acetic Acid)', ph: 2.9, color: '#fb923c', desc: 'CH3COOH weak acid solution. Orange-yellow.' },
    coffee: { name: 'Black Coffee', ph: 5.0, color: '#eab308', desc: 'Mild chlorogenic acids. Yellow indicator.' },
    water: { name: 'Pure Neutral Water (H2O)', ph: 7.0, color: '#10b981', desc: 'Pure neutral Kw = 10^-14. Emerald green.' },
    bakingSoda: { name: 'Baking Soda (NaHCO3)', ph: 8.5, color: '#06b6d4', desc: 'Weak conjugate base hydrolysis. Cyan.' },
    ammonia: { name: 'Household Ammonia (NH3)', ph: 11.2, color: '#3b82f6', desc: 'Weak base amine solution. Electric cobalt blue.' },
    bleach: { name: 'Bleach / 1 M NaOH', ph: 13.5, color: '#a855f7', desc: 'Strong alkaline solution. Deep violet.' }
  };

  window.testIndicatorSubstance = function(key) {
    const sub = SUBSTANCES[key];
    if (!sub) return;

    const tubeFluid = document.getElementById('indicatorTubeFluid');
    const phDisplay = document.getElementById('indicatorPHValue');
    const descDisplay = document.getElementById('indicatorDesc');

    if (tubeFluid) tubeFluid.style.backgroundColor = sub.color;
    if (phDisplay) phDisplay.textContent = `pH ${sub.ph.toFixed(1)}`;
    if (descDisplay) descDisplay.textContent = `${sub.name}: ${sub.desc}`;

    logVlabEvent(`Tested ${sub.name}: Indicator color shifted to pH ${sub.ph} (${sub.desc})`);
  };

  // 3. Precipitation Lab
  const PRECIPITATE_REACTIONS = {
    'AgNO3_NaCl': {
      eq: 'AgNO3 (aq) + NaCl (aq) → AgCl (s)↓ + NaNO3 (aq)',
      net: 'Ag⁺ (aq) + Cl⁻ (aq) → AgCl (s)↓',
      color: 'rgba(255, 255, 255, 0.95)',
      desc: 'White curdy precipitate of Silver Chloride forms instantly.'
    },
    'PbNO3_KI': {
      eq: 'Pb(NO3)2 (aq) + 2KI (aq) → PbI2 (s)↓ + 2KNO3 (aq)',
      net: 'Pb²⁺ (aq) + 2I⁻ (aq) → PbI2 (s)↓',
      color: '#facc15',
      desc: 'Brilliant golden yellow precipitate of Lead(II) Iodide ("Golden Rain").'
    },
    'CuSO4_NaOH': {
      eq: 'CuSO4 (aq) + 2NaOH (aq) → Cu(OH)2 (s)↓ + Na2SO4 (aq)',
      net: 'Cu²⁺ (aq) + 2OH⁻ (aq) → Cu(OH)2 (s)↓',
      color: '#38bdf8',
      desc: 'Gelatinous bright sky-blue precipitate of Copper(II) Hydroxide.'
    }
  };

  window.mixPrecipitation = function(reactionKey) {
    const rxn = PRECIPITATE_REACTIONS[reactionKey];
    if (!rxn) return;

    const tube = document.getElementById('precipitateTubeFluid');
    const label = document.getElementById('precipitateReactionLabel');

    if (tube) {
      tube.style.backgroundColor = rxn.color;
      tube.style.boxShadow = `0 0 16px ${rxn.color}`;
    }
    if (label) {
      label.innerHTML = `<strong>${rxn.eq}</strong><br><span class="text-emerald">Net Ionic: ${rxn.net}</span><br><small>${rxn.desc}</small>`;
    }
    logVlabEvent(`Precipitation Reaction: ${rxn.eq}`);
  };

  // Helper log function
  function logVlabEvent(text) {
    const logBox = document.getElementById('vlabLog');
    if (!logBox) return;

    const entry = document.createElement('div');
    entry.className = 'log-entry';
    const time = new Date().toLocaleTimeString();
    entry.innerHTML = `<span class="log-timestamp">[${time}]</span> ${text}`;
    logBox.prepend(entry);
  }

  // Switch experiment views
  window.switchLabExperiment = function(expName) {
    state.currentExp = expName;
    document.querySelectorAll('.vlab-exp-tab').forEach(t => {
      t.classList.toggle('active', t.getAttribute('data-exp') === expName);
    });

    document.querySelectorAll('.vlab-exp-view').forEach(v => {
      v.style.display = v.id === `view_${expName}` ? 'block' : 'none';
    });

    logVlabEvent(`Switched apparatus to: ${expName.toUpperCase()} experiment.`);
  };

  // Initialize titration on load
  setTimeout(() => {
    state.titration.history = [{ v: 0.0, ph: calculateTitrationPH(0.0) }];
    updateTitrationUI();
  }, 300);
})();
