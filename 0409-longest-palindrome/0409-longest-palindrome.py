class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = {}
        odd_num = 0

      
        for i in s:
            dic[i] = dic.get(i, 0) + 1

        # print(dic)
        

        for j in dic:
            if dic[j] % 2 == 1:
                odd_num += 1

     
        if odd_num > 0:
            return len(s) - odd_num + 1
        else:
            return len(s)
