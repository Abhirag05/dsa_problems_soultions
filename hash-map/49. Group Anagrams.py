class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        freq={}
        for s in strs:
            sorted_word="".join(sorted(s))
            if sorted_word not in freq:
                freq[sorted_word]=[]
            freq[sorted_word].append(s)
        return list(freq.values())
      
#Approach:
#We create a hashmap where the key will be the sorted version of the word and the value will be the list of words that are anagrams of each other.

#Time Complexity:O(N * K * logK)
#Space Complexity:O(N * K)