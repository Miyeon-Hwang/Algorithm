from collections import Counter

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        cnt = 0
        count_list = Counter(nums)
        min_val = min(nums)
        max_val = max(nums) - k
        for n in range(min_val, max_val + 1):
            cnt += count_list[n] * count_list[n + k]
        return cnt
            
            
            
        