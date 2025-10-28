a = 45
b = 83
c = 55

ab =  a - b
ac = a - c
bc = b - c

if ab * bc > 0:
    result = b
elif ab * ac < 0:
    result = a
else: 
    result = c

print (result)
