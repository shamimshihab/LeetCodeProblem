class Solution(object):
    def reverseString(self, s):
       l = 0
       r = len(s)-1

       while l<r:
        temporary = s[l]
        s[l] = s[r]
        s[r] = temporary 
        l = l +1
        r = r -1


        