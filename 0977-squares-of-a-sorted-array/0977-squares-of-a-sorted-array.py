class Solution(object):

    def sortedSquares(self, nums):
         n = len(nums)
         for i in range(0,n,1):
             nums[i] = nums[i] * nums[i]
          
             
         
         nums.sort()
         return nums
       
   
        
  
   

    # def sortedSquares(self, nums):
    #     array= []
    #     for i in nums:
    #         num = i * i
    #         print( num)
    #         array.append(num )
           
           

    #      print(array)
        
            

        
    
        
     