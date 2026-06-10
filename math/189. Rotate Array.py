class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k%=len(nums)
        nums.reverse()
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])

#logic: The algorithm first calculates the effective rotation by taking the modulus of `k` with the length of the array. Then, it reverses the entire array, followed by reversing the first `k` elements and the remaining elements separately. This results in the rotated array.
#time complexity: O(n) where n is the length of the input array since we are reversing the array three times.
#space complexity: O(1) since we are modifying the input array in place and not using any extra space.