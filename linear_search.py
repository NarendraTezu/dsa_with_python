def linear_search(arr,x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    else:
        return -1


arr = [11,12,22,32,13,42,35,67,88,33]
x = 22

result = linear_search(arr,x)

print(f"Searching element present at location {result}")
