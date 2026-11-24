part1 = """<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Virtual Chemistry Simulation Hub - ChemAI Platform</title>
  <meta name="description" content="Interactive chemistry simulations: Build-A-Molecule with valency validation, 3D VSEPR molecular shapes, bonding, Aufbau principle, thermodynamics, and electrochemical cells.">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="css/main.css">
  <link rel="stylesheet" href="css/components.css">
  <link rel="stylesheet" href="css/simulations.css">
</head>
<body>
  <canvas id="particle-canvas" aria-hidden="true"></canvas>
  <div class="ambient-glow ambient-glow-1"></div>
  <div class="ambient-glow ambient-glow-2"></div>

  <!-- Sticky Modern Navigation Bar -->
  <header class="site-nav" role="banner">
    <div class="container">
      <div class="nav-container">
        <a href="index.html" class="nav-brand" aria-label="ChemAI Home">
          <div class="brand-icon-box">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2">
              <path d="M10 2v7.31L4.62 18.27A2 2 0 0 0 6.35 21h11.3a2 2 0 0 0 1.73-2.73L14 9.31V2"/>
              <line x1="8.5" y1="2" x2="15.5" y2="2"/>
              <path d="M14 9.3a6.5 6.5 0 0 0-4 0"/>
            </svg>
          </div>
          <span>Chem<span class="brand-text-ai">AI</span></span>
        </a>
        <nav class="nav-links" id="siteNavLinks">
          <a href="index.html" class="nav-link">Home</a>
          <a href="index.html#ai-assistant" class="nav-link">AI Assistant</a>
          <a href="tools.html" class="nav-link">Tools</a>
          <a href="virtual-lab.html" class="nav-link">Virtual Lab</a>
          <a href="simulations.html" class="nav-link active">Simulations</a>
          <a href="periodic-table.html" class="nav-link">Periodic Table</a>
          <a href="index.html#molecule-viewer" class="nav-link">3D Molecules</a>
          <a href="study-hub.html" class="nav-link">Study Hub</a>
          <a href="spectroscopy.html" class="nav-link">Spectroscopy</a>
        </nav>
        <div class="nav-actions">
          <button type="button" class="btn-icon theme-toggle-btn" id="themeToggleBtn" onclick="toggleTheme()" aria-label="Toggle dark/light theme" title="Toggle theme">
            <span class="theme-toggle-icon">☀️</span>
          </button>
          <button type="button" class="nav-search-btn" onclick="openSearchPalette()">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <span>Search</span>
            <kbd>Ctrl K</kbd>
          </button>
          <a href="virtual-lab.html" class="btn btn-primary btn-sm">Launch Lab</a>
        </div>
      </div>
    </div>
  </header>

  <main class="container" style="padding-top:2.5rem;padding-bottom:5rem;">
    <div class="sec-head">
      <span class="sec-eyebrow">Interactive Physics &amp; Chemistry Simulations</span>
      <h1 class="sec-title">Virtual Chemistry Simulation Hub</h1>
      <p class="sec-subtitle">Hands-on visual models for molecular architecture, VSEPR geometries, electronic configurations, and chemical reaction dynamics.</p>
    </div>

    <div class="sim-hub-layout">
      <!-- Navigation Sidebar -->
      <aside class="sim-sidebar">
        <button class="sim-nav-tab active" data-tab="build" onclick="switchSimTab('build')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="3"/><circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><line x1="12" y1="9" x2="19" y2="7"/><line x1="12" y1="15" x2="5" y2="17"/></svg>
          <span>Build-A-Molecule</span>
        </button>
        <button class="sim-nav-tab" data-tab="vsepr" onclick="switchSimTab('vsepr')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/></svg>
          <span>VSEPR 3D Shapes</span>
        </button>
        <button class="sim-nav-tab" data-tab="bonding" onclick="switchSimTab('bonding')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="7" cy="12" r="4"/><circle cx="17" cy="12" r="4"/></svg>
          <span>Chemical Bonding</span>
        </button>
        <button class="sim-nav-tab" data-tab="aufbau" onclick="switchSimTab('aufbau')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>
          <span>Aufbau Principle</span>
        </button>
        <button class="sim-nav-tab" data-tab="energy" onclick="switchSimTab('energy')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/></svg>
          <span>Reaction Energy (Ea)</span>
        </button>
        <button class="sim-nav-tab" data-tab="lechatelier" onclick="switchSimTab('lechatelier')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="m18 15-6-6-6 6"/></svg>
          <span>Le Chatelier's Principle</span>
        </button>
        <button class="sim-nav-tab" data-tab="gas" onclick="switchSimTab('gas')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg>
          <span>Gas Laws (PV = nRT)</span>
        </button>
        <button class="sim-nav-tab" data-tab="galvanic" onclick="switchSimTab('galvanic')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="2" y="7" width="20" height="14" rx="2" ry="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/></svg>
          <span>Galvanic Cell</span>
        </button>
        <button class="sim-nav-tab" data-tab="solubility" onclick="switchSimTab('solubility')">
          <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M10 2v7.31L4.62 18.27A2 2 0 0 0 6.35 21h11.3a2 2 0 0 0 1.73-2.73L14 9.31V2"/></svg>
          <span>Solubility &amp; Ksp</span>
        </button>
      </aside>

      <!-- Workspace Container -->
      <div class="sim-workspace-card">
        <!-- 1. Build-A-Molecule Pane -->
        <div class="sim-tab-pane" id="simPane_build">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;margin-bottom:1rem;">
            <div>
              <h3 style="color:var(--text-highlight);margin:0;">Build-A-Molecule 2D / 3D Builder</h3>
              <p style="color:var(--text-muted);font-size:0.85rem;margin:0.25rem 0 0;">Drag atoms, connect single/double/triple bonds, and validate IUPAC valency rules.</p>
            </div>
            <div style="display:flex;align-items:center;gap:0.75rem;">
              <span id="buildMolStatus" class="chip chip-emerald">✓ Stable Molecule</span>
              <strong id="buildMolFormula" style="font-size:1.2rem;color:var(--color-cyan);font-family:var(--font-mono);">H₂O</strong>
            </div>
          </div>

          <!-- Atom Palette & Bond Tools -->
          <div class="atom-palette-bar">
            <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Atoms:</span>
            <button class="atom-palette-btn active" data-sym="C" style="background:#475569;" onclick="selectPaletteAtom('C')">C</button>
            <button class="atom-palette-btn" data-sym="H" style="background:#ffffff;color:#0f172a;" onclick="selectPaletteAtom('H')">H</button>
            <button class="atom-palette-btn" data-sym="O" style="background:#ef4444;" onclick="selectPaletteAtom('O')">O</button>
            <button class="atom-palette-btn" data-sym="N" style="background:#3b82f6;" onclick="selectPaletteAtom('N')">N</button>
            <button class="atom-palette-btn" data-sym="Cl" style="background:#10b981;" onclick="selectPaletteAtom('Cl')">Cl</button>
            <button class="atom-palette-btn" data-sym="F" style="background:#22c55e;" onclick="selectPaletteAtom('F')">F</button>
            <button class="atom-palette-btn" data-sym="Br" style="background:#991b1b;" onclick="selectPaletteAtom('Br')">Br</button>
            <button class="atom-palette-btn" data-sym="S" style="background:#eab308;color:#0f172a;" onclick="selectPaletteAtom('S')">S</button>
            <button class="atom-palette-btn" data-sym="P" style="background:#f97316;" onclick="selectPaletteAtom('P')">P</button>

            <div style="margin-left:auto;display:flex;gap:0.5rem;align-items:center;">
              <span style="font-size:0.82rem;color:var(--text-muted);font-weight:600;">Bond:</span>
              <button class="bond-tool-btn active" data-order="1" onclick="setBuildBondOrder(1)">Single (-)</button>
              <button class="bond-tool-btn" data-order="2" onclick="setBuildBondOrder(2)">Double (=)</button>
              <button class="bond-tool-btn" data-order="3" onclick="setBuildBondOrder(3)">Triple (≡)</button>
            </div>
          </div>

          <div class="sim-canvas-box">
            <canvas id="buildMolCanvas"></canvas>
          </div>

          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:0.75rem;">
            <div style="display:flex;gap:0.5rem;">
              <button class="btn btn-ghost btn-sm" onclick="loadBuildPreset('water')">Water</button>
              <button class="btn btn-ghost btn-sm" onclick="loadBuildPreset('methane')">Methane</button>
              <button class="btn btn-ghost btn-sm" onclick="loadBuildPreset('carbon_dioxide')">Carbon Dioxide</button>
            </div>
            <div style="display:flex;gap:0.5rem;">
              <button class="btn btn-ghost btn-sm" onclick="deleteSelectedBuildAtom()">Delete Selected</button>
              <button class="btn btn-ghost btn-sm" onclick="clearBuildCanvas()">Clear Workspace</button>
              <a href="index.html#molecule-viewer" class="btn btn-primary btn-sm">Inspect in 3D Explorer →</a>
            </div>
          </div>
        </div>
"""

with open("simulations.html", "w", encoding="utf-8") as f:
    f.write(part1)
print("Wrote simulations.html Part 1")
