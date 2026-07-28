class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        result=[]
        start=nums[0]
        for i in range(1,len(nums)):
            if nums[i]!=nums[i-1]+1:
                if start==nums[i-1]:
                    result.append(str(start))
                else:
                    result.append(f"{start}->{nums[i-1]}")
                start=nums[i]
        if start==nums[-1]:
            result.append(str(nums[-1]))
        else:
            result.append(f"{start}->{nums[-1]}")
        return result
#Approach: The code iterates through the input list of numbers and identifies consecutive ranges. It keeps track of the start of each range and checks if the current number is not consecutive to the previous one. If it is not, it adds the range to the result list. Finally, it handles the last range after the loop.

#time complexity: O(n), where n is the number of elements in the input list. This is because we are iterating through the list once.

#space complexity: O(1), as we are using a constant amount of extra space for variables and the result list does not count towards space complexity since it is part of the output.