class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()
        def dfs(subset, itr):
            if itr >= len(nums):
                ans.add(tuple(subset))
                return
            subset.append(nums[itr])
            dfs(subset, itr+1)
            subset.pop()
            dfs(subset, itr+1)
        dfs([],0)
        return [list(x) for x in ans]