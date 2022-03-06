# Write a program to reverse an array or string
# Input  : arr[] = {1, 2, 3}
# Output : arr{} = {3, 2, 1}

# Iterative way
# Time Complexity: O(n) 
def reverseList_iter(arr, start, end):
    while end > start:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


# Recursive way
# Time Complexity: O(n) 
def reverseList_recursive(arr, start, end):
    if start >= end:
        return
    arr[start], arr[end] = arr[end], arr[start]
    reverseList_recursive(arr, start+1, end-1)

# Python List Slicing
def reverseList_slicing(arr):
    print(arr[::-1])


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6]
    print(f"Before reverse: {arr}")
    reverseList_recursive(arr, 0, len(arr) - 1)
    print(f"After reverse: {arr}")
