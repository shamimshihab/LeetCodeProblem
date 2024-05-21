class Solution(object):
    def twoSum(self, nums, target):
        found = {}
    
        for index, value in enumerate(nums):
                remain = target - nums[index]

                if remain in found:
                  
                    return [index, found[remain]]

                else:
                    found[value]= index
                    # print(found)
                
