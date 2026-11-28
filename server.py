"""
ChemAI Platform - High-Performance AI Chemistry Backend
Provides Gemini API integration, AI Notes generation, and static file serving.
"""

import os
import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from typing import List, Optional, Dict, Any

# Load .env file if present
env_path = Path(".env")
if env_path.exists():
    with open(env_path, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip())

GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY", "")

# Initialize FastAPI app
app = FastAPI(title="ChemAI Platform API", version="2.0.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# System Prompt for ChemAI Chemistry Assistant
CHEMISTRY_SYSTEM_PROMPT = r"""You are ChemAI, an elite AI Chemistry Tutor, Scientific Assistant, and Molecular Researcher inspired by chemai.in.
Your goal is to guide students, educators, and researchers in mastering chemistry.

Guidelines:
1. Scientific Accuracy: Always ensure stoichiometric balances, exact IUPAC nomenclature, realistic thermodynamics, and valid reaction mechanisms. Never hallucinate fake chemical reactions or citations.
2. Formulas & Mathematics: Format chemical equations and math clearly using LaTeX math syntax (e.g. $PV = nRT$, $\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$, or chemical reactions like $\\text{CH}_4 + 2\\text{O}_2 \\to \\text{CO}_2 + 2\\text{H}_2\\text{O}$).
3. Structured Steps: When answering numerical problems (stoichiometry, equilibrium, pH, thermodynamics), provide clear numbered steps with given values, formulas used, unit substitutions, and final answers with units highlighted.
4. Response Styles:
   - "simple": Explain intuitively with simple analogies, avoiding excessive jargon.
   - "detailed": Provide in-depth academic explanations covering molecular orbital theory, thermodynamics, kinetics, and mechanism steps.
   - "exam": Provide high-yield bulleted points, standard definitions, exam tips, and common pitfalls.
   - "numerical": Provide formal step-by-step mathematical solutions with formulas and unit dimensional analysis.
5. Tone: Encouraging, intellectually rigorous, precise, and scientifically authoritative."""

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    message: str
    style: Optional[str] = "detailed"
    history: Optional[List[ChatMessage]] = []

class NotesRequest(BaseModel):
    topic: Optional[str] = "General Chemistry"
    branch: Optional[str] = "General Chemistry"
    style: Optional[str] = "summary"
    level: Optional[str] = "AP / Undergraduate Chemistry"

@app.get("/api/health")
def health_check():
    has_key = bool(os.environ.get("GEMINI_API_KEY"))
    return {
        "status": "healthy",
        "has_api_key": has_key,
        "model": "gemini-2.5-flash" if has_key else "offline-expert-engine"
    }

@app.post("/api/chat")
def chat_endpoint(req: ChatRequest):
    api_key = os.environ.get("GEMINI_API_KEY", "")

    style_instructions = {
        "simple": "Provide a simple, clear, intuitive explanation suitable for beginners.",
        "detailed": "Provide a comprehensive, university-level explanation with reaction mechanisms and theory.",
        "exam": "Provide structured exam-oriented revision notes, key formulas, and high-yield test points.",
        "numerical": "Provide a step-by-step numerical solution with clear formulas, substitutions, and units."
    }.get(req.style, "Provide a clear and accurate explanation.")

    if api_key:
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=api_key)

            # Build contents
            prompt_text = f"Response Style: {style_instructions}\n\nStudent Query: {req.message}"
            
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt_text,
                config=types.GenerateContentConfig(
                    system_instruction=CHEMISTRY_SYSTEM_PROMPT,
                    temperature=0.3
                )
            )

            reply_text = response.text or "I could not generate an answer for that chemistry problem."
            return {"reply": reply_text, "source": "gemini"}

        except Exception as e:
            # Fall back to offline knowledge engine on API failure
            print(f"Gemini API Exception: {e}", file=sys.stderr)
            return {
                "reply": generate_offline_fallback(req.message, req.style),
                "source": "fallback",
                "note": f"Served via ChemAI Scientific Engine (Gemini error: {str(e)[:60]}...)"
            }

    # If no API key configured, use built-in expert chemistry knowledge engine
    return {
        "reply": generate_offline_fallback(req.message, req.style),
        "source": "fallback",
        "note": "Served via ChemAI Built-in Scientific Engine. To enable live Gemini, set GEMINI_API_KEY in .env"
    }

