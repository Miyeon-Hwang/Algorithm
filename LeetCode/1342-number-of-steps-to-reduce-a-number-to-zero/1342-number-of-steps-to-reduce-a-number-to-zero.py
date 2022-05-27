class Solution:
    def numberOfSteps(self, num: int) -> int:
        if num == 0: return 0
        answer = 0
        cur = num
        while cur > 1:
            answer += 1 if cur % 2 == 0 else 2
            cur = cur // 2
        return answer + 1
        