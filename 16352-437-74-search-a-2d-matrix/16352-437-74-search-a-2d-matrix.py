class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # for i in range(len(matrix)):
        #     for j in range(len(matrix[i])):
        #         if j == target:
        #             return True
        # return False


        ROW, COL = len(matrix), len(matrix[0])

        TOP, BOT = 0 , ROW - 1


        while TOP <= BOT:
            found = (TOP + BOT)//2

            if matrix[found][-1] < target:
                TOP =  found + 1

            elif matrix[found][0] > target:
                 BOT = found - 1
            
            else :
                break 

        if not (TOP <= BOT):

            return False

        found =  (TOP + BOT)//2

        l, r = 0 , COL -1

        while l <= r:

            mid = (l+r)//2

            if matrix[found][mid]>target:

                r = mid -1
            elif matrix[found][mid]<target:
                l =  mid + 1
            
            else:
                return True
        
        return False 



 

