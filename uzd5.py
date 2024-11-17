import re

raw_text = "@John: Sis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

def cleantext(text):
    text = text.lower()
    text = re.sub(r'http\S+', '', text)
    text = re.sub(r'[@!#]', '', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text



result = cleantext(raw_text)
print(result)
