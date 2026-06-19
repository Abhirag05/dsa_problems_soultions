class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        #optimal approach
        m=len(grid)
        n=len(grid[0])
        count=0
        row=m-1
        col=0
        while row>=0 and col<n:
            if grid[row][col]<0:
                count+=n-col
                row-=1
            else:
                col+=1
        return count

#Logic:we need to start from the bottom of the grid from left to right.since it is sorted in decreasing order so if we found any negative number then all the right values will be negative and we can easily get the count without itrating the entire row.and then update the row so that we move to the upper row and if we dont found negative update the col to move to the next element.
#time complexity:O(m + n) bcs,row moves upto m and the cols moves only upto n
#Space complexity:O(1) since we are not creating any new arrays only some constant variables