class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[]
        freq={}
        for i in nums1:
            freq[i]=freq.get(i,0)+1
        for i in nums2:
            if i in freq and freq[i]>0:
                result.append(i)
                freq[i]-=1
        return result

#Approach: Count the frequency of each element in the first array using a dictionary, then iterate through the second array and check if the element exists in the frequency dictionary. If it does, append it to the result list and decrement its count in the frequency dictionary.

#time complexity: O(n + m), where n is the length of nums1 and m is the length of nums2. We iterate through both arrays once.

#space complexity: O(n), where n is the length of nums1. The frequency dictionary can grow linearly with the number of unique elements in nums1.