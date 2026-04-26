

import os
os.system("cls")

# 1.m
# set1={"Artel","Alif","Yandex", "Google", "Meta"} 
# set2={"Google", "Apple", "Amazon", "Meta"}
# set3={"Alibaba", "Uzum", "Meta", "Google", "Amazon"}

# set4 = set1.intersection(set2)
# set5 = set1.intersection(set3)
# set6 = set4.intersection(set5)
# print("Umumiy elementlari: ",set6)
# set7 = set1.difference(set6)
# print("Faqat birinchi setda mavjud: ",set7)


# 2.m
# set1 = {2, 3, 4, 5, 6}
# set2 = {4, 5, 6, 7, 8, 9}
# sum=0
# set3 = set1.symmetric_difference(set2)

# for i in set3:
#     sum+=i
# print(sum)

# 3.m
# set1 = {100, 20, 45, 80, 70, 50}
# set2 = {30, 55, 70, 60, 20, 100}
# lst = []
# set3 = set1.intersection(set2)
# for i in set3:
#     if i>60:
#         lst.append(i)
# print(sum(lst)/len(lst))

# 4.m
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}
# lst1 = []
# set3 = set1.union(set2)

# for i in set3:
#     if i%2==0:
#         lst1.append(i)
# print(lst1)

# 5.m
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# set3 = {3, 4, 5}

# set4 = set1.intersection(set2)
# set5 = set3.intersection(set2)
# set4.update(set5)
# print(set4)

# 6.m
# set1 = {1, 3, 5, 6, 8}
# set2 = {3, 6, 9}
# k=1
# set1.difference_update(set2)
# for i in set1:
#     if i%2!=0:
#         k*=i
# print(k)

# 7.m
# ["olma", "nok", "olma", "uzum", "nok"]

# 8.m
# set1 = {2, 3, 4, 5}
# set2 = {3, 4, 5, 6}
# k=0
# s=0
# set3 = set1.intersection(set2)
# for i in set3:
#     k=i*i
#     s+=k
# print(s)

# 9.m
# set1 = {4, 7, 1, 9, 3, 6}
# lst = []
# a = max(set1)
# b = min(set1)
# set1.remove(a)
# set1.remove(b)
# for i in set1:
#     lst.append(i)
# print(sum(lst)/len(lst))


# 10.m
# set1 = {1, 2, 3}
# set2 = {2, 4, 5}
# set3 = {3, 5, 6}
# set4 = set1.difference(set2,set3)
# set5 = set2.difference(set1,set3)
# set6 = set3.difference(set1,set2)

# set7 = set4.union(set5,set6)
# print(set7)

# 11.m
# set1 = {1, 6, 3, 4}
# set2 = {3, 4, 5, 7}
# lst = []
# set3 = set1.symmetric_difference(set2)
# for i in set3:
#     lst.append(i)
# a = len(lst)
# if a%2==0:
#     print("Juft: ")
# else: 
#     print("Toq: ")

# 12.m
# set1 = {3, 5, 6, 9, 11, 12, 14}
# set2 = []

# for i in set1:
#     if i%3!=0:
#         set2.append(i)
# print(set2)

# 13.m
# set1 = {'a','b','c'}
# set2 = {'b','e','a'}
# set3 = set1.intersection(set2)
# a=0
# if len(set3)==0:
#     print("Umumiy element yoq: ")
# else: 
#     for i in set3:
#         a+=1
# print(a)
