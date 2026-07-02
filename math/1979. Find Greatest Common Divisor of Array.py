class Solution:
    def findGCD(self, nums: List[int]) -> int:
        sm=min(nums)
        lg=max(nums)
        for div in range(sm,0,-1):
            if sm%div==0 and lg%div==0:
                return div
           
#Approach:We find the smallest and largest number int the array using the built-in functions min() and max().Then we iterate from the smallest number down to 1(since we need the greatest common divisor)and check if both the smallest and largest nummbers are divisble by the current number(div).if they are we return that number as the greatest common divisor.

#Time complexity:O(n+min(nums)) since we are iterating through the array to find the min and max using builtin functions it take O(n)and the loop run from the smallest number down to 1 which takes O(min(nums)) in the worst case.

#Space complexity:O(1) since we are using only constant space to store the smallest and largest numbers.