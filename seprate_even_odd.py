# seprate even and odd data in array

# Function defination 
def sep(arr):
    result_arr = []
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            result_arr.append(arr[i])

    for j in range(len(arr)):
        if arr[j] % 2 != 0:
            result_arr.append(arr[j])

    return result_arr


# input array

arr = [7,2,9,4,6,1,3,8,5]

# function call

result = sep(arr)
print(result)


