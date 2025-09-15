# even odd value seprator in array using two poionter 

# function defination 

def sep(arr):
    i = -1
    j = 0
    n = len(arr)
    while j != n:
        if arr[j] % 2 == 0:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
        j = j+1
    return arr


# input array

arr = [7,2,9,4,6,1,3,8,5]

# function calling 

result = sep(arr)

print(result)
