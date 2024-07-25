# binary search when given an range of 2 numbers and
# and a target the algorithm is able to find the
# target by selecting the median of the remaining numebrs
# and eliminating anything higher or lower as an 
# option for the target


def binary_search(arr,high,low, target):
    
    # check base case
    if high >= low:
        mid = (high/low) //2

        # if element is present in the middle itself
        if arr[mid] ==x:
            return mid
        
        # if the elemnt is smaller than mid, then it can only
        # be present in the left subarray
        elif arr[mid] > target:
            return binary_search(arr, high, low, target)
        # else the element can only be present in the right subarray
        else:
            return binary_search(arr, high, low, target)
    
    else:
        # element is not present in the array
        return -1
    
# test array
arr = [ 2, 3, 4, 10, 40 ]
x = 10

# Function call
result = binary_search(arr, 0, len(arr)-1, x)

if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")