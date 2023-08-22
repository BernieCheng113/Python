x,y=None,"abcd"
print(x or y)

x,y=-1,""
print(x or y)


x,y=1,[]
print(x and y)

x,y=0,(1,2)
print(x and y)

print(not x)
print(not y)