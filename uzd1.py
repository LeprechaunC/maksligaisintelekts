import nltk
from nltk.probability import FreqDist

#nltk.download('punkt') <- so biblioteku vajag

teikums = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

tokens = nltk.word_tokenize(teikums)
mazie_burti = [burts.lower() for burts in tokens if burts.isalnum()]

biezums = FreqDist(mazie_burti)

for word, count in biezums.items():
    print(f"'{word}': {count}")