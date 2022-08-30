class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        m=len(matrix[0])
        
        for i in range(n):
            for j in range(i):
                print(i,j)
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
                    
        print(matrix)           
                    
             
        for i in range(n):
            l=0
            r=n-1
            while l<r:
                matrix[i][l],matrix[i][r]=matrix[i][r],matrix[i][l]
                
                l+=1
                r-=1
                