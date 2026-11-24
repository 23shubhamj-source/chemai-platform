js_code = r'''/* ==========================================================================
   ChemAI Platform - Advanced AI Chemistry Assistant & Voice Companion
   Gemini API Backend integration, 4 response styles, Voice I/O, KaTeX Math
   ========================================================================== */

(function initAdvancedAIAssistant() {
  let conversationHistory = [];
  let currentResponseStyle = "detailed";
  let lastUserMessage = "";
  let lastBotResponse = "";
  let recognitionInstance = null;
  let isListening = false;
  let synthUtterance = null;
  let isSpeaking = false;
  let isPaused = false;

  // Scientific Offline Fallback Knowledge Base (for static GitHub Pages or offline use)
  const OFFLINE_KB = [
    {
      keywords: ["balance", "equation", "reaction"],
      title: "Chemical Equation Balancing",
      response: `To balance a chemical equation, ensure equal atom counts on both sides according to the **Law of Conservation of Mass**:

<div class="chem-equation-box">$$4\text{Fe (s)} + 3\text{O}_2\text{ (g)} \longrightarrow 2\text{Fe}_2\text{O}_3\text{ (s)}$$</div>

<div class="step-box">
  <div class="step-box-title">Step 1: Count Initial Atoms</div>
  Reactants: Fe = 1, O = 2<br>
  Products: Fe = 2, O = 3
</div>

<div class="step-box">
  <div class="step-box-title">Step 2: Balance Oxygen First</div>
  LCM of 2 and 3 is 6. Multiply $\text{O}_2$ by 3 and $\text{Fe}_2\text{O}_3$ by 2:<br>
  <code>Fe + 3O₂ → 2Fe₂O₃</code>
</div>

<div class="step-box">
  <div class="step-box-title">Step 3: Balance Metal Atoms</div>
  Products now have 4 Fe. Add coefficient 4 to reactant Fe:<br>
  <strong class="text-emerald">Balanced: 4Fe + 3O₂ → 2Fe₂O₃ ($\Delta H^\circ = -1648\text{ kJ/mol}$)</strong>
</div>`
    },
    {
      keywords: ["sn1", "sn2", "nucleophilic", "substitution"],
      title: "SN1 vs SN2 Reaction Mechanisms",
      response: `Here is a side-by-side comparison of **S<sub>N</sub>1** and **S<sub>N</sub>2** nucleophilic substitution:

<table class="element-props-table" style="margin: 0.75rem 0;">
  <thead>
    <tr style="color: var(--color-emerald); border-bottom: 1px solid var(--border-subtle);">
      <th style="text-align: left; padding: 4px 0;">Property</th>
      <th style="text-align: left;">S<sub>N</sub>1</th>
      <th style="text-align: left;">S<sub>N</sub>2</th>
    </tr>
  </thead>
  <tbody>
    <tr><td>Mechanism</td><td>Two steps (Carbocation intermediate)</td><td>One step (Concerted transition state)</td></tr>
    <tr><td>Kinetics</td><td>First order: $\text{Rate} = k[R-X]$</td><td>Second order: $\text{Rate} = k[R-X][Nu^-]$</td></tr>
    <tr><td>Substrate</td><td>3° > 2° >> 1° (Steric stability)</td><td>CH₃ > 1° > 2° >> 3° (Steric hindrance)</td></tr>
    <tr><td>Stereochemistry</td><td>Racemization (inversion + retention)</td><td>Complete Walden Inversion (100% backside attack)</td></tr>
    <tr><td>Solvent</td><td>Polar protic (H₂O, EtOH, MeOH stabilizes carbocation)</td><td>Polar aprotic (Acetone, DMSO, DMF maximizes Nu⁻)</td></tr>
  </tbody>
</table>`
    },
    {
      keywords: ["bond", "bonding", "covalent", "ionic", "vsepr"],
      title: "Chemical Bonding & VSEPR Geometries",
      response: `Chemical bonds form to achieve stable minimum-energy octet electron configurations:

<div class="step-box">
  <div class="step-box-title">1. Ionic Bonding ($\Delta EN > 1.7$)</div>
  Complete valence electron transfer: $\text{Na (3s¹)} + \text{Cl (3p⁵)} \to \text{Na}^+ [\text{Ne}] + \text{Cl}^- [\text{Ar}]$.
</div>

<div class="step-box">
  <div class="step-box-title">2. Covalent Bonding ($\Delta EN < 1.7$)</div>
  Valence electron sharing: single ($\sigma$), double ($\sigma + \pi$), and triple ($\sigma + 2\pi$) bonds.
</div>

<div class="step-box">
  <div class="step-box-title">3. VSEPR Molecular Geometry</div>
  Electron pairs repel each other: Lone Pair-Lone Pair > Lone Pair-Bonding Pair > Bonding Pair-Bonding Pair.
</div>`
    },
    {
      keywords: ["stoichiometry", "limiting", "reagent", "yield"],
      title: "Stoichiometry & Limiting Reagents",
      response: `Stoichiometry calculates mass-mole quantities from balanced chemical equations:

<div class="step-box">
  <div class="step-box-title">Problem: 16.0 g of O₂ reacting with 4.0 g of H₂</div>
  Reaction: $2\text{H}_2 + \text{O}_2 \longrightarrow 2\text{H}_2\text{O}$<br><br>
  1. $\text{Moles of } \text{H}_2 = \frac{4.0\text{ g}}{2.016\text{ g/mol}} = 1.984\text{ mol}$<br>
  2. $\text{Moles of } \text{O}_2 = \frac{16.0\text{ g}}{31.998\text{ g/mol}} = 0.500\text{ mol}$<br>
  3. Mole ratio requires $2 \times 0.500 = 1.00\text{ mol } \text{H}_2$. Since we have 1.984 mol $\text{H}_2$, $\text{O}_2$ is the **Limiting Reagent**.<br>
  4. **Theoretical Yield:** $0.500\text{ mol } \text{O}_2 \times 2 = 1.00\text{ mol } \text{H}_2\text{O} = 18.015\text{ g}$.
</div>`
    }
  ];

  function getOfflineResponse(text, style) {
    const q = text.toLowerCase();
    for (const item of OFFLINE_KB) {
      if (item.keywords.some((k) => q.includes(k))) {
        return item.response;
      }
    }

    return `### ChemAI Scientific Analysis

**Core Scientific Concept:**
Chemical processes and transformations follow the fundamental laws of thermodynamics ($\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$) and quantum molecular orbital stability.

**Recommended Exploration Steps:**
1. **Interactive Tools:** Model this reaction in the <a href="#tools" class="text-emerald" style="text-decoration:underline;">Calculators Dashboard</a>.
2. **Virtual Simulations:** Run live digital titrations or VSEPR simulations in the <a href="#virtual-lab" class="text-emerald" style="text-decoration:underline;">Virtual Chemistry Lab</a>.
3. **3D Molecular Models:** Examine spatial conformations in the <a href="#molecule-viewer" class="text-emerald" style="text-decoration:underline;">3D Molecule Viewer</a>.

*Tip: Connect your Gemini API key in <code>.env</code> for unlimited live generative chemistry tutoring!*`;
  }

  // Append Chat Message
  function appendMessage(sender, htmlContent, rawTextForSpeech = "") {
    const area = document.getElementById("chatMessagesArea");
    if (!area) return;

    const row = document.createElement("div");
    row.className = `chat-message ${sender}`;

    const isBot = sender === "bot";
    const avatar = isBot ? "AI" : "You";

    const speechText = rawTextForSpeech || (typeof htmlContent === "string" ? htmlContent.replace(/<[^>]*>/g, "") : "");

    row.innerHTML = `
      <div class="chat-avatar">${avatar}</div>
      <div class="chat-bubble">
        ${htmlContent}
        ${isBot ? `
          <div class="chat-msg-actions">
            <button type="button" class="chat-action-btn" onclick="window.speakTextMessage(this)" data-speech="${encodeURIComponent(speechText)}" title="Read Aloud">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><polygon points="11 5 6 9 2 9 2 15 6 15 11 19 11 5"/><path d="M19.07 4.93a10 10 0 0 1 0 14.14M15.54 8.46a5 5 0 0 1 0 7.07"/></svg>
              <span>Listen</span>
            </button>
            <button type="button" class="chat-action-btn" onclick="window.copyMessageText(this)" title="Copy text">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/></svg>
              <span>Copy</span>
            </button>
            <button type="button" class="chat-action-btn" onclick="window.regenerateLastResponse()" title="Regenerate Response">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M23 4v6h-6M1 20v-6h6M3.51 9a9 9 0 0 1 14.85-3.36L23 10M1 14l4.64 4.36A9 9 0 0 0 20.49 15"/></svg>
              <span>Regenerate</span>
            </button>
          </div>
        ` : ""}
      </div>
    `;

    area.appendChild(row);
    area.scrollTop = area.scrollHeight;

    // Trigger MathJax / KaTeX typesetting if present
    if (window.renderMathInElement) {
      window.renderMathInElement(row, {
        delimiters: [
          { left: "$$", right: "$$", display: true },
          { left: "$", right: "$", display: false }
        ],
        throwOnError: false
      });
    } else if (window.MathJax && window.MathJax.typesetPromise) {
      window.MathJax.typesetPromise([row]).catch((err) => console.log(err));
    }
  }

  // Show Typing Indicator
  function showTypingIndicator() {
    const area = document.getElementById("chatMessagesArea");
    if (!area) return null;

    const ind = document.createElement("div");
    ind.id = "chatTypingIndicator";
    ind.className = "chat-message bot";
    ind.innerHTML = `
      <div class="chat-avatar">AI</div>
      <div class="chat-bubble" style="display:flex;align-items:center;gap:6px;padding:0.75rem 1.25rem;">
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
        <span class="typing-dot"></span>
        <span style="font-size:0.82rem;color:var(--text-dim);margin-left:8px;">ChemAI is analyzing...</span>
      </div>
    `;
    area.appendChild(ind);
    area.scrollTop = area.scrollHeight;
    return ind;
  }

  function removeTypingIndicator() {
    const ind = document.getElementById("chatTypingIndicator");
    if (ind) ind.remove();
  }

  // Send Message to Backend Gemini API
  async function sendMessage(text) {
    if (!text || !text.trim()) return;
    const cleanText = text.trim();
    lastUserMessage = cleanText;

    appendMessage("user", cleanText);
    conversationHistory.push({ role: "user", content: cleanText });

    const indicator = showTypingIndicator();

    try {
      const response = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message: cleanText,
          style: currentResponseStyle,
          history: conversationHistory.slice(-6)
        })
      });

      removeTypingIndicator();

      if (response.ok) {
        const data = await response.json();
        const reply = data.reply || "I am analyzing this chemical problem.";
        lastBotResponse = reply;
        conversationHistory.push({ role: "assistant", content: reply });
        
        let formatted = formatMarkdownReply(reply);
        if (data.note) {
          formatted += `<div style="font-size:0.75rem;color:var(--text-dim);margin-top:8px;border-top:1px dashed var(--border-subtle);padding-top:4px;">ℹ️ ${data.note}</div>`;
        }
        appendMessage("bot", formatted, reply);
      } else {
        // Fallback to offline knowledge base
        const fallback = getOfflineResponse(cleanText, currentResponseStyle);
        lastBotResponse = fallback;
        conversationHistory.push({ role: "assistant", content: fallback });
        appendMessage("bot", formatMarkdownReply(fallback), fallback);
      }
    } catch (err) {
      removeTypingIndicator();
      // Graceful offline fallback
      const fallback = getOfflineResponse(cleanText, currentResponseStyle);
      lastBotResponse = fallback;
      conversationHistory.push({ role: "assistant", content: fallback });
      appendMessage("bot", formatMarkdownReply(fallback), fallback);
    }
  }

  // Simple Markdown & Equation Formatter
  function formatMarkdownReply(text) {
    if (!text) return "";
    let html = text
      .replace(/### (.*?)\n/g, '<h4 style="color:#fff;margin:0.5rem 0 0.35rem 0;font-size:1.05rem;">$1</h4>')
      .replace(/## (.*?)\n/g, '<h3 style="color:#10b981;margin:0.75rem 0 0.4rem 0;font-size:1.15rem;">$1</h3>')
      .replace(/\*\*(.*?)\*\*/g, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/g, '<em>$1</em>')
      .replace(/```([\s\S]*?)```/g, '<pre style="background:var(--bg-deep);padding:0.75rem;border-radius:6px;overflow-x:auto;"><code>$1</code></pre>')
      .replace(/`([^`]+)`/g, '<code style="background:rgba(255,255,255,0.1);padding:2px 5px;border-radius:4px;font-family:monospace;">$1</code>')
      .replace(/\n\n/g, '<br><br>')
      .replace(/\n/g, '<br>');
    return html;
  }

  // Voice Input Setup (Speech-to-Text)
  function setupSpeechRecognition() {
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
    if (!SpeechRecognition) return;

    recognitionInstance = new SpeechRecognition();
    recognitionInstance.continuous = false;
    recognitionInstance.interimResults = true;
    recognitionInstance.lang = "en-US";

    const input = document.getElementById("chatUserInput");
    const micBtn = document.getElementById("chatMicBtn");

    recognitionInstance.onstart = () => {
      isListening = true;
      if (micBtn) {
        micBtn.classList.add("listening");
        micBtn.innerHTML = '<span class="mic-pulse"></span><span style="font-size:0.75rem;">Listening...</span>';
      }
      if (input) input.placeholder = "Listening... Speak your chemistry question now.";
    };

    recognitionInstance.onresult = (event) => {
      let transcript = "";
      for (let i = event.resultIndex; i < event.results.length; i++) {
        transcript += event.results[i][0].transcript;
      }
      if (input) input.value = transcript;
    };

    recognitionInstance.onerror = (event) => {
      console.warn("Speech recognition error:", event.error);
      stopListening();
    };

    recognitionInstance.onend = () => {
      stopListening();
      if (input && input.value.trim()) {
        window.handleChatSubmit();
      }
    };
  }

  function startListening() {
    if (!recognitionInstance) {
      setupSpeechRecognition();
    }
    if (!recognitionInstance) {
      alert("Speech recognition is not supported in this browser. Please try Chrome, Edge, or Safari.");
      return;
    }
    try {
      recognitionInstance.start();
    } catch (e) {
      recognitionInstance.stop();
    }
  }

  function stopListening() {
    isListening = false;
    const micBtn = document.getElementById("chatMicBtn");
    const input = document.getElementById("chatUserInput");
    if (micBtn) {
      micBtn.classList.remove("listening");
      micBtn.innerHTML = `
        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
          <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
          <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
          <line x1="12" y1="19" x2="12" y2="23"/>
          <line x1="8" y1="23" x2="16" y2="23"/>
        </svg>
      `;
    }
    if (input) input.placeholder = "Ask anything in chemistry (e.g. balance equations, reaction mechanisms)...";
  }

  // Voice Output Setup (Text-to-Speech)
  function cleanSpeechText(raw) {
    if (!raw) return "";
    let s = decodeURIComponent(raw);
    // Replace chemical formula subscripts with spoken words
    s = s.replace(/H₂O/g, "H 2 O")
         .replace(/CO₂/g, "C O 2")
         .replace(/CH₄/g, "C H 4")
         .replace(/H₂SO₄/g, "H 2 S O 4")
         .replace(/O₂/g, "oxygen gas")
         .replace(/N₂/g, "nitrogen gas")
         .replace(/ΔH/g, "delta H")
         .replace(/ΔG/g, "delta G")
         .replace(/ΔS/g, "delta S")
         .replace(/→/g, "produces")
         .replace(/⇌/g, "is in equilibrium with");
    return s;
  }

  // Global Exposed Functions
  window.handleChatSubmit = function(e) {
    if (e) e.preventDefault();
    const input = document.getElementById("chatUserInput");
    if (!input) return;
    const text = input.value.trim();
    if (!text) return;
    input.value = "";
    sendMessage(text);
  };

  window.sendQuickPrompt = function(promptText) {
    sendMessage(promptText);
  };

  window.setChatStyle = function(styleKey) {
    currentResponseStyle = styleKey;
    document.querySelectorAll(".chat-style-pill").forEach((pill) => {
      pill.classList.toggle("active", pill.getAttribute("data-style") === styleKey);
    });
  };

  window.clearChatHistory = function() {
    conversationHistory = [];
    const container = document.getElementById("chatMessagesArea");
    if (container) {
      container.innerHTML = `
        <div class="chat-message bot">
          <div class="chat-avatar">AI</div>
          <div class="chat-bubble">
            <p><strong>Hello! I am ChemAI, your intelligent AI Chemistry Tutor &amp; Research Companion.</strong></p>
            <p>I can help you balance chemical equations, resolve $S_N1/S_N2$ reaction mechanisms, compute stoichiometry, analyze 3D molecular geometries, and guide virtual laboratory experiments. What would you like to explore today?</p>
          </div>
        </div>
      `;
    }
  };

  window.regenerateLastResponse = function() {
    if (lastUserMessage) {
      sendMessage(lastUserMessage);
    }
  };

  window.toggleVoiceInput = function() {
    if (isListening) {
      if (recognitionInstance) recognitionInstance.stop();
      stopListening();
    } else {
      startListening();
    }
  };

  window.speakTextMessage = function(btn) {
    if (!("speechSynthesis" in window)) {
      alert("Text-to-speech is not supported on this browser.");
      return;
    }
    const raw = btn.getAttribute("data-speech");
    const clean = cleanSpeechText(raw);

    window.speechSynthesis.cancel();
    const utterance = new SpeechSynthesisUtterance(clean);
    utterance.rate = 1.0;
    utterance.pitch = 1.0;
    window.speechSynthesis.speak(utterance);
  };

  window.copyMessageText = function(btn) {
    const bubble = btn.closest(".chat-bubble");
    if (!bubble) return;
    const text = bubble.innerText.replace(/Listen|Copy|Regenerate/g, "").trim();
    navigator.clipboard.writeText(text).then(() => {
      const orig = btn.innerHTML;
      btn.innerHTML = '<span>Copied!</span>';
      setTimeout(() => { btn.innerHTML = orig; }, 1500);
    });
  };

  window.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("chatForm");
    if (form) form.addEventListener("submit", window.handleChatSubmit);

    const clearBtn = document.getElementById("chatClearBtn");
    if (clearBtn) clearBtn.addEventListener("click", window.clearChatHistory);

    const micBtn = document.getElementById("chatMicBtn");
    if (micBtn) micBtn.addEventListener("click", window.toggleVoiceInput);

    setupSpeechRecognition();
  });
})();
'''

with open("js/ai-assistant.js", "w", encoding="utf-8") as f:
    f.write(js_code)

print("js/ai-assistant.js successfully updated with Gemini backend & voice assistant!")
