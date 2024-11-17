import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
import nltk
#nltk.download('vader_lexicon')

sia = SentimentIntensityAnalyzer()

teksts1 = "Šis produkts ir lielisks, esmu ļoti apmierināts!"
teksts2 = "Esmu vīlies, produkts neatbilst aprakstam."
teksts3 = "Neitrāls produkts, nekas īpašs."

print(sia.polarity_scores(teksts1))
print(sia.polarity_scores(teksts2))
print(sia.polarity_scores(teksts3))
