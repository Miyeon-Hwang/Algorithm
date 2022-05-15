from collections import Counter

class Solution:    
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        # cnt_char = Counter(s) # Counter를 여기서 구하는게 재귀돌때마다 다 구하니까 오래걸리네..
        for i, c in enumerate(s):
            if s.count(c) < k:
                #return max(self.longestSubstring(s[:i], k), self.longestSubstring(s[i+1:], k)) # 리스트 복사라 오래걸리나?
                return max(self.longestSubstring(sub, k) for sub in s.split(c))
        return len(s)
            