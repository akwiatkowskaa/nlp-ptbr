import wikipediaapi
import os

user_agent = "nlp-ptbr-analysis"
wiki = wikipediaapi.Wikipedia(user_agent=user_agent, language="pt")

#PT-BR variant
topics = [
    "Brasil", "História do Brasil", "Amazônia", "São Paulo", 
    "Rio de Janeiro", "Cultura do Brasil", "Futebol do Brasil", 
    "Carnaval do Brasil", "Geografia do Brasil", "Economia do Brasil", "Música do Brasil"
]

WORD_TARGET = 100000
collected_words = 0
collected_text = ""

print("Starting Wikipedia data extraction (PT-BR)...")

for topic in topics:
    if collected_words >= WORD_TARGET:
        break
        
    try:
        print(f"Downloading: {topic}...")
        page = wiki.page(topic)
        
        if page.exists():
            text = page.text
            collected_text += text + "\n\n"
            
            word_count = len(text.split())
            
            collected_words += word_count
            
            print(f" -> Added {word_count} words. Total: {collected_words}/{WORD_TARGET}")
        else:
            print(f" [!] Topic '{topic}' not found.")
            
    except Exception as e:
        print(f" [!] Error fetching '{topic}': {e}")

katalog_projektu = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
output_path = os.path.join(katalog_projektu, "data", "raw", "wiki_raw.txt")
os.makedirs(os.path.dirname(output_path), exist_ok=True)

with open(output_path, "w", encoding="utf-8") as f:
    f.write(collected_text)

print(f"\nSaved {collected_words} words to {output_path}")