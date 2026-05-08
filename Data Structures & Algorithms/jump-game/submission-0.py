class Solution:
    def canJump(self, nums: List[int]) -> bool:

        safeZone = len(nums) - 1


        for i in range(len(nums)-1,-1,-1):

            if i + nums[i] >= safeZone:
                safeZone = i

        return True if safeZone == 0 else False
        