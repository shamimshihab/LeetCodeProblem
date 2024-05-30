class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        words_array= s.split()

        return  len(words_array[-1])
       

           
        

        