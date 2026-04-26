import os
os.system("cls")

# 1.m
# set1={1,2,3,4,5,6}
# set2={4,5,6,7,8,9}
# lst1 = []
# lst2 = []
# set3=set1.difference(set2)
# for i in set3:
#     lst1.append(i)
# set4 = set1.symmetric_difference(set3)
# for i in set4:
#     lst2.append(i)

# print(sum(lst2)-sum(lst1))


# 2.m
# set1={'olma', 'anor', 'youtube', 'instagram', 'gilos'}
# set2={'youtube', 'gilos', 'anor', 'BMW', 'Tesla', 'Nissan'}
# set3={'gilos', 'olma', 'instagram', 'Tesla', 'Nissan'}

# set4 = set1.intersection(set2)
# set5 = set4.difference(set3)
# print(set5)


# 3.m
# set1 = {1,2,3,4,5,6}
# set2 = {4,5,6,7,8,9}
# lst1 = []
# set3 = set1.symmetric_difference(set2)

# for i in set3:
#     lst1.append(i)
# print(lst1[::-1])


# 4.m
# ali = {"Toshkent", "Samarqand", "Buxoro", "Andijon"}
# vali = {"Toshkent", "Farg'ona", "Buxoro", "Xiva"}

# ikkalasi = ali.intersection(vali)
# uzi = ali.difference(vali)

# print("Ikalasi ham borgan shaharlar: ",ikkalasi)
# print("Uzi borgan shaharlar: ",uzi)

# 5.m
# a = input("1: ")
# b = input("2: ")
# if len(a) != len(b):
#     print(False)
# else:
#     count=0
#     for i in a:
#         if i in b:
#             count+=1
#     if count == len(a):
#         print(True)
#     else:
#         print(False)
        

# 6.m
# set1={4,5,6,7,8,9}
# set2={5,6,7,10,11}

# set3 = set1.symmetric_difference(set2)
# set4 = set1.intersection(set2)

# print(sum(set3)-sum(set4))