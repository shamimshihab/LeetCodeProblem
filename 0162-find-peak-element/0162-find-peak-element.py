class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)):
     
            if i == 0 and (len(nums) == 1 or nums[i] > nums[i+1]):
                return i
          
            if i == len(nums) - 1 and nums[i] > nums[i-1]:
                return i
       
            if i != 0 and i + 1 < len(nums) and nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                return i

        
        