class Solution:
    def reverseWords(self, s: str) -> str:
        splited_word = s.split()  
        reversed_splited_word = splited_word[::-1]
        reversed_string = " ".join(reversed_splited_word)
        return reversed_string 
      
        
        
        