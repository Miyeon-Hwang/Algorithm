from collections import defaultdict

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_str = min(strs, key=len)
        if min_str == "":
            return ""
        for str in strs:
            for i, c in enumerate(str):
                if i > len(min_str) - 1:
                    break
                if c != min_str[i]:
                    min_str = min_str[:i]
                    if min_str == "":
                        return ""
                    break
        return min_str
                    
                    
                
                
        
        