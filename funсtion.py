
# with open('input.txt', 'r') as f:
#     lines = f.readlines()
#     string = lines[0]
#     f.close()
string = str(input())

list_str = string.split()
a = int(list_str[0])
x = int(list_str[1])
b = int(list_str[2])
c = int(list_str[3])

def quadratic_equation(a, x ,b, c):
    y = a*(x**2) +b*x +c
    return y
y = str(quadratic_equation(a, x, b, c))

print(quadratic_equation(a, x, b, c))
# with open('output.txt', 'w') as f:
#     f.write(y)
#     f.close()
# print(quadratic_equation(a, x, b, c))
