n = 8 #numer of rows

for row in range (n): #row varies 0,1,..,n-1
    for col in range (row + 1):
        print (col + 1, end=' ')
    print ()

