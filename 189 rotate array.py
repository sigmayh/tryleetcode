def rotate(nums,k):
    num1=nums[len(nums)-k:]
    num2=nums[:len(nums)-k]
    return (num1+num2)
    
