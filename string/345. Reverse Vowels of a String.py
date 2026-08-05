class Solution:
    def reverseVowels(self, s: str) -> str:
        left=0
        right=len(s)-1
        vowels="aeiouAEIOU"
        s1=list(s)
        while left<=right:
            if s1[left] in vowels and s1[right] in vowels:
                s1[left],s1[right]=s1[right],s1[left]
                left+=1
                right-=1
            elif s1[left] in vowels:
                right-=1
            elif s1[right] in vowels:
                left+=1
            else:
                left+=1
                right-=1
        return "".join(s1)

#Approach: The code implements a two-pointer technique to reverse the vowels in a given string. It initializes two pointers, `left` and `right`, at the beginning and end of the string, respectively. It then iterates through the string, checking if the characters at the `left` and `right` pointers are vowels. If both are vowels, they are swapped, and both pointers are moved inward. If only one of them is a vowel, the corresponding pointer is moved inward. If neither is a vowel, both pointers are moved inward. Finally, the modified list of characters is joined back into a string and returned.

#time complexity: O(n), where n is the length of the input string. The algorithm processes each character in the string at most once.

#space complexity: O(n), where n is the length of the input string. The algorithm creates a list of characters from the input string, which requires additional space proportional to the length of the string.