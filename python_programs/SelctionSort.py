data = [4,5,1,3,6]

def selectionsort(array):
    for i in range(len(array)):
        min_index = i

        for j in range(i+1, len(array)):
            if array[j] < array[min_index]:
                min_index = j

        #swap 2 elements
        array[i], array[min_index] = array[min_index],array[i]

print("list before sorting:")
print(data)
selectionsort(data)
print("list after sorting:")
print(data)

#Count the number of swaps performed in Selection Sort

data = [5, 3, 7, 1, 8, 6]
def selection_sort_with_swap_count(array):
    n = len(array)
    swap_count = 0

    for i in range(n):
        min_index = i

        for j in range(i + 1, n):
            if array[j] < array[min_index]:
                min_index = j

        # swap only if needed
        if min_index != i:
            array[i], array[min_index] = array[min_index], array[i]
            swap_count += 1

    return array, swap_count


print("original array:", data)
sorted_array, count = selection_sort_with_swap_count(data)
print("sorted array:", sorted_array)
print("Number of swaus:", count)

#Implement Selection Sort without modifying the original array

#Sort a list of strings using Selection Sort

#Sort only even numbers using Selection Sort (odd numbers stay at same index)



