from collections import deque

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        
        target = len(nums) - 1
        jump_cnt = 0
        jump_range = 0
        cur_i = 0
        while True:
            jump_cnt += 1
            cur_max_jump = 0
            for j in range(cur_i, jump_range+1):
                cur_max_jump = max(cur_max_jump, j + nums[j])
            if cur_max_jump >= target:
                return jump_cnt
            cur_i = jump_range + 1
            jump_range = cur_max_jump
            
            
                
                
            
            

            
            
            
        