# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

total = int(input('Введите количество сделанных журавликов: -> '))

if total % 3 == 0:
    katya = (total // 3) * 2 
    petya = katya // 4
    sereja = katya // 4
    print(f'Катя сделала {katya} журавликов')
    print(f'Петя сделал {petya} журавликов')
    print(f'Сережа сделал {sereja} журавликов')

else:
    print('Введенное количество не подходит условию задачи')