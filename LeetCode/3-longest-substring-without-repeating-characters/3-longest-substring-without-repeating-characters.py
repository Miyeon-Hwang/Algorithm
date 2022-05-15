class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        start = 0
        used_substr = {}
        for i in range(len(s)):
            if s[i] in used_substr and start <= used_substr[s[i]]:
                start = used_substr[s[i]] + 1
            else:
                max_len = max(max_len, i - start + 1)
            used_substr[s[i]] = i
        return max_len
                    