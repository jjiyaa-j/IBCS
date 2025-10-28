N = 139
L = 3
d = N//L
z = 1
b = False
while z < L:
    d = d // L
    z = z + 1
    b = not b

if d != 0 and b:
    print (d,b)
else:
    print (z,not b)

