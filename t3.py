# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, 
# которая проверяет счастливость билета.
# *Пример:*
# 385916 -> yes
# 123456 -> no
n=int(input ('Введите номер билета'))
s1=0
s1=n%10+(n//10%10)+(n//100%10)
s2=0
s2=n//10000%10+n//100000+n//1000%10
print (s1)
print (s2)
if s1==s2:
    print ('Билет счастливый')
else:
    print ('Билет не счастливый')