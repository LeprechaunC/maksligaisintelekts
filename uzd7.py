import gensim.downloader as api


model = api.load("word2Vec-google-news-300")
words = ["māja", "dzīvoklis", "jūra"]

word_vectors = {word: model[word] for word in words}

vards1 = model.similarity("māja", "dzīvoklis")
vards2 = model.similarity("māja", "jūra")
vards3 = model.similarity("dzīvoklis", "jūra")

print(f"sakritība: {vards1}")
print(f"sakritība: {vards2}")
print(f"sakritība: {vards3}")
