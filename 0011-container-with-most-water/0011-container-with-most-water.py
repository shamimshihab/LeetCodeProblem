class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        left = 0
        right = len(height) -1
      

        while left <  right:
            k =  min(height[left],  height[right]) * (right-left)
            if k> max :
                max = k

            if height[left] < height[right]:
                left = left + 1 
            
            else:
                right = right-1
        return max







        