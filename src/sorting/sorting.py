# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):

    # Your code here
    a = 0
    b = 0
    # Store the length of the two inputs in a new variable to avoid typing out len(arr) multiple times

    len1 = len(arrA)
    len2 = len(arrB)

# This is going to be the final output list
    arr = []

    # This while loop will continue iterating until we've used up all the elements in one of the lists
    while (a < len1) and (b < len2):
        # We compare the elements at the top of each list and append whichever is smaller to our merged list
        if(arrA[a] < arrB[b]):
            arr.append(arrA[a])
            # we increment the index from the list we pulled from to prevent writing the same element
                # onto the merge list again
            a += 1
        else:
            arr.append(arrB[b])
            b += 1

    # We extend the merged list with whichever of the two lists that wasn't completed used up inside the while loop
    if a == len1:
        arr.extend(arrB[b:])
    else:
        arr.extend(arrA[a:])
    return arr

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # Your code here

     # A list with only 1 element or less, is already sorted. 
    if len(arr) <= 1:
        return arr

    # this variable is just so we don't have to type this out multiple times
        # it'll take the length of our input and divide it by 2
    l = len(arr)//2

    # Now that the list is divided in 2, we can call merge_sort recursively on each half
    arrA = merge_sort(arr[:l]) # :l so it passes in the first half of the list
    arrB = merge_sort(arr[l:]) # :l so it passes in the second half of the list

    # use our merge function from before to merge the two lists
    arr = merge(arrA, arrB)

    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass

def merge_sort_in_place(arr, l, r):
    # Your code here
    pass
