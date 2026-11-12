class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current_sum = 0
        best_sum = -1 * float("inf")
        for num in nums:
            # print(current_sum, num)
            current_sum = max(current_sum + num, num)
            best_sum = max(current_sum, best_sum)
        return best_sum
