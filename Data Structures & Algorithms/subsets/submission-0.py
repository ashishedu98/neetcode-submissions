class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for x in nums:
            ans += [subset + [x] for subset in ans]

        return ans
