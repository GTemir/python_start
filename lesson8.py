word = str(input("Какие у вас хобби: \n"))
#print (len(word)) #Для строк справедливы некоторые функции списков
#print (word.count('y'))
# Есть функции применимые исключительно к строкам
#print (word.upper()) # isupper выведет значение True или False, как вопрос все ли в верхнем ресгистре
#print (word.lower()) # islower выведет значение True или False, как вопрос все ли в нижнем регистре
#print (word.find('g'))

hopa = word.split(" ")
#print (hopa[1])

for i in range(len(hopa)):
	hopa[i] = hopa[i].capitalize()
result = ", ".join(hopa)
print (result)
