# Дана последовательность из N целых чисел и число 
# K. Необходимо сдвинуть всю последовательность 
# (сдвиг - циклический) на K элементов вправо, K – 
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# list1 = [1,2,3,4,5,6]
# k=0
# list2=[]
# for i in range (len(list1)):
#     if i>=len(list1) :
#         k=list1[i]
#         list1[i]=list1[len(list1)-2]
#         list1[len(list1)-2]=k
#     if i<len(list1):
#         k=list1[i]
#         list1[i]=list1[i+3]
#         list1[i+3]=k
  
# print (list1)
       
#        list_1 = [1, 2, 3, 4, 5]
# k = 3
# for i in range(k):
#     list_1.insert(0,list_1.pop())
# print(list_1) 
        
# list_1 = [1, 2, 3, 4, 5]
# k = 3

# p1 = list_1[-k:]
# p2 = list_1[:-k]
# print(p1+p2)
        
k = 3
lst_1 = [1, 2, 3, 4, 5]
lst_2 = []
for i in range(len(lst_1)):
    if len(lst_1) > i + k:
        lst_2.insert(i + k, lst_1[i])
    else:
        lst_2.insert(k + i -len(lst_1), lst_1[i])
print(lst_2)
    