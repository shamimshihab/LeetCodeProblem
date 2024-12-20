



class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
    
        def find_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        
        def find_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

    
        if not nums:
            return [-1, -1]

        left_index = find_left(nums, target)
        right_index = find_right(nums, target)

      
        if left_index <= right_index and left_index < len(nums) and nums[left_index] == target:
            return [left_index, right_index]
        else:
            return [-1, -1]
        
# mine b, above cg 
  # class Solution:
#     def searchRange(self, nums: List[int], target: int) -> List[int]:

#         if len(nums) == 1:
#             if nums[0] == target:
#                 return [0,0]
#             else:
#                 return [-1,-1]

#         l,r =0, len(nums)-1

#         for i in range(len(nums)):
#             m = (l+r) //2
#             print("ddd",m)
            
#             if nums[m]>target:
#                 r= m
#             elif nums[m]<target :
#                 l= m

#             else:
#                 print("i",m)
#         arr= []
#         for j in range (l,r,1):
#             if nums[j] == target:
#                 arr.append(j)

#         if arr == []:
#             return [-1,-1]

        

#         for p in range(len(arr)):
#             l=0
#             r =len(arr)-1

#             return [arr[l],arr[r]]
