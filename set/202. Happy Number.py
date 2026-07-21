class Solution:
    def isHappy(self, n: int) -> bool:
        if (n<0):
            return False
        seen=set()
        while n!=1:
            if n in seen:
                return False
            seen.add(n)
            sq=0
            while n>0:
                ld=n%10
                sq+=ld**2
                n//=10
            n=sq
        return True
#Approach:We will use to keep track of the squares and if a number repeats that means its going to be in a cycle so we will return false otherwise we will check if the square equals to 1 by updating the latest sum of squares with the given number stored in n.

#Time Complexity:O(K) Since only the small number of iterations i.e 50-100 will be encountered where k is the number of iterations.

#Space Complexity(K):Since only the small number of squares will be stored in the set.