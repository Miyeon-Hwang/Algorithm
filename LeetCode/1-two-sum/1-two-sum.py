class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        for i, n in enumerate(nums):
            sub_n = target - n
            if sub_n in numHash:
                return [i, numHash[sub_n]]
            numHash[n] = i
                    