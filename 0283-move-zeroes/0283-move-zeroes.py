class Solution(object):
    def moveZeroes(self, nums):

        j = 0

        for i in range(len(nums)):

            if nums[i] != 0:
                temporary = nums[i]

                nums[i]= nums[j]
                nums[j] = temporary
                j+=1
            
# ts solution
# function moveZeroes(nums: number[]): void {


#     let zerod :number  =  0

#     for (let i = 0 ; i < nums.length ; i ++ ){

#         if(nums[i]!== 0 ){

#             let tempA =  nums[i]
            
#             // nums[i] = 0

#              nums[i] = nums[zerod]


#             nums[zerod] = tempA 
         

#             zerod ++


#         }



#     }


       
                
               
                
                   
               
        

      


        
       
                
        

                
        
