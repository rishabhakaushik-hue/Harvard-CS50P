x, y, z = input("Expression: ").split()
x_num = float(x)
z_num = float(z)
if y == "+":
    print(x_num+z_num)
elif y == "-":
    print(x_num-z_num)
elif y == "*":
    print(x_num*z_num)
elif y == "/":
    print(x_num/z_num)
