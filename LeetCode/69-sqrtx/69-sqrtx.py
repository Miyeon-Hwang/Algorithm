class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0: 
            return 0
        left = 1
        right = x
        while left < right - 1:
            mid = (left + right) // 2
            val = mid * mid
            if val > x:
                right = mid
            elif val == x:
                return mid
            else:
                left = mid
        return left
        