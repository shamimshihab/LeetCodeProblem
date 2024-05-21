class Solution(object):
    def containsDuplicate(self, nums):
        uset = set()
        for id in nums:

            if id in uset:
                return True
            else:
                uset.add(id)
        return False
        