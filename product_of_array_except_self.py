# Write the program for find the product of the array except itself and division not to use

# function defnation 

def product_except_itself(arr):
    n = len(arr)
    ans = [0]*n
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product = product * arr[j]

        ans[i] = product
    return ans


# input array

arr = [1,2,3,4]

# function call

result = product_except_itself(arr)

print(result)





## Time complexity O(n^2)
## Space complexity O(n)


