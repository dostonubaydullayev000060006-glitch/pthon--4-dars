import os 
os.system("cls")
# 1.m
# list= [1,2,3,4,5,6]

# for i in list:
#     if i%2==0:
#         print(0)
#     else:
#         print(1)

# 2.m
# set1 ={10,20,30,40}
# set2 = {15,20,35,40}

# set3 = set1.intersection(set2)
# a = max(set3)
# print(a)


# 3.m
# set1 = {1,2,3,4}
# set2 = {3,4,5,6,7}

# set3 = set1.intersection(set2)
# set4 = set2.symmetric_difference(set3)
# a=0

# for i in set4:
#     a+=1
# print(a)


# 4.m
# set1 = {8,3,10}
# set2 = {2,6,9}

# set3 = set1.union(set2)
# a = min(set3)
# print(a)

# 5.m
# set = {1,3,6,8,2,10}
# lst = []
# for i in set:
#     if i>=5:
#         lst.append(i)
# print(lst)


# 6.m
# set1 = {2,3,4,5,6}
# set2 = {4,5,6,7,8}

# set3 = set1.intersection(set2)

# for i in set3:
#     if i%2==0:
#         print(i,end=" ")

# 7.m
# set1 = {1,2,3,4}
# set2 = {3,4,5,6}

# set3 = set1.symmetric_difference(set2)
# a = min(set3)
# print(a)

# 8.m
# set1 = {1,2,3}
# set2 = {3,4,5}
# set3 = {5,6,7}

# set4 = set1.difference(set2).difference(set3)
# set6 = set2.difference(set3).difference(set1)
# set7 = set3.difference(set2).difference(set1)
# set8 = set4.union(set6).union(set7)
# a = sum(set8)
# print(a)


# 9.m
# set = {'olma','anor','banan','shaftoli','uzum'}
# lst = []
# for i in set:
#     if len(i)>=5:
#         lst.append(i)
# print(lst)


# 10.m
# set1 ={1,2,3}
# set2 = {4,3,6}
# set3 = set1.intersection(set2)
# if len(set3) == 0:
#     print("yoq")
# else:
#     print("bor")