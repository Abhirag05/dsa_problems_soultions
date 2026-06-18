class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        count=0
        pref_len=len(pref)
        for word in words:
            if word[:pref_len]==pref:
                count+=1
        return count

#Logic:We need to count how many words start with the given prefix. For each word, we compare its first len(pref) characters with pref. If they match, we increment the count.
#Time complexity: O(n*m) where n is the number of words and m is the length of the prefix.
#Space complexity: O(1) since we are not using any extra space, we are just using a counter to count the number of words with the given prefix.