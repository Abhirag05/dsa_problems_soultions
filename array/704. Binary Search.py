class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if target==nums[mid]:
                return mid
            elif target<nums[mid]:
                right=mid-1
            else:
                left=mid+1
        return -1

#Logic:
#The search space is defined by the 'left' and 'right' pointers, initially pointing to the start and end of the array.
#In each step, we calculate the 'mid' index.
#If the target is found at 'mid', we return it.
#If the target is smaller than 'mid', we discard the right half (including 'mid') and continue searching in the left half.
#If the target is larger than 'mid', we discard the left half (including 'mid') and continue searching in the right half.
#The loop continues until the search space is exhausted (left > right), at which point the target is not found.
#Time Complexity: O(log n) because we halve the search space in each iteration.
#Space Complexity: O(1) as we only use a few extra variables.