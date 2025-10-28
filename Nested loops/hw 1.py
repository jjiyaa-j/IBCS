#1
n = 5

for row in range(n):
    for col in range(n):
        print (col + 1, end=' ')
    print ()

#2
n = 5
x = 1 
for row in range (n):
    for col in range(x,n+x): #n+x because n is a fixed value but it has to increase by 1 each time which is what the x does too so that's what it starts from element x and goes on tip n + x so that the numbers of elements in each row stay the same 
        print (col, end=' ')
    x += 1 #after it is done print 1 row in the next one it start with the next number 
    print ()

