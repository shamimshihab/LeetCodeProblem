class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        abc = sorted(score)
        rank = 4
        hashmap= {}
        for i in range(len(abc)-1, -1, -1):
            if  i == len(abc)-1:
                hashmap[abc[i]] = "Gold Medal"
            elif i ==len(abc)-2:
                hashmap[abc[i]] = "Silver Medal"

            elif i ==len(abc)-3:
                hashmap[abc[i]] = "Bronze Medal"

            else:
                 hashmap[abc[i]] = f"{rank}"
                 rank += 1

        order = []
        for x in score:
            if x in hashmap:
                order.append(hashmap[x])

        return order

            


            
        