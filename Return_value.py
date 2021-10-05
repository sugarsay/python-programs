# function with return valu
def square(argument):
    total = argument**2
    print('The squared value of',argument,'is:',total)
    return total

a = square(6) #input value
print(a)

print('+'*100)

# function with return value and multiple arguments
def addition(argument1,argument2):
    total = argument1 + argument2
    print(argument1,'+',argument2,'=',total)
    return total

def multiplication(argument1,argument2):
    total = argument1 * argument2
    print(argument1,'x',argument2,'=',total)
    return total

b = multiplication(5,addition(5,8)) #input value

print(b)