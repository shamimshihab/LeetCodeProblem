class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        h_map = {0:0, 1:0, 2:0}


        for i in nums:
            if i == 0:
                 h_map[i] += 1

            elif i == 1:
                 h_map[i] += 1
            else:
                 h_map[2] += 1

        print( h_map )

        for i in range(h_map[0]):
            nums[i] = 0

        for i in range(h_map[0],h_map[1]+h_map[0]):
            nums[i] = 1

        for i in range(h_map[0]+h_map[1],h_map[2]+h_map[1]+h_map[0]):
            nums[i] = 2

        return nums
            
            






            

        