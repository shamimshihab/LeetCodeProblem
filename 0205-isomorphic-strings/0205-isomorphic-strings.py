class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        

        hashT1, hashT2 = {},{}


        for i in range(len(s)):
            char1 , char2  =  s[i], t[i]

            if ((char1 in hashT1 and char2 != hashT1[char1]) or (char2 in hashT2 and char1 != hashT2[char2] )   ):
                return False 


            hashT1[char1] = char2
            hashT2[char2] = char1
     
        return True
       