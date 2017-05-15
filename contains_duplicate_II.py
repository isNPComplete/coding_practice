# Problem: Contains Duplicate II
# (https://leetcode.com/problems/contains-duplicate-ii/#/description)

from collections import defaultdict

class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        numsToIndices = defaultdict(list)
        for index, num in enumerate(nums):
            numsToIndices[num].append(index)
            if len(numsToIndices[num]) > 1 and numsToIndices[num][-1] - numsToIndices[num][-2] <= k:
                return True
        return False
        