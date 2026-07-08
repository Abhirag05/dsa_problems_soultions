class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res=[]
        for num in range(left,right+1):
            valid=True
            n=num
            while n>0:
                d=n%10
                if d==0 or num%d!=0:
                    valid=False
                    break
                n//=10
            if valid:
                res.append(num)
        return res
        
#Approach:we iterate through the numbers from left to right range and for each number we take the digits and check if the number is divisible or if the digit is 0.if either of the conditions is true w emake the variable valid to false and break the loop.if the number is valid we append it to the result list and return it.

#Time complexity:O(n*m) where n is the number of integers in the range and m is the average number of digits in each integer.

#space complexity:O(n) where n is the number of integers in the range since we are storing the valid self-dividing numbers in a list.