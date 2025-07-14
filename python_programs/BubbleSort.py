data = [2,1,4,5,8,6,3]

def bubblesort(array):
    for i in range(len(array)):
        for j in range(0,len(array)-i -1):

            if array[j] >array[j+1]:
                #swap 2 elements
                array[j],array[j+1] = array[j+1], array[j]
    return array

print("array before sorting:")
print(data)
print("array after sorting:")
k = bubblesort(data)
print(k)

#....................
#Sort an array using Bubble Sort




#Sort in descending order using Bubble Sort



#Count the number of swaps required to sort an array



#Sort a list of strings using Bubble Sort



#Implement Bubble Sort without modifying the original array (use a copy)


