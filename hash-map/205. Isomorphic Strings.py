class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_to_t={}
        t_to_s={}
        for i in range(len(s)):
            s1=s[i]
            t1=t[i]
            if s1 in s_to_t:
                if s_to_t[s1]!=t1:
                    return False
            s_to_t[s1]=t1

            if t1 in t_to_s:
                if t_to_s[t1]!=s1:
                    return False
            t_to_s[t1]=s1
        return True
        

#Approach: we use two hash maps one for mapping characters of s to t and other for mapping characters of t to s and iterate through the s and t string and check if the characters are mapped correctly

#Time complexity:O(n) where n is the length of the s and t string

#Space complexity:O(k) where k is the number of unique characters in the s and t string and in worst case it can be O(1) because the number of possible characters is limited (e.g., 26 for lowercase English letters).