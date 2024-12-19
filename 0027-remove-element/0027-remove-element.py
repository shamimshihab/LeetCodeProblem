class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        poi = 0 

        for i in range(len(nums)):
            if nums[i] != val:
                nums[poi] = nums[i]
                poi +=1

        
        return poi