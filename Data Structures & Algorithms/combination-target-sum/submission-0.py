class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        def dfs(i,currSum,total):
            if total == target:
                ans.append(currSum.copy())
                return
            if i >=len(nums) or total>target:
                return
            currSum.append(nums[i])
            dfs(i, currSum, total+nums[i])
            currSum.pop()
            dfs(i+1, currSum, total)

        dfs(0,[],0)
        return ans