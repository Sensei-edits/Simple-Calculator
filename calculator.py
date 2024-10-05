x = int(input("Enter Num 1 : "))
y = int(input("Enter Num 2 : "))
z = input("Choose one operator (+,-,x,%): ")

if z == '+' :
    print(x + y)
elif z == '-' :
    print(x - y)
elif z == 'x' :
    print(x * y)
elif z == '%' :
    print(x // y)
else:
    print('Error 404')