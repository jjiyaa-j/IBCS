is_prime = True
a = int(input('give a number: '))
if a < 1:
    print ('error')
for i in range (2,(a-1)):
    if a % i == 0:
        is_prime = False
        
print (is_prime)
    

