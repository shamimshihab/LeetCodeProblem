class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
      

        temp_window = 0 

        for i in range(k):
             temp_window += nums[i]
        

        max_num = temp_window

        for right in range(k,len(nums)):
      
            temp_window = temp_window + nums[right]
            temp_window = temp_window - nums[right-k]

            if temp_window> max_num:
                max_num = temp_window

        return max_num/k
            




