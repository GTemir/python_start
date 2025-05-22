user_data = int(input("Введите чимло: "))

happiness= True

##If всегда вверху 
#if happiness and  user_data == 6: #Проверка двух условий одновременно оператором and
#	print ('user is happy')
#elif user_data == 5: # сколько угодно операторов elif может быть
#	print ('number is 5') 
#elif user_data == 7:
#        print ('number is 7')
#else: #Просто иное условие выполняется во всех остальных случаях
#	print ('user is not happy')







if happiness or user_data == 6 or 5 == 5: #Хотябы одно из условий верно оператором OR
        print ('user is happy')
elif user_data == 5: # сколько угодно операторов elif может быть
        print ('number is 5')
elif user_data == 7:
        print ('number is 7')
else: #Просто иное условие выполняется во всех остальных случаях
        print ('user is not happy')
#if user_data != 5:
#	print ('Number')
#	if user_data > 6:
#		print ('Nuber bigger than 6')
