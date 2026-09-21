class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        for i in range(n):
            for j in range(0,n-1-i):
                if nums[j]>nums[j+1]:
                    nums[j],nums[j+1]=nums[j+1],nums[j]

#Approach:we can use bubble sort algorithm to sort the colors in-place. We iterate through the list multiple times, comparing adjacent elements and swapping them if they are in the wrong order. This process continues until the entire list is sorted.

#time complexity: O(n^2), where n is the number of elements in the list. In the worst case, we may need to perform n passes through the list, and in each pass, we may need to compare and swap adjacent elements.
#space complexity: O(1), as we are sorting the list in-place and not using any additional data structures.