# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, 
# а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, 
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть
n=int (input ('Введите количество монет'))
o= int (input ('Введите количество монет орлом вверх'))
r=int (input ('Введите количество монет решкой вверх'))
if o>=r :
    print ('Минимальное количество монет для переворота ', r )
else :
    print ('Минимальное количество монет для переворота ', o )
