

while not (1 <= (weekday := int (input('what day of the week(1-7):'))) <= 7):
    print ('give valid day')

while ((vacation := input('vacation?:')) != 'yes' and vacation != 'no'):
    print ('say yes or no')

sleeps_late = weekday == 6 or weekday == 7 or vacation == 'yes'

if sleeps_late == True:
    v = True
else:
    v = False
print (v)







