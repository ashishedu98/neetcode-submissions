class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def dfs(op, cl, seq):
            if cl == op == n:
                ans.append("".join(seq))
                return
            if op < n:
                seq.append("(")                
                dfs(op+1, cl, seq)
                seq.pop()
            if cl < op:
                seq.append(")")
                dfs(op, cl+1, seq)
                seq.pop()

        dfs(0, 0, [])
        return ans