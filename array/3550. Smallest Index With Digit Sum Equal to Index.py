class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        for i in range(len(nums)):
            digit_sum=0
            for digit in str(nums[i]):
                digit_sum+=int(digit)
            if digit_sum==i:
                return i
        return -1

#Approach: Iterate through the array and for each element, calculate the sum of its digits. If the sum is equal to the index, return the index. If no such index is found, return -1.

#time complexity: O(n * m), where n is the length of the array and m is the number of digits in the largest number in the array. In the worst case, we may have to check all elements and calculate their digit sums.

#space complexity: O(1), as we are using a constant amount of extra space for variables.