class Solution:
    def missingNumber(self, nums: List[int]) -> int:

# usimg sum of two array

        def sumNumber(number):
            m= 0
            n = 0
            for i in range(len(number)):
                m = m + number[i]
                n = n + i
            n = n + len(number)
            return [m, n]
        
        i ,j =  sumNumber(nums)
        
        return j-i 
        

      
# using xor
    #  sum = 0
    #  n = len(nums)

    

    #  for i in range(len(nums)):
    #     print(nums[i])
    #     sum = sum ^ i ^ nums[i]
    #  sum = n ^ sum
     
    #  return sum
#  sorting
        # nums.sort()

        # l,r =0, len(nums)-1

        # while l<r:
        #     l+r
    

        # for i in range(len(nums)):
        #     if i != nums[i]:
            
        #         return i
        # return len(nums)
          

        