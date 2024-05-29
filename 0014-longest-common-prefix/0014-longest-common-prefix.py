class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        smallest = len(strs[0])
        for i in range(1,len(strs)):
                if( len(strs[i])< smallest ):
                    smallest= len(strs[i])
        

    


        longest_prefix = ""
        for i in range(smallest):
            current_char = strs[0][i]
            for s in strs:
                if s[i] != current_char:
                    return longest_prefix
            longest_prefix += current_char

        return longest_prefix
            


            
            

        
        