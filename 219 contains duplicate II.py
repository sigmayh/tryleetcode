def containduplicate(nums,k):
    m=0
    n=0
    for i in range (len(nums)):
        for j in range (i+1, len(nums)):
            if nums[i]==nums[j] and (j-i)<=k:
                return 'yes'
    return 'no'
        
