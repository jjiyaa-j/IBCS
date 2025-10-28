numbers = [7,-5,11,6]
i = 0
while i< len(numbers):
    j = i+1
    while j < len(numbers):
        if numbers [j] < numbers [i]:
            #this is the less neat way but as tuples exist in python you can straight do that instead of having a variable t to hold the values during their switch
            #t = numbers[i]
            #numbers[i] = numbers[j]
            #numbers[j] = t
            (numbers [i],numbers[j]) = (numbers[j],numbers[i])
        j = j+1
    i = i+1

print (numbers)
