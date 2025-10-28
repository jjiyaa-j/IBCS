year = int(input('give a year:'))
leap = False

if year % 4 == 0:
    leap = True
if year % 100 == 0:
    leap = False
if year % 400 == 0:
    leap = True

print (leap)

if (year %  4 == 0 and year % 100 != 0) or (year % 400 == 0):
    alt_leap = True
else:
    alt_leap = False

print (alt_leap)

