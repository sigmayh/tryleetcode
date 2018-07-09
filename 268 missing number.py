def missingnumber(nums):
    for i in range (len(nums)):
        if nums[i]!=i:
            return i
