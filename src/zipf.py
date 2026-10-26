import math
import os
from collections import Counter

katalog_projektu = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(katalog_projektu, "data", "processed", "wiki_clean.txt")
output_path = os.path.join(katalog_projektu, "data", "processed", "zipf.txt")
wykres_path = os.path.join(katalog_projektu, "data", "processed", "zipf.png")

with open(input_path, "r", encoding="utf-8") as f:
    words = f.read().split()

ranking = Counter(words).most_common()
suma = len(words)

xs = []
ys = []
linie = []
linie.append("Prawo Zipfa")
linie.append(f"Liczba slow: {suma}")
linie.append(f"Rozne wyrazy: {len(ranking)}")
linie.append("Wzor: liczba wystapien * ranga jest w przyblizeniu stala.")
linie.append("Na wykresie log-log punkty ida wzdluz prostej o nachyleniu -1.")
linie.append("")
linie.append(f"{'ranga':>6}  {'wyraz':<20}{'liczba':>10}{'czestotliwosc':>16}{'ranga*liczba':>14}")
linie.append("-" * 70)

for ranga, (wyraz, ile) in enumerate(ranking, start=1):
    xs.append(math.log(ranga))
    ys.append(math.log(ile))
    procent = ile / suma * 100
    linie.append(f"{ranga:>6}  {wyraz:<20}{ile:>10}{procent:>15.2f}%{ranga * ile:>14}")

n = len(xs)
sx = sum(xs)
sy = sum(ys)
sxx = sum(x * x for x in xs)
sxy = sum(x * y for x, y in zip(xs, ys))
nachylenie = (n * sxy - sx * sy) / (n * sxx - sx * sx)
linie.insert(3, f"Nachylenie prostej log-log: {nachylenie:.3f}")

tekst = "\n".join(linie) + "\n"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(tekst)

print("\n".join(linie[:12]))
print("...")
print(f"Zapisano: {output_path}")

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    rangi = list(range(1, len(ranking) + 1))
    liczby = [ile for _, ile in ranking]
    wzor = [liczby[0] / r for r in rangi]

    plt.figure()
    plt.loglog(rangi, liczby, ".", markersize=3, label="korpus")
    plt.loglog(rangi, wzor, label="Zipf, 1/r")
    plt.xlabel("ranga")
    plt.ylabel("liczba wystapien")
    plt.legend()
    plt.tight_layout()
    plt.savefig(wykres_path, dpi=150)
    plt.close()
    print(f"Wykres: {wykres_path}")
except ImportError:
    print("Brak matplotlib, wykres pominiety.")