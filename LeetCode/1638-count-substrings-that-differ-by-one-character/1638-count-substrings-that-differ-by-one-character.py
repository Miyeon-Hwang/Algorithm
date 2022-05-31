class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        answer = 0
        for i in range(len(s)):
            for j in range(len(t)):
                length = diff = 0
                while i + length < len(s) and j + length < len(t) and diff <= 1:
                    if s[i+length] != t[j+length]:
                        diff += 1
                    if diff == 1:
                        answer += 1
                    length += 1
        return answer
                        
                    
                
        