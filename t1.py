# Задача 2: Найдите сумму цифр трехзначного числа.
# *Пример:*
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) | 



n=int(input ('Введите число'))
s=0
s=n%10+(n//10%10)+(n//100)
print (s)
 