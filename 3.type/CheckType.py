#Base View Type
x = 'PythonGood'
print(type(x))

y= 20230818
print(type(y))

z=3.5
type_name = type(z).__name__
print(type_name)

#Type Operations int
print('輸入兩個數字')
int1 = eval(input('請輸當分子的數'))
int2 = eval(input('請輸當分母的數'))

Result = int1/int2
type_name = type(Result).__name__
print('Get Type:' + type_name +'  ' + 'Val:' + str(Result))


