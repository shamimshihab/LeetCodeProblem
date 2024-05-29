class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:


        left = 0   

        for s in range(1, len(nums)):

            if nums[left] != nums[s]:
                left += 1
                nums[left] = nums[s]
                
        return left + 1