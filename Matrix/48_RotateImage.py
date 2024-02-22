# 48: Rotate Image

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1

        while l < r: # while left boundry is less than right boundry
            for i in range(r - l): # from left boundry to right boundry
                # set top and bottom boundries, same as left & right as it's a square (nxn) matrix
                top = l
                bottom = r
                
                # save top-left
                topLeft = matrix[top][l + i]

                # move bottom-left into top-left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bottom-right into bottom left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                # move top right into bottom right
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft

            # after completing a 'layer', update left&right boundries
            l+=1
            r-=1

        