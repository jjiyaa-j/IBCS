result = 1
x = 2
y = 5

while y > 0:
    if y % 2 == 0:
        y = y // 2
        x = x**2
    else:
        y = y - 1
        result *= x

print (result)
