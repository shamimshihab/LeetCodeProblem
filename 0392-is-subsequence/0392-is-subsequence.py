class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) == 0:
            return True

        i = 0

        for j in t:
            if j == s[i]:
                i = i +1
        
            if i == len(s):
                break
    

        if i == len(s) :
            return True
        else:
            False




        


        