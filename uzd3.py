import nltk
from nltk.tokenize import word_tokenize

teksts1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
teksts2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."


vardi1 = set(word.lower() for word in word_tokenize(teksts1) if word.isalnum())
vardi2 = set(word.lower() for word in word_tokenize(teksts2) if word.isalnum())


sakritibas = vardi1 & vardi2
total_words = len(vardi1 | vardi2)  #kopejais unikalo vardu skaits
sakritibas_procenti = (len(sakritibas) / total_words) * 100 if total_words > 0 else 0

print(f"Sakritības: {sakritibas}")
print(f"Sakritību procents: {sakritibas_procenti:.2f}")
