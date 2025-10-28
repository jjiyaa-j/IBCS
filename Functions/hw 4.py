def share (a,b):
    for i in a:
        for x in b:
            if i == x:
                return True
    else: #when it has gone through all values and then there is no match then it returns false and that is why it is under the first for loop not the second for loop
        return False

print (share([1,4,7,8], [3,2,9,6]))



