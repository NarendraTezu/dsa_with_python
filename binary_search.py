arr = [11,12,14,16,17,19,22,25,28,29,43,46,49,50]

def binary_search(arr,x):
    start = 0
    end = len(arr) - 1

    while(start <= end):
        mid = (start + end) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            start = mid + 1
        else:
            end = mid - 1

    return -1


res = binary_search(arr, 43)
print(f"Number is present at the index : ", res)
        

