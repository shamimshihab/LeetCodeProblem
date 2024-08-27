class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        def search(nums, target, left_biased):
            left , right =  0 , len(nums)-1
            index = -1

            while left <= right:
                mid = (left + right) // 2

                if nums[mid] > target:
                    right =  mid -1
                
                elif nums[mid] < target:
                    left = mid + 1
                
                else:
                    index  =  mid 
                    if left_biased:
                        right = mid -1
                    else:
                        left =  mid +1
            return index


        left = search(nums, target, True)
        right = search(nums, target, False)


        return [left, right]



        
