#classic binary search on sorted array
def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

#2.Find first and last position of an element in sorted array
def find_first_last(arr, target):
    def find(is_first):
        left, right, res = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                res = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return res

    return [find(True), find(False)]

#3.Find the peak element in a mountain array
def find_peak(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] < arr[mid + 1]:
            left = mid + 1
        else:
            right = mid
    return left
#4.Find the square root (without using math.sqrt)
def sqrt(x):
    if x < 2:
        return x
    left, right = 1, x // 2
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            left = mid + 1
            ans = mid
        else:
            right = mid - 1
    return ans

#5.Search in rotated sorted array
def search_rotated(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid

        if arr[left] <= arr[mid]:  # Left half is sorted
            if arr[left] <= target < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:  # Right half is sorted
            if arr[mid] < target <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

#6.Find the count of Target in sorted array
def count_target(arr, target):
    def find_boundary(is_first):
        left, right, res = 0, len(arr) - 1, -1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                res = mid
                if is_first:
                    right = mid - 1
                else:
                    left = mid + 1
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return res

    first = find_boundary(True)
    last = find_boundary(False)
    return last - first + 1 if first != -1 else 0

#7.Find the minimum in Rotated sorted array
def find_min_rotated(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    return arr[left]

