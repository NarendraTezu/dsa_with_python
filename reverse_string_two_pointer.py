# reverse string using two pointer

# function defination 

def reverse(arr):
    i = 0
    j = len(arr)-1
    while i<j:
        arr[i],arr[j] = arr[j],arr[i]
        i+=1
        j-=1
    return arr


#input arr

arr = [2,7,12,19,21,27,52]

# function call

result = reverse(arr)

print(result)
