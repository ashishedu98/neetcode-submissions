class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        nums.sort()
        def dfs(i, currSum, total):
            if total == target:
                ans.append(currSum.copy())
                return
            if i>=len(nums) or total>target:
                return
            #include current number
            currSum.append(nums[i])
            dfs(i+1, currSum, total+nums[i])

            #dont include currNum
            currSum.pop()
            i+=1
            while i<len(nums) and nums[i]==nums[i-1]:
                i+=1
            dfs(i, currSum, total)

        dfs(0,[],0)
        return ans
