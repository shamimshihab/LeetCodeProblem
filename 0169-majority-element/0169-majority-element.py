class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        dict ={}

        

        for x in nums:
            dict[x] = dict.get(x,0) + 1

        for s in dict:
           if dict.get(s) > (len(nums)/2):
            return s




        