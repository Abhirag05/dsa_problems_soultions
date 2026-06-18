class Solution:
    def maxPrefixes(self, arr, leftIndex, rightIndex):
        # code here.
        result=[]
        for i in range(len(leftIndex)):
            l=leftIndex[i]
            r=rightIndex[i]
            prefix_sum=0
            max_sum=float('-inf')
            for j in range(l,r+1):
                prefix_sum+=arr[j]
                max_sum=max(max_sum,prefix_sum)
            result.append(max_sum)
        return result

#Logic: For each query, we iterate through the array from leftIndex[i] to rightIndex[i] and calculate the sum of the elements in that range. We maintain a variable max_sum to store the maximum sum found so far and update it if the current sum is greater than max_sum. Finally, we append max_sum to the result list.
#Time complexity: O(q*n) where q is the number of queries and n is the size of the array.
#Space complexity: O(1) since we are not using any extra space, we are just using a counter to count the number of words with the given prefix.