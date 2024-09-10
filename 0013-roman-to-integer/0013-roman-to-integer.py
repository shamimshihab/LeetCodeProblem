class Solution:
    def romanToInt(self, s: str) -> int:
        h_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        result = 0

        for i in range(len(s)):

            if i+1< len(s) and h_map[s[i]]<  h_map[s[i+1]]:
                result-=  h_map[s[i]]
            else:
                result+=  h_map[s[i]]

        return result

    


        