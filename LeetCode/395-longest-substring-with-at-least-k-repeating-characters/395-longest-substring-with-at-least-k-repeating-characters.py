from collections import Counter

class Solution:    
    def longestSubstring(self, s: str, k: int) -> int:
        if s == '' or len(s) < k:
            return 0
        
        cnt_char = Counter(s)
        for char, cnt in cnt_char.items():
            if cnt >= k:
                break
        else:
            return 0
                
        start = 0
        max_len = 0
        for i, c in enumerate(s):
            if cnt_char[c] >= k:
                if i == len(s) - 1:
                    max_len = max(max_len, len(s) - start)
            else:
                max_len = max(max_len, self.longestSubstring(s[start:i], k))
                max_len = max(max_len, self.longestSubstring(s[i+1:], k))
                break
        return max_len
            