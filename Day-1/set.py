list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

set1 = set(list1)
set2 = set(list2)

common = set1 & set2
difference = set1 - set2

print(f"Common elements: {common}")
print(f"Elements only in list1: {difference}")