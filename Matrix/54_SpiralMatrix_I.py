# 54: Spiral Matrix

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        res = []
        left = 0 # initial left boundry
        right = len(matrix[0]) # initial right boundry (length of horizontal (x) axis)
        top = 0 # initial top boundry
        bottom = len(matrix) #initial bottom boundry (length of vertical (y) axis)

        print('init right boundry: {} \ninit bottom boundry: {}'.format(right,bottom))

        
        while left < right and top < bottom: # While neither pointers have met each other...

            # Left to right: get every 'i' in the top row
            for i in range (left, right): # 'right' is non-inclusive
                res.append(matrix[top][i]) # append value from top row, 'i' col, to res
            top += 1 # top row is complete, so increase top boundry by 1
            print(res)

            # Top to bottom: get every 'i' in the rightmost col
            for i in range(top, bottom):
                res.append(matrix[i][right - 1]) # 'right' is non inclusive so we do 'right-1'
            right -= 1 # shift right boundry left

            if not (left < right and top < bottom): # if pointers have crossed, break loop
                break
            
            # Right to left: get every 'i' in bottom row
            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1 # shift bottom boundry up
       
            # Bottom to top: get every 'i' in leftmost col
            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1 # shift left boundry right

        return res