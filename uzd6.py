import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist

text = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām.
Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai.
Tā ir viena no Eiropas Savienības dalībvalstīm.
"""


def summarize_text(text):
    sentences = sent_tokenize(text)

    stop_words = set(stopwords.words("Latvija"))

    words = nltk.word_tokenize(text)
    words = [word.lower() for word in words if word.isalnum() and word not in stop_words]

    freq_dist = FreqDist(words)

    importantSentences = []
    for sentence in sentences:
        totalScore = 0
        for word in nltk.word_tokenize(sentence.lower()):
            if word in freq_dist:
                totalScore += freq_dist[word]
        if totalScore > 0:
            importantSentences.append((totalScore, sentence))

    importantSentences.sort(reverse=True, key=lambda x: x[0])
    summary = ' '.join([sentence for totalScore, sentence in importantSentences[:3]])  #svarigakie 3 teikumi
    return summary


summary = summarize_text(text)
print("Rezume:", summary)
