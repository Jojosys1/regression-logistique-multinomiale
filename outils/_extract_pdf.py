from pypdf import PdfReader
from pathlib import Path

for name in ["TP.pdf", "10.21037atm-2020-57-1.pdf"]:
    p = Path(name)
    print("\n" + "="*20 + f" {name} " + "="*20)
    r = PdfReader(str(p))
    print(f"pages={len(r.pages)}")
    for i, page in enumerate(r.pages[:4]):
        txt = (page.extract_text() or "").replace("\n", " ")
        print(f"\n--- page {i+1} ---")
        print(txt[:2500])
