from collections import defaultdict

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        d = defaultdict(int)
        for s in strs:
            for i in range(len(s)):
                d[s[:i+1]] += 1
        
        if "" in d:
            return ""
        
        items = list(item for item in d.items() if item[1] == len(strs))
        if not items:
            return ""
        items.sort(reverse=True, key=lambda x: len(x[0]))
        return items[0][0]
                
        
        