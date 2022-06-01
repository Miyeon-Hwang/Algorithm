class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        nums.sort()
        targeti = n//2
        if n % 2 == 0:
            targetn = (nums[targeti] + nums[targeti - 1]) // 2
        else:
            targetn = nums[targeti]
        answer = 0
        for i in nums:
            answer += abs(targetn - i)
        return answer
        