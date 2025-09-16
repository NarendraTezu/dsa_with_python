# rotate the the list right by k position 

nums = [1,2,3,4,5,6,7]
#function defenation reverse 
n = len(nums)
k = 3
k = k%n

def reverse(nums, low, high):
    #two pointer apporach
    while low < high:
        nums[low], nums[high] = nums[high], nums[low]
        low = low + 1
        high = high - 1

# function defination for rotate by k 
def rotate_by_k(nums , k):
    reverse(nums, 0, n-1)
    reverse(nums, 0, k-1)
    reverse(nums, k, n-1)

    return nums



#function call

result = rotate_by_k(nums, 3)

print(result)
