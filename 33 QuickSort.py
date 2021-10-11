

def quicksort(start, end, array):
    if start < end:
        p = partition(start,end,array)
        quicksort(start,p-1,array)
        quicksort(p+1,end,array)

def partition(start,end,array):
    pivot_index = start
    pivot = array[pivot_index]

    while start < end:
        while start < len(array) and array[start] <= pivot:
            start +=1

        while array[end] > pivot:
            end -= 1

        if (start < end):
            array[start], array[end] = array[end], array[start]

    array[end], array[pivot_index] = array[pivot_index], array[end]
    return end

A = [1,9,27,30,4,6,7,27,13,11,10,20]
quicksort(0,len(A)-1,A)
print(A)




