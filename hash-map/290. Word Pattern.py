class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s1=s.split(' ')
        if len(s1)!=len(pattern):
            return False
        char_to_word={}
        word_to_char={}
        for i in range(len(s1)):
            c=pattern[i]
            w=s1[i]
            if c in char_to_word:
                if char_to_word[c]!=w:
                    return False
            char_to_word[c]=w

            if w in word_to_char:
                if word_to_char[w]!=c:
                    return False
            word_to_char[w]=c
        return True

#Approach:
#1. Split the string s into a list of words.
#2. Check if the length of the list of words is equal to the length of the pattern. If not, return False.
#3. Create two dictionaries: char_to_word and word_to_char to store the mapping between characters in the pattern and words in the string.
#4. Iterate through the characters in the pattern and the corresponding words in the list of words  
#5. For each character and word, check if the character is already in char_to_word. If it is, check if the corresponding word matches the current word. If not, return False.
#6. If the character is not in char_to_word, add the mapping from character to word in char_to_word.
#7. Similarly, check if the word is already in word_to_char. If it is, check if the corresponding character matches the current character. If not, return False.
#8. If the word is not in word_to_char, add the mapping from word to character in word_to_char.
#9. If all characters and words match the pattern, return True.

#Time Complexity: O(m+n), where m is the length of the pattern and n is the total number of characters in the string s.

#Space Complexity: O(n),where n is the total number of characters in the string s. This is because we are storing the mapping between characters and words in two dictionaries.