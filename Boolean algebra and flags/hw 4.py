while ((a := int(input('give a number: '))) <= 0 ):
    print ('give positive interger')

while ((b := int(input('give another number: '))) <= 0 ):
    print ('give positive interger')

c = 0
if a>b:
    c = a
if b>a:
    c = b
for x in range(2,c+1):
    if a%x == 0 and b%x == 0:
        print(x)
        break