from collections import Counter

class Solution:    
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        
        cnt_char = Counter(s)
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            if cnt_char[c] < k:
                max_len = max(max_len, self.longestSubstring(s[start:i], k))
                max_len = max(max_len, self.longestSubstring(s[i+1:], k))
                return max_len
        return len(s)
            