class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set=set(nums)
        max_len=0
        for num in num_set:
            if num-1 not in num_set:
                length=1
                while num+length in num_set:
                    length+=1
                max_len=max(max_len,length)
        return max_len
#Approach: The code uses a set to store the unique numbers from the input list. It then iterates through each number in the set and checks if it is the start of a sequence (i.e., if the previous number is not in the set). If it is, it counts the length of the consecutive sequence starting from that number and updates the maximum length found so far. Finally, it returns the maximum length of consecutive numbers found in the input list.

#time complexity: O(n), where n is the number of elements in the input list. This is because we are iterating through the set of unique numbers and checking for consecutive sequences.

#space complexity: O(n), where n is the number of unique elements in the input list. This is because we are storing the unique numbers in a set.