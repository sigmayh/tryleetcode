def twosumII(nums,target):
    m=0
    n=0
    for i in range (len(nums)):
        for j in range (len(nums)):
            if target==(nums[i]+nums[j]):
                m=i
                n=j
                return (print('index 1 = %d , index 2 = %d' % (m,n)))
            
