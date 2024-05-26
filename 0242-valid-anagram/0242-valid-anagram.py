class Solution(object):
    def isAnagram(self, s, t):
        if len(s) != len(t):
            return False



        DicA={}
        DicB={}
        
        for i in range(len(s)):
            DicA[s[i]]= 1 + DicA.get(s[i],0) 

        for j in range(len(t)):
            DicB[t[j]] = 1 + DicB.get(t[j],0)
        
       

        for k in DicA:
            if DicA[k] != DicB.get(k,0):
                return False

            
        return True

         # print(DicA)
        # print(DicB)

     
        
      

