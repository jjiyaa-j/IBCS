while (i := input('give equation: ')) != '':
       if '+' in i:
              x = i.split('+')
              a = float(x[0])
              b = float(x[1])
              print (a + b)
       elif '-' in i:
              x = i.split('-') 
              a = float(x[0])
              b = float(x[1])
              print (a - b)
       elif '*' in i:
              x = i.split('*')
              a = float(x[0])
              b = float(x[1])
              print (a * b)


        


       
        
        