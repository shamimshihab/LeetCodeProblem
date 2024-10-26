class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hashMap = {}

        for i in range(len(nums)):

            if nums[i] in  hashMap:
                 hashMap[nums[i]] =   hashMap[nums[i]] + 1
            else:
                hashMap[nums[i]] = 1
        
        


        for i in hashMap :
            if hashMap[i] == 1:
                return i


            

            
        