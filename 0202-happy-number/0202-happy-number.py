class Solution:
    def isHappy(self, n: int) -> bool:
        def sumOfSquares(n):
            output = 0
            while n:
                d = n % 10
                d = d ** 2
                output += d
                n = n // 10
            return output

        setValue = set()
        

        while n not in setValue:
            # adding value in set 
            setValue.add(n)
            n = sumOfSquares(n)
            if n == 1:
                return True
        # print(setValue)
        return False





        

        
       

    


         


