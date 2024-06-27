class Solution:
    def findLHS(self, nums: List[int]) -> int:

        max_sum = 0
        hmap ={}

        for i in nums:
            if i in hmap:
                hmap[i] = hmap[i] + 1  
            else:
                 hmap[i] = 1

        for j, count in hmap.items():

            if j+1 in hmap:
                max_sum = max(count+hmap[j+1], max_sum)

        return max_sum




                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         