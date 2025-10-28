import random
n = 12
lst = random.sample(list(range(12)),n)
print (lst)
diffs = [next - prev for (prev,next) in zip(lst,lst[1:])]
print(diffs)


