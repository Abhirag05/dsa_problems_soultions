class Solution:
    def search(self, arr, x):
        # code here
        for i in range(len(arr)):
            if arr[i]==x:
                return i
        return -1
    #Logic:Iterate through the array and check if the current element is equal to the target element.
    #If it is, return the index of the current element.
    #If the loop finishes without finding the target element, return -1.
    #time_complexity:O(n)
    #space_complexity:O(1)