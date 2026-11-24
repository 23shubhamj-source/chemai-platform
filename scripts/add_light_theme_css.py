light_css = """

/* ==========================================================================
   ChemAI Platform - Light Mode Theme Specification
   ========================================================================== */

[data-theme="light"] {
  --bg-dark: #f8fafc;
  --bg-deep: #f1f5f9;
  --bg-surface: #ffffff;
  --bg-surface-elevated: #f8fafc;
  --bg-surface-hover: #e2e8f0;
  --bg-glass: rgba(255, 255, 255, 0.88);
  --bg-glass-light: rgba(255, 255, 255, 0.65);

  --color-emerald: #059669;
  --color-emerald-glow: rgba(5, 150, 105, 0.15);
  --color-emerald-light: #10b981;
  --color-cobalt: #2563eb;
  --color-cobalt-glow: rgba(37, 99, 235, 0.15);
  --color-cyan: #0284c7;
  --color-amber: #d97706;
  --color-amber-glow: rgba(217, 119, 6, 0.15);
  --color-violet: #7c3aed;
  --color-violet-glow: rgba(124, 58, 237, 0.15);
  --color-rose: #db2777;
  --color-red: #dc2626;

  --text-main: #334155;
  --text-muted: #64748b;
  --text-dim: #94a3b8;
  --text-highlight: #0f172a;

  --border-subtle: rgba(15, 23, 42, 0.1);
  --border-emerald: rgba(5, 150, 105, 0.3);
  --border-cobalt: rgba(37, 99, 235, 0.3);
  --border-glow: 0 4px 24px rgba(5, 150, 105, 0.12);
}

[data-theme="light"] body {
  background-color: var(--bg-dark);
  color: var(--text-main);
}

[data-theme="light"] .ambient-glow-1 {
  background: radial-gradient(circle, rgba(5, 150, 105, 0.08) 0%, transparent 70%);
}

[data-theme="light"] .ambient-glow-2 {
  background: radial-gradient(circle, rgba(37, 99, 235, 0.08) 0%, transparent 70%);
}

[data-theme="light"] .hero-title,
[data-theme="light"] .sec-title,
[data-theme="light"] h1, [data-theme="light"] h2, [data-theme="light"] h3, [data-theme="light"] h4 {
  color: var(--text-highlight) !important;
}

[data-theme="light"] .glass-card,
[data-theme="light"] .tool-card,
[data-theme="light"] .hero-preview-card,
[data-theme="light"] .chat-card,
[data-theme="light"] .mol-details-card,
[data-theme="light"] .ptable-container,
[data-theme="light"] .sim-card {
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.06), 0 1px 3px rgba(0, 0, 0, 0.05);
}

[data-theme="light"] .btn-ghost {
  border-color: rgba(15, 23, 42, 0.2);
  color: #0f172a;
}
"""

with open("css/main.css", "a", encoding="utf-8") as f:
    f.write(light_css)

print("Light mode CSS appended to css/main.css!")
