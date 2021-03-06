# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    a = 0
    b = 0
    for i in range(elements):
        if a >= len(arrA):
            merged_arr[i] = arrB[b]
            b += 1
        elif b >= len(arrB):
            merged_arr[i] = arrA[a]
            a += 1
        elif arrA[a] < arrB[b]:
            merged_arr[i] = arrA[a]
            a += 1
        else:
            merged_arr[i] = arrB[b]
            b += 1

    return merged_arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    mid = (len(arr) - 1) // 2 + 1
    left = [x for x in arr[0:mid]]
    right = [x for x in arr[mid:]]
    if len(arr) > 2:
        left = merge_sort(left)
        right = merge_sort(right)
    
    arr = merge(left, right)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    a = start
    b = mid
    while True:
        if a >= mid or b > end:
            return
        if arr[a] <= arr[b]:
            a += 1
        else:
            smallest = arr[b]
            for i in reversed(range(a, b)):
                arr[i + 1] = arr[i]
            arr[a] = smallest
            a += 1
            b += 1
            mid += 1

def merge_sort_in_place(arr, l, r):
    mid = (l + r) // 2 + 1
    if r - l > 1:
        merge_sort_in_place(arr, l, mid - 1)
        merge_sort_in_place(arr, mid, r)
    
    merge_in_place(arr, l, mid, r)

    return arr

arr1 = [4, 3, 2, 1]
merge_sort_in_place(arr1, 0, 3)
