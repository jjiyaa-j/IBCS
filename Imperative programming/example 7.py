s = int(input('please give s:'))
n = 1
found = False #False is a boolean variable, has to be a captial F

while found == False:
    if n*(n+1) / 2 > s:
        found = True
    else:
        n += 1 
print (n)

