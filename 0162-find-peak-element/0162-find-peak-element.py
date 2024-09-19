class Solution:
    def findPeakElement(self, nums: List[int]) -> int: 
        l, r = 0 , len(nums) -1

        while l<=r:

            m = l + ((r-l)//2)


            if m>0 and nums[m] < nums[m-1]:
                r = m-1

            elif m < len(nums) -1 and nums[m+1]> nums[m]:
               
                l = m+1

            else:
                return m


    








        # for i in range(len(nums)):
     
        #     if i == 0 and (len(nums) == 1 or nums[i] > nums[i+1]):
        #         return i
          
        #     if i == len(nums) - 1 and nums[i] > nums[i-1]:
        #         return i
       
        #     if i != 0 and i + 1 < len(nums) and nums[i] > nums[i-1] and nums[i] > nums[i+1]:
        #         return i

        
        