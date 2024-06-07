class Solution:
    def missingNumber(self, nums: List[int]) -> int:
# using xor
     sum = 0
     n = len(nums)

    

     for i in range(len(nums)):
        print(nums[i])
        sum = sum ^ i ^ nums[i]
     sum = n ^ sum
     
     return sum
#  sorting
        # nums.sort()

        # l,r =0, len(nums)-1

        # while l<r:
        #     l+r
    

        # for i in range(len(nums)):
        #     if i != nums[i]:
            
        #         return i
        # return len(nums)
          

        