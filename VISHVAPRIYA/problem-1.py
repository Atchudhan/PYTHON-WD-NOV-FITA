'''nums=[2,1,3,5,6]
k=5
multiplier=2
for i in range (k):
    for num in nums:
        if num==min(nums):
           num=num*multiplier
           
           print(nums)'''





nums = [1,2]
k = 3
multiplier =4

for i in range(k):
    for j in range(len(nums)):
        if nums[j] == min(nums):
            nums[j] *= multiplier  # Update the value in the list
            break  # Exit the loop after updating the first occurrence of the minimum
    print(nums)
