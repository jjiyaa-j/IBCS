#1
def f(x):
    return 0.5*(x + (2/x))

def iterate (f,x,n):
    result = []
    value = x
    for i in range(n):
        value = f(value)
        result.append (value)
    
    return result
    
print (iterate(f,1,6))
print ()

#2
def apply_functions(fs,x):
    value = x
    for f in reversed(fs):
        value = f(value)
    return value 
    
fs = ['...'.join, str.split, str.lower]
x = "WHAT IS THIS?"

print (apply_functions(fs,x))
