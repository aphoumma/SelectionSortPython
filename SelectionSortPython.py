# Selection sort in Python


# Function for selection sort. Takes in array and size of that array. 
def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at right spot by swapping 
        (array[step], array[min_idx]) = (array[min_idx], array[step])


# Create array 
array_sample = [29,10,14,37,16]
size = len(array_sample) 

# Print array before sorting
print('Before Sorting, the array is:')
print(array_sample)

# Call selection sort and pass in array_sample and size 
selectionSort(array_sample, size)

# Pring array after sorting 
print('After Selection Sort, the array in ascending order is:')
print(array_sample)
