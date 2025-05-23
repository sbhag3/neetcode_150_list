class Solution(object):
    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        dp = [0 for i in range(target + 1)]
        dp[0] = 1

        for total in range(target + 1):
            for num in nums:
                if total - num >= 0:
                    dp[total] += dp[total - num]

        return dp[target]
        