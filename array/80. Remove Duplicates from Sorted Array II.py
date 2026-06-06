class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        if n<=2:
            return n
        k=2
        for i in range(2,n):
            if nums[i]!=nums[k-2]:
                nums[k]=nums[i]
                k+=1
        return k

#Logic: The algorithm maintains a pointer `k` to the position where the next unique element should be placed. It iterates through the array starting from index 2, and if the current element is different from the element at position `k-2`, it places the current element at position `k` and increments `k`. This ensures that at most two duplicates are allowed in the resulting array.
#time complexity: O(n) where n is the length of the input array since we are iterating through the array once.
#space complexity: O(1) since we are modifying the input array in place and not using any extra space.