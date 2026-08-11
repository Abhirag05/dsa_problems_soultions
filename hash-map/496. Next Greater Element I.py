class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]
        next_greater={}
        stack=[]
        for num in nums2:
            while stack and stack[-1]<num:
                next_greater[stack.pop()]=num
            stack.append(num)
        while stack:
            next_greater[stack.pop()]=-1
        for n in nums1:
            ans.append(next_greater[n])
        return ans

#Approach: Use a stack to keep track of the next greater elements in nums2. Iterate through nums2 and for each element, pop elements from the stack until the current element is greater than the top of the stack. Store the next greater element in a dictionary. Finally, iterate through nums1 and retrieve the next greater elements from the dictionary.

#time complexity: O(n + m), where n is the length of nums1 and m is the length of nums2. We iterate through both arrays once.

#space complexity: O(m), where m is the length of nums2. The stack and the next_greater dictionary can grow linearly with the number of unique elements in nums2.