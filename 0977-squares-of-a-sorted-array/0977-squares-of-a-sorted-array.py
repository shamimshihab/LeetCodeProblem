class Solution(object):

    def sortedSquares(self, nums):
         array = []
         for i in nums:
             num = i * i
          
             array.append(num)
         
         array.sort()
         return array
       
   
        
  
   

    # def sortedSquares(self, nums):
    #     array= []
    #     for i in nums:
    #         num = i * i
    #         print( num)
    #         array.append(num )
           
           

    #      print(array)
        
            

        
    
        
     