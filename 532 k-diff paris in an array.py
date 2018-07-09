def findpairs(num,k):
    ans=0
    nums=list(set(num))
    for i in range (len(nums)):
        for j in range (i,len(nums)):
            if abs(nums[i]-nums[j])==k:
                ans+=1
    return ans
