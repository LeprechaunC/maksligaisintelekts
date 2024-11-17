import goslate
gs = goslate.Goslate()

text1 = "Labdien! Kā jums klājas?"
text2 =  "Es šodien lasīju interesantu grāmatu."

print(gs.translate(text1, 'eng'))
print(gs.translate(text2, 'eng'))