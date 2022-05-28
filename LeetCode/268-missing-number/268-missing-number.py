class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # maxn = max(nums)
        # if len(nums) == maxn:
        #     return sum([i for i in range(maxn + 1)]) - sum(nums)
        # return len(nums)
        n = len(nums)
        return n*(n+1)//2 - sum(nums)