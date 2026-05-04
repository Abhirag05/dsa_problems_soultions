class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=len(matrix)
        for i in range(row):
            for j in range(i+1,row):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        for i in range(row):
            matrix[i].reverse()
        
        #Logic: To rotate the matrix by 90 degrees clockwise, we can first transpose the matrix and then reverse each row. Transposing the matrix will swap the rows with columns, and reversing each row will give us the desired rotated matrix.

        #time complexity: O(n^2) since we are iterating through the matrix twice, once for transposing and once for reversing.
        
        #space complexity: O(1) since we are not using any extra space, we are just modifying the matrix in-place.