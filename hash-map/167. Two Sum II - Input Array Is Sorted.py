class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen={}
        for index,value in enumerate(numbers):
            diff=target-value
            if diff in seen:
                return[seen[diff]+1,index+1]
            seen[value]=index
        return []
    #logic: The algorithm uses a hash map (dictionary) to store the indices of the numbers as it iterates through the input array. For each number, it calculates the difference between the target and the current number. If this difference is already in the hash map, it means we have found the two numbers that add up to the target, and we return their indices (adjusted for 1-based indexing). If not, we store the current number and its index in the hash map for future reference.
    #time complexity: O(n) where n is the length of the input array since we are iterating through the array once.
    #space complexity: O(n) in the worst case if all numbers are unique and we store all of them in the hash map.