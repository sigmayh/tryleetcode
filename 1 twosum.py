def twosum(nums,target):
    for i in range (len(nums)):
        for j in range (len(nums)):
            if nums[i]+nums[j]==target:
                return (i,j)
    
