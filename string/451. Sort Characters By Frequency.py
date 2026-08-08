class Solution:
    def frequencySort(self, s: str) -> str:
        freq={}
        new_str=""
        for i in s:
            freq[i]=freq.get(i,0)+1
        sorted_chars=sorted(freq,key=freq.get,reverse=True)
        for i in sorted_chars:
            new_str+=i*freq[i] 
        return new_str

#Approach: Count the frequency of each character in the string using a dictionary, then sort the characters based on their frequency in descending order and construct the result string.

#time complexity: O(n log n), where n is the length of the input string. The sorting step dominates the time complexity.

#space complexity: O(n), where n is the length of the input string. The frequency dictionary and the result string can grow linearly with the number of unique characters in the input string.