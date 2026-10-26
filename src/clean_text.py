import re
import os

katalog_projektu = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
input_path = os.path.join(katalog_projektu, "data", "raw", "wiki_raw.txt")
output_path = os.path.join(katalog_projektu, "data", "processed", "wiki_clean.txt")

WORD_LIMIT = 100000

print("Starting corpus cleaning...")

if not os.path.exists(input_path):
    print(f"[!] Error: Cannot find {input_path}")
    exit(1)

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

text = text.lower()

ALFABET = set("abcdefghijklmnopqrstuvwxyzáàâãéêíóôõúç")

words = re.findall(r'[^\W\d_]+', text)
words = [w for w in words if all(c in ALFABET for c in w)]


if len(words) > WORD_LIMIT:
    words = words[:WORD_LIMIT]

os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(" ".join(words))

print(f"Saved {len(words)} words to {output_path}")