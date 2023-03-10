# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. 
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

ticket = int(input('Введите номер биллета: -> '))

if 99999 < ticket > 100000:
    number1 = ticket % 10
    number2 = (ticket // 10) % 10
    number3 = (ticket // 100) % 10
    number4 = (ticket // 1000) % 10
    number5 = (ticket // 10000) % 10
    number6 = (ticket // 100000) % 10
    if number1 + number2 + number3 == number4 + number5 + number6:
        print('Биллет счастливый')
    else:
        print('Биллет не счастливый')

else:
    print('Это номер биллета?')