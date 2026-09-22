def insertion_sort(arr):
    n=len(arr)
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and arr[j]>key:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key
    return arr




print(insertion_sort([1,4,3,2,5]))

#Approach:we use the insertion sort algorithm to sort the array in-place. We iterate through the list, and for each element, we compare it with the elements before it and insert it into its correct position.

#time complexity: O(n^2), where n is the number of elements in the list. In the worst case, we may need to perform n passes through the list, and in each pass, we may need to compare and shift elements.
#space complexity: O(1), as we are sorting the list in-place and not using