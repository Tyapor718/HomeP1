# Дан список чисел. Определите, сколько в нем 
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


# list1 = [1, 1, 2, 0, -1, 3, 4, 4]
# set1 = set (list1)
# print (set1)
# print (len(set1))

# list_1 = [1, 2, 3, 1, 1, 5, 10, 20, 20, 30]

# for i in list_1:
#     if list_1.count(i)>1:
#         for _ in range(list_1.count(i)-1):
#             list_1.remove(i)
# print(list_1)

lst_1 = [1, 1, 2, 0, -1, 3, 4, 4]
lst_2 = []
for i in lst_1:
    if i not in lst_2:
        lst_2.append(i)
print(lst_2)