from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res: List[str] = []

        def dfs(curr: str, opened: int, balance: int) -> None:
            # if we have placed 2n characters, then it is a valid sequence
            if len(curr) == 2 * n:
                res.append(curr)
                return
            # try adding "(" if we haven't used up all n opens
            if opened < n:
                dfs(curr + "(", opened + 1, balance + 1)
            # try adding ")" for any unmatched "("
            if balance > 0:
                dfs(curr + ")", opened, balance - 1)

        dfs("", 0, 0)
        return res