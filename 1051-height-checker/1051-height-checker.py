class Solution(object):
    def heightChecker(self, heights):
        expected = sorted(heights)
        unmatched= 0

        for i in range(len(heights)):
            if heights[i] !=expected[i]:
                unmatched = unmatched +1
        return unmatched
            

     
   