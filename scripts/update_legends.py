for fname in ["index.html", "periodic-table.html"]:
    with open(fname, "r", encoding="utf-8-sig") as f:
        c = f.read()
    old = '<button type="button" class="legend-pill cat-noble-gas" data-cat="noble-gas">Noble Gases</button>'
    new = old + '\n          <button type="button" class="legend-pill cat-lanthanide" data-cat="lanthanide">Lanthanides</button>\n          <button type="button" class="legend-pill cat-actinide" data-cat="actinide">Actinides</button>'
    if old in c and 'data-cat="lanthanide"' not in c:
        c = c.replace(old, new)
        with open(fname, "w", encoding="utf-8") as f:
            f.write(c)
        print(f"{fname} legend updated")
