class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                ans.append("FizzBuzz")
            elif i%3==0:
                ans.append("Fizz")
            elif i%5==0:
                ans.append("Buzz")
            else:
                ans.append(f"{i}")
        return ans

#Approach: Iterate through numbers from 1 to n, check divisibility by 3 and 5, and append appropriate strings to the result list.

#time complexity: O(n), where n is the input integer. The algorithm processes each number from 1 to n once.

#space complexity: O(n), where n is the input integer. The result list can grow linearly with the number of elements from 1 to n.