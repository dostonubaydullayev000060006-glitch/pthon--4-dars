import os
os.system("cls")

# set1 = {1,2,3,4,5,6,67,8,1,2,90}

# # print(set1[5])
# # set1[5] = 777
# print(set1)

# set2 = {'Olma','Anor','Gilos',"O'rk"}
# if "Anor" in set2:
#     print("Yes")
# else:
#     print("No")

 
#  SET METODLARI
# set1 = {13,32,14,25}
# set1.add(11)
# set1.add(60)
# set1.add(22)
# print(set1)

# set1 = {"olma", 'anor', 'gilos', 'banan'}
# set1.remove('anor')
# print(set1)

# set1 = {"olma", 'anor', 'gilos', 'banan'}
# n = set1.pop()
# print(n)
# print(set1)

# set1 = {"olma", 'anor', 'gilos', 'banan'}
# set1.discard('apelsin')
# print(set1)

# set1 = {"olma", 'anor', 'gilos', 'banan'}
# set1.clear()
# print(set1)

# set1 = {"olma", 'anor', 'gilos', 'banan'}
# # set2 = set1.copy()
# set2 = set1
# print(set2)

# set1 = {"olma", 'anor', 'gilos', 'banan'}
# lst = {'gilos', 'banan', 1,2,3,4}
# set1.update(lst)
# print(set1)

# set1 = {"olma", 'anor', 'gilos', 'banan'}
# lst = {'gilos', 'banan', 1,2,3,4}
# set2 = set1.union(lst)
# print(set1)
# print(set2)


# 2-METODLAR

# set1 = {'olma', 'anor', 'gilos', 'banan', 'uzum'}
# set2 = {'qovun', 'tarvuz', 'uzum', 'banan', 'olma'}

# set3 = set1.intersection(set2)
# print(set3)

# set1.intersection_update(set2)
# print(set1)

# set3 = set1.difference(set2)
# set3 = set2.difference(set1)
# print(set3)

# set1.difference_update(set2)
# print(set1)

# set3 = set1.symmetric_difference(set2)
# print(set3)

# set1.symmetric_difference_update(set2)
# print(set1)


# set1 = {1,2,3,4,5,6,7,8,9,10}
# set2 = {4,5,6}

# print(set2.issubset(set1))
# print(set1.issuperset(set2))