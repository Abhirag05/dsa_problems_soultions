class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=n-2
        while i>=0 and nums[i]>=nums[i+1]:
            i-=1
        if i>=0:
            j=n-1
            while nums[j]<=nums[i]:
                j-=1
            nums[i],nums[j]=nums[j],nums[i]
        left=i+1
        right=n-1
        while left<=right:
            nums[left],nums[right]=nums[right],nums[left]
            left+=1
            right-=1
#Approach:We will find a pivot which is the first element which is smaller than the element to its right.After that we will find the smallest element to the right of the pivot which is greater than the pivot and swap them.Finally we will reverse the subarray to the right of the pivot.
#Time complexity: O(n)
#Space complexity: O(1)