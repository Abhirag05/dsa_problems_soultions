class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen={}
        for n in nums:
            seen[n]=seen.get(n,0)+1
        for n in nums:
            if seen[n]==1:
                return n

#Approach: The code implements a solution to find the single number in a list where every other number appears twice. It uses a dictionary to count the occurrences of each number. First, it iterates through the list and populates the dictionary with the count of each number. Then, it iterates through the list again to find and return the number that appears only once.

#time complexity: O(n), where n is the number of elements in the input list. This is because we are iterating through the list twice, but each iteration takes linear time.

#space complexity: O(n), where n is the number of unique elements in the input list. This is because we are using a dictionary to store the counts of each number, which can grow linearly with the number of unique elements.