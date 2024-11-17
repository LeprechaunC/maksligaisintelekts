from langdetect import detect

vards1 = "Šodien ir saulaina diena."
vards2 = "Today is a sunny day."
vards3 = "Сегодня солнечный день."

print(vards1 + " : " + detect(vards1))
print(vards2 + " : " + detect(vards2))
print(vards3 + " : " + detect(vards3))

