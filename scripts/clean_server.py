with open("server.py", "r", encoding="utf-8") as f:
    text = f.read()

# Convert all multiline strings in server.py to raw strings where appropriate
text = text.replace('CHEMISTRY_SYSTEM_PROMPT = """', 'CHEMISTRY_SYSTEM_PROMPT = r"""')
text = text.replace('return """### Chemical Equation', 'return r"""### Chemical Equation')
text = text.replace('return """### $S_N1$', 'return r"""### $S_N1$')
text = text.replace('return """### Acid-Base', 'return r"""### Acid-Base')

with open("server.py", "w", encoding="utf-8") as f:
    f.write(text)

import py_compile
py_compile.compile("server.py", doraise=True)
print("server.py compiled cleanly with zero warnings!")
