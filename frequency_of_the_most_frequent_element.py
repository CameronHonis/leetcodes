from typing import List


class Solution:
    # @staticmethod
    # def maxFrequency(nums: List[int], k: int) -> int:
    #     # brute force with a few short returns
    #     nums.sort()
    #     max_freq = 0
    #     for i, num in enumerate(nums):
    #         if i + 1 < len(nums) - 1 and nums[i+1] == nums[i]:
    #             continue
    #
    #         incrs_left = k
    #         j = i-1
    #         while j >= 0:
    #             if incrs_left < num - nums[j]:
    #                 break
    #             incrs_left -= num - nums[j]
    #             j -= 1
    #         freq = i - j
    #         max_freq = max(max_freq, freq)
    #     return max_freq

    @staticmethod
    def maxFrequency(nums: List[int], k: int) -> int:
        nums.sort()
        max_freq = 1
        l = len(nums) - 1
        r = l
        block_incrs = 0
        while l > 0 and r > 0:
            if l > r:
                l = r

            incrs_left = k - block_incrs

            if incrs_left >= nums[r] - nums[l - 1]:
                block_incrs += nums[r] - nums[l - 1]
                l -= 1
                freq = 1 + r - l
                max_freq = max(max_freq, freq)
            else:
                subject_diff = nums[r] - nums[r-1]
                block_incrs -= (r - l) * subject_diff
                r -= 1
        return max_freq


if __name__ == "__main__":
    output = Solution.maxFrequency([1, 2, 4], 5)
    assert output == 3

    output = Solution.maxFrequency([1, 4, 8, 13], 5)
    assert output == 2

    output = Solution.maxFrequency([3, 9, 6], 2)
    assert output == 1

    output = Solution.maxFrequency([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    assert output == 3
