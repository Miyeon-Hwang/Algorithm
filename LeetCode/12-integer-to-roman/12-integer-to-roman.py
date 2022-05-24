class Solution:
    def intToRoman(self, num: int) -> str:
        ONE = ["I", "X", "C", "M"]
        FIVE = ["V", "L", "D"]
        str_n = str(num)
        len_n = len(str_n)
        answer = ""
        for i, s in enumerate(str_n):
            cur_i = len_n - 1 - i
            n = int(s)
            if n == 5:
                answer += FIVE[cur_i]
            elif n == 4:
                answer += ONE[cur_i] + FIVE[cur_i]
            elif n == 9:
                answer += ONE[cur_i] + ONE[cur_i + 1]
            else:
                if n in [6, 7, 8]:
                    answer += FIVE[cur_i]
                answer += ONE[cur_i] * (n % 5)
        return answer
                
                
            
        
        