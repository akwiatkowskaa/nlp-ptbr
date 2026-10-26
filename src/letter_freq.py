import os
from collections import Counter

katalog_projektu = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(katalog_projektu, "data", "processed", "wiki_clean.txt")
output_path = os.path.join(katalog_projektu, "data", "processed", "letter_freq.txt")

ALFABET = "aáàâãbcçdeéêfghiíjklmnoóôõpqrstuúvwxyz"

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

words = text.split()
litery = Counter(c for w in words for c in w)
suma = sum(litery.values())

def wiersz(litera, ile):
    procent = ile / suma * 100
    return f"{litera:<8}{ile:>10}{procent:>15.2f}%"

naglowek = f"{'litera':<8}{'liczba':>10}{'czestotliwosc':>16}"
linia = "-" * 34

linie = []
linie.append("Analiza liter")
linie.append(f"Liczba slow: {len(words)}")
linie.append(f"Liczba liter: {suma}")
linie.append("")
linie.append("1. Alfabet")
linie.append(naglowek)
linie.append(linia)
for litera in ALFABET:
    linie.append(wiersz(litera, litery[litera]))

linie.append("")
linie.append("2. Od najczestszej")
linie.append(naglowek)
linie.append(linia)
for litera, ile in sorted(litery.items(), key=lambda x: (-x[1], x[0])):
    linie.append(wiersz(litera, ile))

tekst = "\n".join(linie) + "\n"

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8") as f:
    f.write(tekst)

print(tekst)
print(f"Zapisano: {output_path}")