# Write the program to remove the number from list inplace and return count of remain number in list 

# function defination 

def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k = k + 1
    return k


# input array 

nums = [3,2,2,3]
val = 3

# function call

result = remove_element(nums, val)

print(result)
