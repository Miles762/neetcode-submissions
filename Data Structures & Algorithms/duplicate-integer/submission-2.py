class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x = len(set(nums))
        y = len(nums)

        if y-x > 0:
            return True
        return False