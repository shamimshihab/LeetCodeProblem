class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dic  = {}


        for j in  magazine:
            if j in dic:
                dic[j] = dic[j] + 1
            else:
                 dic[j] = 1

        for k in ransomNote:
            if k in dic and dic[k]>0:
                dic[k]= dic[k] -1
            else:
                return False
        return True

        


        # for i in range(len( magazine)):
        #      abc[magazine[i]] = i 

        # for j  in abc:
        #     for k in ransomNote:
        #         if k != j:
        #             continue 
        # return True 
        