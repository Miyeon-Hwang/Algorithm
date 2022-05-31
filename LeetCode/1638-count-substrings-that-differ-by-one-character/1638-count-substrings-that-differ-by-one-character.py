class Solution:
    def countSubstrings(self, s: str, t: str) -> int:
        answer = 0
        for i in range(len(s)):
            for j in range(len(t)):
                if s[i] == t[j]:
                    continue
                left = right = 0
                while min(i-left, j-left) > 0 and s[i-left-1] == t[j-left-1]:
                    left += 1
                while i+right < len(s)-1 and j+right < len(t)-1 and s[i+right+1] == t[j+right+1]:
                    right += 1
                answer += (left+1)*(right+1)
        return answer
        
        
        # 아래 풀이는 처음 풀이랑 유사하지만(loop 세번) 처음 풀이가 더 노가다식 
        # 이미 조건 충족하지 않는 substring을 포함하는 substring을 다시 idx 0 부터 확인하기 때문에
        # 시간이 더 오래 걸린거
        # answer = 0
        # for i in range(len(s)):
        #     for j in range(len(t)):
        #         length = diff = 0
        #         while i + length < len(s) and j + length < len(t) and diff <= 1:
        #             if s[i+length] != t[j+length]:
        #                 diff += 1
        #             if diff == 1:
        #                 answer += 1
        #             length += 1
        # return answer
                        
                    
                
        