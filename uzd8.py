import nltk
from nltk import word_tokenize, pos_tag, ne_chunk


nltk.download('punkt')
nltk.download('maxent_ne_chunker')
nltk.download('words')


text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

tokens = word_tokenize(text)
tagged_tokens = pos_tag(tokens)


tree = ne_chunk(tagged_tokens)

# Funkcija, kas izvada personvārdus un organizācijas
def extract_entities(tree):
    person_names = []
    organizations = []
    for subtree in tree:
        if isinstance(subtree, nltk.Tree):
            entity = " ".join(word for word, tag in subtree)
            if subtree.label() == 'GPE':  #gpe - lokacija
                organizations.append(entity)
            elif subtree.label() == 'PERSON': #personas vards utt
                person_names.append(entity)

    return person_names, organizations
persons, orgs = extract_entities(tree)

print("Personvārdi:", persons)
print("Organizācijas:", orgs)
