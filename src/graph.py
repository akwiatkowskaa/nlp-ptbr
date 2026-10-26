import os
from collections import Counter, defaultdict

katalog_projektu = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(katalog_projektu, "data", "processed", "wiki_clean.txt")
rdzen_path = os.path.join(katalog_projektu, "data", "processed", "core.txt")
krawedzie_path = os.path.join(katalog_projektu, "data", "processed", "core_edges.txt")
wykres_path = os.path.join(katalog_projektu, "data", "processed", "core.png")

ILE_RDZENIA = 100

with open(input_path, "r", encoding="utf-8") as f:
    words = f.read().split()

pary = Counter(zip(words, words[1:]))
wychodzace = defaultdict(list)
for (a, b), waga in pary.items():
    wychodzace[a].append((b, waga))

rdzen = sorted(wychodzace, key=lambda w: (-len(wychodzace[w]), w))[:ILE_RDZENIA]

linie = []
linie.append("Rdzen jezyka")
linie.append("Waga krawedzi: ile razy ta para wystapila.")
linie.append(f"Wezly: {len(wychodzace)}")
linie.append(f"Krawedzie: {len(pary)}")
linie.append(f"Rdzen: {ILE_RDZENIA} wyrazow z najwieksza liczba krawedzi wychodzacych")
linie.append("")
linie.append(f"{'miejsce':>8}  {'wyraz':<20}{'krawedzie':>12}{'suma_wag':>12}")
linie.append("-" * 56)

for miejsce, wyraz in enumerate(rdzen, start=1):
    sasiedzi = wychodzace[wyraz]
    suma_wag = sum(waga for _, waga in sasiedzi)
    linie.append(f"{miejsce:>8}  {wyraz:<20}{len(sasiedzi):>12}{suma_wag:>12}")

with open(rdzen_path, "w", encoding="utf-8") as f:
    f.write("\n".join(linie) + "\n")

krawedzie = []
krawedzie.append("Krawedzie wychodzace z rdzenia")
krawedzie.append("wyraz_a wyraz_b waga")
for wyraz in rdzen:
    sasiedzi = sorted(wychodzace[wyraz], key=lambda x: (-x[1], x[0]))
    for nastepny, waga in sasiedzi:
        krawedzie.append(f"{wyraz} {nastepny} {waga}")

with open(krawedzie_path, "w", encoding="utf-8") as f:
    f.write("\n".join(krawedzie) + "\n")

print("\n".join(linie[:20]))
print("...")
print(f"Zapisano: {rdzen_path}")
print(f"Zapisano: {krawedzie_path}")

try:
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    top = rdzen[:20]
    nazwy = list(reversed(top))
    wartosci = [len(wychodzace[w]) for w in nazwy]

    plt.figure()
    plt.barh(nazwy, wartosci)
    plt.xlabel("liczba krawedzi wychodzacych")
    plt.tight_layout()
    plt.savefig(wykres_path, dpi=150)
    plt.close()
    print(f"Wykres: {wykres_path}")
except ImportError:
    print("Brak matplotlib, wykres pominiety.")