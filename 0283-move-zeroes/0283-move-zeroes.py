class Solution(object):
    def moveZeroes(self, nums):

        j = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                temporary = nums[i]

                nums[i]= nums[j]
                nums[j] = temporary
                j+=1
                
       
                
               
                
                   
               
        

      


        
       
                
        

                
        