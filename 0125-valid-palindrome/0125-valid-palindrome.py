class Solution(object):
    def isPalindrome(self, s):
        filtered_stringe = ""
        for i in s:
            if i.isalnum():
                 print(i)
                 filtered_stringe = filtered_stringe + i.lower()
        

        left=0
        right = len(filtered_stringe)-1
        print(filtered_stringe)


        while left<right:
            if filtered_stringe[left] != filtered_stringe[right]:
                return False
            left+=1
            right-=1
        return True
            


