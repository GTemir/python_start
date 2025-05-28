#def summa(a, b):   	 			# В этой функции мы создали функцию с названием SUMMA которая принимает 2е переменные
#	res = a + b     			# далее плюсует две переменные и выводит результат
#	print("Result: ", res)
#summa(8, 6)
#summa(int(input("Введите число A: ")), int(input("Введите число B: ")))


#def summa(a, b):
#	return = a + b   			# такая же функция как и в первом случае но тут вы не выводим результат сразу мы ВОЗВРАЩАЕМ res которую можно применять ВНЕ функции
#
#res = summa(5.4, 1.6)
#print (res)



def minimal(l):					#Функция для поиска минимального значения в списке. Создав функцию которой можно пользоваться при поиске элемента не печатая снова тотже код
	min_n = l[0]
	for el in l:
		if el < min_n:
			min_n = el

	return min_n

nums1=[31, 54, 3, 1.3]
min1=minimal(nums1)
print(min1)
nums2 = [1234, 76567, 123, 1.0, -7]
min2=minimal(nums2)
print(min2)

if min1 < min2:
	print(mun1)
else:
	print(min2)


func = lambda x, y: x * y

print(func(3, 5))
