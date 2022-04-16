def sort_fake(nums):    
    for i in range(0,len(nums)-1):
        if nums[i]>nums[i+1]:
            a=nums[i+1]
            nums[i+1]=nums[i]
            nums[i]=a

nums=[5,-1,1,8,92,30]
print("orginal list: ")
for i in nums:
    print(i,end=" ")

sort_fake(nums)
print("\n New list:")
for i in nums:
    print(i,end=" ")