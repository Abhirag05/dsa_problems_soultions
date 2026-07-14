class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count={}
        for i in magazine:
            count[i]=count.get(i,0)+1
        for j in ransomNote:
            if j not in count or count[j]==0:
                return False
            count[j]-=1
        return True

#Approach: we use the python dictionary(hash-map) to store the frequency of each character in the magazine string and iterate through the ransomNote and checks if the character exists in the hashmap and if its exist and the frequency is not 0 we will reduce the frequency by 1 other wise we return False

#Time Complexity:O(m+n) where m is the length of the magazine and n is the length of ransom note

#Space Complexity:O(1) 