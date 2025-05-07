def duplicates(nums):
    if not nums:
        return []
    unique=[nums[0]]
    for  i in range(1,len(nums)):
        if  nums[i]!=nums[i-1]:
            unique.append(nums[i])
    return  unique

nums=[1,2,2,2,3,4,5,6]
print(duplicates(nums))


    
