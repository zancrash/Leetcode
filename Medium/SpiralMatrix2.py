class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        
        # init 2d nxn matrix of 0s 
        mat = [[0] * n for _ in range(n)]

        # init pointers
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1

        # init count
        c = 1

        # while left pointer has not crossed the right pointer
        while left <= right:

            # top row (left to right)
            for i in range(left, right + 1):
                mat[top][i] = c
                c += 1
            top += 1 # top row is filled, so move top pointer down

            # right col (top to bottom)
            for i in range(top, bottom + 1):
                mat[i][right] = c
                c += 1
            right -= 1 # shift right pointer left

            # bottom row (right to left)
            for i in range(right, left - 1, -1):
                mat[bottom][i] = c
                c+=1
            bottom -= 1 # shift bottom pointer up

            # left col (bottom to top)
            for i in range(bottom, top - 1, -1):
                mat[i][left] = c
                c+=1
            left += 1 # shift left pointer right

        return mat

