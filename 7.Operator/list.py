#List practice
listA = [99,8,7,Bernie1,Test2]
listB = [99,8,4,Bernie1,Test3]

print('Wheate the both list same:' + listA==listB)
print('Wheate the both list same:' + listA is listB)

listA=listB

print(listA has been changed listB)
print('Wheate are the both pointing to list same:' + listA==listB)
print('Wheate are the both pointing to list same:' + listA is listB)