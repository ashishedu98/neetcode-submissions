class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = [] 
        char = {"2":"abc", "3":"def","4":"ghi","5":"jkl","6":"mno",
        "7":"qprs","8":"tuv","9":"wxyz"}
        def backtrack(itr, sub):
            if len(sub) == len(digits):
                res.append(sub)
                return
            for x in char[digits[itr]]:
                backtrack(itr+1, sub+x)
        if digits:
            backtrack(0,"")
        return res
            