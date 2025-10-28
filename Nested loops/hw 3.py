nums = [3,7,4]
m = 0
while m < len(nums):
    n = 0
    while n< len(nums):
        if m != n:
            print (10*nums[m]+nums[n])
        n += 1
    m += 1


