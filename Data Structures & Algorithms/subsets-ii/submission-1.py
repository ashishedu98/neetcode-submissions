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
            while itr+1 < len(nums) and nums[itr] == nums[itr+1]:
                itr += 1
            dfs(subset, itr+1)
        dfs([],0)
        return [list(x) for x in ans]