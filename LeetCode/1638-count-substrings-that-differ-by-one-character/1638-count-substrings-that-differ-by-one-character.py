from collections import defaultdict

class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        answer = 0
        d = defaultdict(int)
        for i, c in enumerate(s):
            for j in range(i+1, len(s)+1):
                substr = s[i:j]
                if substr in d:
                    answer += d[substr]
                    continue
                for n in range(len(t) - len(substr) + 1):
                    diff_cnt = 0
                    for ti, tc in enumerate(t[n:n+len(substr)]):
                        if tc != substr[ti]:
                            diff_cnt += 1
                            if diff_cnt > 1:
                                break
                    if diff_cnt == 1:
                        d[substr] += 1
                
        print(d)
        return answer + sum(d.values())
                        
                    
                
        