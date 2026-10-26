# NLP PT-BR Analysis

Analiza portugalskiego brazylijskiego na tekstach z Wikipedii. Po czyszczeniu korpus - 100 000 słów.

## Co już jest zrobione

- **Korpus.** Artykuły zbiera `src/wiki_download.py`. `src/clean_text.py` zamienia tekst na małe litery, zostawia same słowa i ucina wynik do 100 000. Gotowy tekst: `data/processed/wiki_clean.txt`.
- **Alfabet.** W korpusie zostają litery portugalskie, razem ze znakami `á à â ã é ê í ó ô õ ú ç` oraz `k`, `w`, `y`. Słowa z obcymi znakami są usuwane.
- **Częstość liter.** `src/letter_freq.py` zapisuje tabelę do `data/processed/letter_freq.txt`. Najczęstsze litery to `a` (12,61%), `e` (11,08%) i `o` (10,45%).
- **Prawo Zipfa.** `src/zipf.py`. W tekście jest 12 983 różnych wyrazów. Nachylenie prostej na wykresie log-log wynosi **-1,030** (wzorzec to -1), więc prawo jest spełnione w przybliżeniu. Wynik: `zipf.txt`, `zipf.png`.
- **Najczęstsze wyrazy.** `src/coverage.py`. **4 655** wyrazów (35,9% słownika) pokrywa 90% wystąpień w tekście. Wynik: `coverage.txt`, `coverage.png`.
- **Graf sąsiedztwa.** `src/graph.py`. Węzeł to wyraz. Krawędź `A → B` znaczy, że `B` stoi tuż po `A`, a waga to liczba takich par. Graf ma 12 982 węzłów i 56 954 krawędzi. Rdzeń języka to 100 wyrazów z największą liczbą krawędzi wychodzących. Na czele są `de`, `e`, `a` i `o`. Wynik: `core.txt`, `core_edges.txt`, `core.png`.