@app.post("/api/generate-notes")
def generate_notes_endpoint(req: NotesRequest):
    topic = req.topic or req.branch or "General Chemistry"
    branch = req.branch or req.topic or "General Chemistry"
    style = req.style or "summary"
    level = req.level or "AP / Undergraduate Chemistry"
    api_key = os.environ.get("GEMINI_API_KEY", "")

    if api_key:
        try:
            from google import genai
            from google.genai import types

            client = genai.Client(api_key=api_key)
            prompt = f"""Generate comprehensive chemistry study notes for:
Topic: {topic}
Branch: {branch}
Academic Level: {level}
Format / Style: {style}

Include:
1. Introduction & Overview
2. Key Concepts & Principles
3. Important Definitions
4. Chemical Equations & Reaction Mechanisms (in LaTeX)
5. Mathematical Formulas & Laws
6. Solved Numerical Examples
7. Real-world & Industrial Applications
8. High-yield Exam Summary & Review Practice Questions."""

            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=CHEMISTRY_SYSTEM_PROMPT,
                    temperature=0.2
                )
            )

            return {"notes": response.text or "# " + req.topic, "source": "gemini"}
        except Exception as e:
            print(f"Gemini Notes error: {e}", file=sys.stderr)

    # Built-in structured notes fallback
    return {
        "notes": get_structured_notes_fallback(req.topic, req.branch),
        "source": "fallback"
    }

