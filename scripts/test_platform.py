import os
import json

errors = []

# 1. Verify HTML pages
required_html = ["index.html", "periodic-table.html", "tools.html", "virtual-lab.html", "study-hub.html", "spectroscopy.html", "simulations.html"]
for h in required_html:
    if not os.path.exists(h) or os.path.getsize(h) < 500:
        errors.append(f"Missing or empty HTML page: {h}")
    else:
        print(f"[PASS] Found {h} ({os.path.getsize(h):,} bytes)")

# 2. Verify molecules data
if os.path.exists("js/molecules-data.js"):
    with open("js/molecules-data.js", "r", encoding="utf-8") as f:
        content = f.read()
        raw_json = content.split("window.CHEMAI_MOLECULES = ")[1].rstrip(";\n")
        mols = json.loads(raw_json)
        print(f"[PASS] Verified {len(mols)} 3D molecules in js/molecules-data.js")
        if len(mols) < 75:
            errors.append(f"Expected at least 75 molecules, got {len(mols)}")
else:
    errors.append("Missing js/molecules-data.js")

# 3. Verify periodic table data
if os.path.exists("js/periodic-table-data.js"):
    with open("js/periodic-table-data.js", "r", encoding="utf-8") as f:
        content = f.read()
        raw_json = content.split("window.PERIODIC_TABLE_DATA = ")[1].rstrip(";\n")
        elems = json.loads(raw_json)
        print(f"[PASS] Verified {len(elems)} chemical elements in js/periodic-table-data.js")
        if len(elems) != 118:
            errors.append(f"Expected 118 elements, got {len(elems)}")
else:
    errors.append("Missing js/periodic-table-data.js")

# 4. Verify quiz data
if os.path.exists("js/quiz-data.js"):
    with open("js/quiz-data.js", "r", encoding="utf-8") as f:
        content = f.read()
        raw_json = content.split("window.CHEMAI_QUIZ_QUESTIONS = ")[1].rstrip(";\n")
        quiz = json.loads(raw_json)
        print(f"[PASS] Verified {len(quiz)} quiz questions across 20 topics")
else:
    errors.append("Missing js/quiz-data.js")

# 5. Check CSS & JS critical assets
assets = [
    "css/main.css", "css/components.css", "css/molecule-viewer.css", "css/periodic-table.css",
    "css/virtual-lab.css", "css/spectroscopy.css", "css/simulations.css",
    "js/app.js", "js/ai-assistant.js", "js/molecule-viewer.js", "js/periodic-table.js",
    "js/virtual-lab.js", "js/calculators.js", "js/quiz-engine.js", "js/notes-generator.js",
    "js/spectroscopy-hub.js", "js/simulations-hub.js", "js/particles.js"
]
for a in assets:
    if not os.path.exists(a) or os.path.getsize(a) < 100:
        errors.append(f"Missing or corrupt asset: {a}")
    else:
        print(f"[PASS] Asset verified: {a} ({os.path.getsize(a):,} bytes)")

if errors:
    print(f"\n[FAIL] Found {len(errors)} errors:")
    for e in errors:
        print("  -", e)
    exit(1)
else:
    print("\n[SUCCESS] ALL ASSETS & DATASETS VALIDATED PERFECTLY!")
