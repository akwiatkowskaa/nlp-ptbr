import os
from collections import Counter

katalog_projektu = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(katalog_projektu, "data", "processed", "wiki_clean.txt")
output_path = os.path.join(katalog_projektu, "data", "processed", "coverage.txt")
wykres_path = os.path.join(katalog_projektu, "data", "processed", "coverage.png")

PROG = 0.90

with open(input_path, "r", encoding="utf-8") as f:
    words = f.read().split()

ranking = Counter(words).most_common()
suma = len(words)

zebrane = 0
wybrane = []
for wyraz, ile in ranking:
    zebrane += ile
    wybrane.append((wyraz, ile, zebrane))
    if zebrane / suma >= PROG:
        break

linie = []
linie.append("Najczestsze wyrazy")
linie.append(f"Liczba slow: {suma}")
linie.append(f"Rozne wyrazy: {len(ranking)}")
linie.append(f"Prog: {PROG * 100:.0f}% wystapien w tekscie")
linie.append(f"Wyrazow w progu: {len(wybrane)}")
linie.append(f"To jest {len(wybrane) / len(ranking) * 100:.1f}% slownika")
linie.append("")
linie.append(f"{'miejsce':>8}  {'wyraz':<20}{'liczba':>10}{'skumulowane':>14}{'udzial':>10}")
linie.append("-" * 66)

for miejsce, (wyraz, ile, skumulowane) in enumerate(wybrane, start=1):
    udzial = skumulowane / suma * 100
    linie.append(f"{miejsce:>8}  {wyraz:<20}{ile:>10}{skumulowane:>14}{udzial:>9.2f}%")

with open(output_path, "w", encoding="utf-8") as f:
    f.write("\n".join(linie) + "\n")

print("\n".join(linie[:8]))
print(f"Zapisano: {output_path}")

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    udzialy = []
    narastajaco = 0
    for _, ile in ranking:
        narastajaco += ile
        udzialy.append(narastajaco / suma * 100)

    plt.figure()
    plt.plot(range(1, len(udzialy) + 1), udzialy)
    plt.axhline(PROG * 100, linestyle="--", label=f"{PROG * 100:.0f}%")
    plt.axvline(len(wybrane), linestyle=":", label=f"{len(wybrane)} wyrazow")
    plt.xlabel("liczba najczestszych wyrazow")
    plt.ylabel("udzial w tekscie (%)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(wykres_path, dpi=150)
    plt.close()
    print(f"Wykres: {wykres_path}")
except ImportError:
    print("Brak matplotlib, wykres pominiety.")