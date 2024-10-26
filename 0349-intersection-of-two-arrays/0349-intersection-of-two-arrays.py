class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        found  =  set()

        for i in nums1:

            found.add(i)

        
        array = []

        for j in nums2:
            if j in found:
              
                array.append(j)
                found.remove(j)

        


        
        return array
            
        