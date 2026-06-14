class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        left=0
        right=len(lst)-1
        while left<=right:
            lst[left],lst[right]=lst[right],lst[left]
            left+=1
            right-=1
        return " ".join(lst)
    #logic: The algorithm first splits the input string into a list of words using the split() method. Then, it uses two pointers (left and right) to reverse the order of the words in the list. The left pointer starts at the beginning of the list, and the right pointer starts at the end. The algorithm swaps the words at these two pointers and then moves them towards each other until they meet or cross. Finally, it joins the reversed list of words back into a single string with spaces in between.
    #time complexity: O(n) where n is the length of the input string since we are iterating through the string to split it and then iterating through the list of words to reverse it.
    #space complexity: O(n) in the worst case if all characters in the input string are non-space characters, resulting in a list of words that takes up O(n) space. Additionally, the final output string also takes O(n) space.