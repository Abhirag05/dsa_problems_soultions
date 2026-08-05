class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left=0
        right=len(s)-1
        while left<=right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        return s

#Approach: The code implements a two-pointer technique to reverse the characters in a given string. It initializes two pointers, `left` and `right`, at the beginning and end of the string, respectively. It then iterates through the string, swapping the characters at the `left` and `right` pointers and moving both pointers inward until they meet in the middle. Finally, the modified list of characters is returned.

#time complexity: O(n), where n is the length of the input string. The algorithm processes each character in the string at most once.

#space complexity: O(1), as the algorithm modifies the input list in place and does not require any additional space proportional to the input size.