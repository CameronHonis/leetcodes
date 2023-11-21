from typing import List


class Solution:
    @staticmethod
    def minPairSum(nums: List[int]) -> int:
        nums.sort()
        l = 0
        r = len(nums) - 1
        max_sum = 0
        while l < r:
            sum = nums[l] + nums[r]
            if sum > max_sum:
                max_sum = sum
            l += 1
            r -= 1
        return max_sum


if __name__ == "__main__":
    output = Solution.minPairSum([3, 5, 2, 3])
    assert output == 7

    output = Solution.minPairSum([3, 5, 4, 2, 4, 6])
    assert output == 8
