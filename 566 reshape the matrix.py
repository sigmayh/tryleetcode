def reshape(nums,r,c):
    if len(nums)*len(nums[0])!=r*c:
        return nums
    else:
        l=[nums[i][j] for i in range (len[nums]) for j in range (len(nums[0]))]
        return [l[t*c:(t+1)*c] for t in range (r)]
