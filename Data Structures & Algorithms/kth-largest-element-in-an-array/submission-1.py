class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapp = []

        for i in range(len(nums)):
            heapq.heappush(heapp,-(nums[i]))

        while k>0:
            ans = heapq.heappop(heapp)
            k-=1
        return ans * -1
        
        