class Solution:
    def reverseArray(self, arr):
        # code here
        left=0
        right=len(arr)-1
        while left<=right:
            arr[left],arr[right]=arr[right],arr[left]
            left+=1
            right-=1
        return arr
        
        #logic: 
        # We use two pointers, left and right, initialized to the start and end of the array.
        # We swap the elements at the left and right pointers.
        # We increment the left pointer and decrement the right pointer.
        # We continue this process until the left pointer is greater than the right pointer.
        #Time complexity: O(n)
        #Space complexity: O(1)

