while ((sun := input('is the sun shining? ')) != 'yes' and sun != 'no'):
       print ('say yes or no')

while not (0 <= (time := int(input('what is the time(0-23): '))) <= 23):
       print ('unvalid time')

if sun == 'yes' and (time >= 10 and time <= 16):
       v = 'please use sunscreen'
else:
       v = 'no need'
print (v)

