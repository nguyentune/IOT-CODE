print("Data analyisc")

equation = 'x1 + 2 * x2 + x3'

def modify_value(x1, x2, x3):
    result = eval(equation)
    print(result)
    return result

a = 5
b = 3
c = 3
d = modify_value(a,b,c)
print(d)