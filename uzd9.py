from nltk.parse.generate import generate
from nltk import CFG

grammar = CFG.fromstring("""
      S -> 'Reiz' 'kādā' 'tālā' 'zemē' VP
      VP -> V NP | V NP PP | V S | V PP
      V -> 'dzīvoja' | 'aizskrēja' | 'piedzīvoja' | 'gāja' | 'lidoja'
      NP -> Det N | Det N PP | N
      PP -> P NP
      Det -> 'viens' | 'katra' | 'kāds' | 'dažādi'
      N -> 'zaķis' | 'mežs' | 'pasaules' | 'kalns' | 'debesis'
      P -> 'pār' | 'pa' | 'caur'
    """)

generated_sentences = generate(grammar, n=2)
for sentence in generated_sentences:
    print(' '.join(sentence))
