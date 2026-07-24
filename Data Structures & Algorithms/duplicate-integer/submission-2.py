class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()
        for x in nums:
            hashset.add(x)
        if len(hashset)==len(nums):
            return False
        else:
            return True

