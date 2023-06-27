#списки словари множетсва

# a1 = [1, 2, 3, 4, 10, -1]
# a2 = []
# for i in range(5,20,2):
#     a2.append(i)
# print(a2)
# a= ["a"*i for i in range(6)]
# print(a)
# print(min(a))
# print(max(a))
# # print(sum(a))
# print(len(a))

#key - неизменяемых типов данных
#изменяемые - list,set,dict,tuple

# dct = {4:"rt",}
# for i in range(5):
#     dct[i] = "qwe"
# print(dct)
# dct = {1 : "qwe" for i in range(6)}
# for key,val in dct.items():
#     print(key,val)

# a = set()
# a.add(3)
# a.add(3)
# print(a)


lst = [i for i in range(15000000)]

dct = {i: 1 for i in range(15000000)}

import time
start = time.perf_counter()
if 12000000 in lst:
    print(1)
end = time.perf_counter()
print("time to searct in list: ", end - start)

start = time.perf_counter()
if 12000000 in dct:
    print(2)
end = time.perf_counter()
print("time to searct in dct: ", end - start)
#0.1587
#0.0000076