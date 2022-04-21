class Solution:    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numHash = {}
        for i, n in enumerate(nums):
            sub_n = target - n
            if sub_n in numHash:
                return [i, numHash[sub_n]]
            numHash[n] = i
        
        # My First solution
        # for i, n in enumerate(nums):
        #     for j in range(i + 1, len(nums)):
        #         if n + nums[j] == target:
        #             return [i, j]
                    