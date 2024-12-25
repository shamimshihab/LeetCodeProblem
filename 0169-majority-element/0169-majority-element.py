class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        h ={}
        for i in nums:
            if i not in h:
                h[i] = 1
            else:
               h[i] = h[i] + 1
        
        
        
        freq =  0
        max = None

        

        for j in h:
            
            if h[j] > freq:

               
                freq= h[j]
                max = j

        

        return max

