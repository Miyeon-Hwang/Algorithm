class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        def dfs(prt, cnt_opener, left_opener):
            if len(prt) == n * 2:
                answer.append(prt)
                return
            
            if left_opener > 0:
                dfs(prt + "(", cnt_opener + 1, left_opener - 1)
            if cnt_opener > 0:
                dfs(prt + ")", cnt_opener - 1, left_opener)
                    
        answer = []
        dfs("(", 1, n - 1)
        return answer
            
            
        