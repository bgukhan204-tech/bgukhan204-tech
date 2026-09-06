# Time complexity: O(n)
# Space complexity: O(n)
class Solution(object):
    def containsDuplicate(self, nums):
        abc = set()
        for a in nums:
            if a in abc:
                return True
            else:
                abc.add(a)
        return False