def generate_offline_fallback(query: str, style: str) -> str:
    q = query.lower()
    
    if "balance" in q or "reaction" in q:
        return r"""### Chemical Equation Balancing (Law of Conservation of Mass)

To balance a chemical equation, equalize the atom count of each element on both sides:

$$4\\text{Fe (s)} + 3\\text{O}_2\\text{ (g)} \\longrightarrow 2\\text{Fe}_2\\text{O}_3\\text{ (s)}$$

**Step-by-Step Derivation:**
1. **Count Reactant Atoms:** $\\text{Fe} = 1$, $\\text{O} = 2$.
2. **Count Product Atoms:** $\\text{Fe} = 2$, $\\text{O} = 3$.
3. **Balance Oxygen First:** The LCM of 2 and 3 is 6. Multiply $\\text{O}_2$ by 3 and $\\text{Fe}_2\\text{O}_3$ by 2:
   $$\\text{Fe} + 3\\text{O}_2 \\longrightarrow 2\\text{Fe}_2\\text{O}_3$$
4. **Balance Iron:** Products now contain $2 \\times 2 = 4\\text{ Fe}$. Add coefficient 4 to reactant $\\text{Fe}$:
   $$4\\text{Fe} + 3\\text{O}_2 \\longrightarrow 2\\text{Fe}_2\\text{O}_3$$
5. **Thermodynamic Note:** This oxidation is exothermic with $\\Delta H^\circ = -1648\\text{ kJ/mol}$."""

    if "sn1" in q or "sn2" in q:
        return r"""### $S_N1$ vs $S_N2$ Nucleophilic Substitution Mechanisms

| Parameter | $S_N1$ (Substitution Nucleophilic Unimolecular) | $S_N2$ (Substitution Nucleophilic Bimolecular) |
| :--- | :--- | :--- |
| **Steps** | Two steps via carbocation intermediate | Single concerted transition state |
| **Kinetics** | First order: $\\text{Rate} = k[R-X]$ | Second order: $\\text{Rate} = k[R-X][Nu^-]$ |
| **Substrate Preference** | $3^\circ > 2^\circ \\gg 1^\circ$ (Carbocation stability) | $\\text{CH}_3 > 1^\circ > 2^\circ \\gg 3^\circ$ (Steric hindrance) |
| **Stereochemistry** | Racemization (retention + inversion) | 100% Walden Inversion (backside attack) |
| **Optimal Solvent** | Polar protic ($\text{H}_2\text{O}, \text{EtOH}, \text{MeOH}$) | Polar aprotic (Acetone, DMSO, DMF) |"""

    if "ph" in q or "acid" in q or "base" in q:
        return r"""### Acid-Base Equilibrium & pH Calculations

The pH is defined as the negative base-10 logarithm of hydrogen ion activity:

$$\\text{pH} = -\\log_{10}[\\text{H}^+]$$
$$\\text{pOH} = -\\log_{10}[\\text{OH}^-]$$
$$\\text{pH} + \\text{pOH} = 14.00 \\quad (\\text{at } 25^\circ\\text{C})$$

**Example:** For a $0.005\\text{ M } \\text{H}_2\\text{SO}_4$ solution:
- Since sulfuric acid donates $2\\text{ H}^+$ in dilute solution:
  $$[\\text{H}^+] = 2 \\times 0.005\\text{ M} = 0.010\\text{ M} = 1.0 \\times 10^{-2}\\text{ M}$$
- $\\text{pH} = -\\log_{10}(10^{-2}) = 2.00$
- Acidity Classification: **Strongly Acidic**."""

    return f"""### Chemistry Analysis: {query}

**Fundamental Principles:**
- Chemical processes follow thermodynamic spontaneity governed by Gibbs free energy: $\\Delta G = \\Delta H - T\\Delta S$.
- When $\\Delta G < 0$, reactions occur spontaneously.
- Molecular geometries depend on valence shell electron pair repulsion (VSEPR theory), minimizing electron pair repulsion.

**Interactive Tools Available:**
- Model this reaction in the **Calculators Dashboard**.
- Test live visual dynamics in the **Virtual Chemistry Lab**.
- Explore molecular geometries in the **3D Molecule Viewer**."""

def get_structured_notes_fallback(topic: str, branch: str) -> str:
    return f"""# {topic} — Comprehensive Study Notes
**Discipline:** {branch} · **Source:** ChemAI Verified Scientific Knowledgebase

---

## 1. Introduction & Overview
{topic} represents a core foundation of chemical sciences, describing how matter interacts, transforms, and organizes at the molecular and subatomic scale.

## 2. Key Theoretical Concepts
- **Governing Law:** Conservation of mass and energy dictates that all chemical transformations maintain stoichiometric balance.
- **Microscopic State:** Atoms and molecules interact through electrostatic Coulombic potentials, covalent orbital overlap, and dispersion forces.
- **Thermodynamic Spontaneity:** Evaluated by Gibbs free energy:
  $$\\Delta G^\\circ = -RT \\ln K_{{eq}}$$

## 3. Fundamental Formulas & Equations
$$\\text{{Rate}} = k[A]^m [B]^n$$
$$PV = nRT \\implies P = \\frac{{\\rho RT}}{{M}}$$
$$\\text{{pH}} = \\text{{pK}}_a + \\log_{{10}}\\left(\\frac{{[A^-]}}{{[HA]}}\\right)$$

## 4. Key Takeaways & Exam Tips
1. Always check stoichiometry and unit balance before calculating numerical values.
2. Remember that catalysts lower activation energy ($E_a$) but do not shift chemical equilibrium position ($K_{{eq}}$).
3. Electronegativity increases across a period from left to right and decreases down a group."""

# Mount static files at root
app.mount("/", StaticFiles(directory=".", html=True), name="static")

if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8080))
    host = os.environ.get("HOST", "127.0.0.1")
    print(f"Starting ChemAI Platform Server on http://{host}:{port}")
    uvicorn.run("server:app", host=host, port=port, reload=False)
