with open("index.html", "r", encoding="utf-8-sig") as f:
    c = f.read()

# Add response style pills and mic button
old_chat_input = """          <!-- Chat Input Bar -->
          <div class="chat-input-bar">
            <form id="chatForm" class="chat-form">
              <input type="text" id="chatUserInput" class="chat-input" placeholder="Ask any chemistry question or formula (e.g. 'What is the molar mass of H2SO4?' or 'Explain Gibbs free energy')..." autocomplete="off" required>
              <div class="chat-btn-group">
                <input type="file" id="chatImageUploadInput" accept="image/*" style="display:none;" onchange="handleImageSelected(event)">
                <button type="button" class="btn-icon" title="Upload chemistry problem image / screenshot" onclick="triggerImageUpload()" aria-label="Upload question image">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
                </button>
                <button type="submit" class="btn btn-primary btn-sm" aria-label="Send question">
                  <span>Send</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                </button>
              </div>
            </form>
          </div>"""

new_chat_input = """          <!-- Response Style Selector -->
          <div style="padding: 0 1.5rem; display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 0.5rem; margin-top: 0.5rem;">
            <div style="font-size: 0.78rem; color: var(--text-dim); font-weight: 700; text-transform: uppercase;">Response Style:</div>
            <div class="chat-style-pills">
              <button type="button" class="chat-style-pill" data-style="simple" onclick="setChatStyle('simple')">Simple Explanation</button>
              <button type="button" class="chat-style-pill active" data-style="detailed" onclick="setChatStyle('detailed')">Detailed Academic</button>
              <button type="button" class="chat-style-pill" data-style="exam" onclick="setChatStyle('exam')">Exam Preparation</button>
              <button type="button" class="chat-style-pill" data-style="numerical" onclick="setChatStyle('numerical')">Step-by-Step Numerical</button>
            </div>
          </div>

          <!-- Chat Input Bar -->
          <div class="chat-input-bar">
            <form id="chatForm" class="chat-form">
              <button type="button" id="chatMicBtn" class="chat-mic-btn" title="Speak question with voice" aria-label="Voice input">
                <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <path d="M12 1a3 3 0 0 0-3 3v8a3 3 0 0 0 6 0V4a3 3 0 0 0-3-3z"/>
                  <path d="M19 10v2a7 7 0 0 1-14 0v-2"/>
                  <line x1="12" y1="19" x2="12" y2="23"/>
                  <line x1="8" y1="23" x2="16" y2="23"/>
                </svg>
              </button>
              <input type="text" id="chatUserInput" class="chat-input" placeholder="Ask anything in chemistry or click the mic to speak..." autocomplete="off" required>
              <div class="chat-btn-group">
                <input type="file" id="chatImageUploadInput" accept="image/*" style="display:none;" onchange="handleImageSelected(event)">
                <button type="button" class="btn-icon" title="Upload chemistry problem image / screenshot" onclick="triggerImageUpload()" aria-label="Upload question image">
                  <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
                </button>
                <button type="submit" class="btn btn-primary btn-sm" aria-label="Send question">
                  <span>Send</span>
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
                </button>
              </div>
            </form>
          </div>"""

if old_chat_input in c:
    c = c.replace(old_chat_input, new_chat_input)
    with open("index.html", "w", encoding="utf-8") as out:
        out.write(c)
    print("index.html chat input updated with voice and response styles!")
else:
    print("Error: Could not locate old_chat_input in index.html")
