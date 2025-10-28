while ((a := int(input('give a number: '))) <= 0 ):
    print ('give positive interger')

while ((b := int(input('give another number: '))) <= 0 ):
    print ('give positive interger')

if a % 10 == b % 10:
    v = True
else:
    v = False
print (v)

