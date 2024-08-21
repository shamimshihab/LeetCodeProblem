class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row , col = len(matrix), len(matrix[0])

        top, bot = 0 , row-1

        while top<= bot:
            mid = (top+bot)//2
            if target >matrix[mid][-1]:
                top = mid +1
            elif target < matrix[mid][0]:
                bot = mid -1
            else:
                break
        if not (top<=bot):
            return False


        row_found = (top+bot)//2

        left, right = 0 , col-1

        while left<= right:
            mid = (left+right)//2

            if target > matrix[row_found][mid]:
                left = mid +1
            elif target < matrix[row_found][mid]:
                right = mid -1
            else:
                return True
        return False 


        