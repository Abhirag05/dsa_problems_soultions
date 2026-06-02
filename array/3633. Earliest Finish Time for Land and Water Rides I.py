class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        ans=float('inf')
        for i in range(len(landStartTime)):
            for j in range(len(waterStartTime)):
                land_finish=landStartTime[i]+landDuration[i]
                water_start=max(land_finish,waterStartTime[j])
                ans=min(ans,water_start+waterDuration[j])

                water_finish=waterStartTime[j]+waterDuration[j]
                land_start=max(water_finish,landStartTime[i])
                ans=min(ans,land_start+landDuration[i])
        return ans
        #Logic: We can iterate through all the possible combinations of land and water rides. For each combination, we can calculate the finish time for both the land and water rides and update the answer with the minimum finish time.
        #time complexity: O(n*m) where n is the length of landStartTime and m is the length of waterStartTime since we are iterating through all possible combinations of land and water rides.
        #space complexity: O(1) since we are not using any extra space, we are just using a variable to store the answer.