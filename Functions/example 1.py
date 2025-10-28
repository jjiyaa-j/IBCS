#defining functions 
def abs_value (x):
    if x >= 0:
        return x
    else:
        return -x
    

print (abs_value(-50))
print (abs_value(1.44))

#distance function
def distance(a,b):
    return abs_value(a-b)

print (distance(-5,16))
