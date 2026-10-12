import re
import os

input_path = "../data/raw/wiki_raw.txt"
output_path = "../data/processed/wiki_clean.txt"

WORD_LIMIT = 100000

print("Starting corpus cleaning...")

if not os.path.exists(input_path):
    print(f"[!] Error: Cannot find {input_path}")
    exit(1)

with open(input_path, "r", encoding="utf-8") as f:
    text = f.read()

text = text.lower()

words = re.findall(r'[^\W\d_]+', text)

if len(words) > WORD_LIMIT:
    words = words[:WORD_LIMIT]

os.makedirs("../data/processed", exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(" ".join(words))

print(f"Saved {len(words)} words to {output_path}")