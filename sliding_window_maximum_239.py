from collections import deque
from typing import List


class Solution:
    # @staticmethod
    # def sort_with_mapping_to_original(nums: List[int]) -> List[Tuple[int, int]]:
    #     rtn = [(v, i) for i, v in enumerate(nums)]
    #     rtn.sort(reverse=True)
    #     return rtn
    #
    # @staticmethod
    # def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    #     # super slow, I know. O(n*k)
    #     rtn: List[int] = [-100000000] * (len(nums) - k + 1)
    #     sorted_mapped_pairs = Solution.sort_with_mapping_to_original(nums)
    #     for num, orig_idx in sorted_mapped_pairs:
    #         ledge_start = max(0, orig_idx - k + 1)
    #         ledge_end = min(len(rtn) - 1, orig_idx + k - 1)
    #         for i in range(ledge_start, ledge_end + 1):
    #             rtn[i] = max(rtn[i], num)
    #     return rtn

    # @staticmethod
    # def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    #     # super slow, I know O(n*k)
    #     rtn: List[int] = []
    #     for i in range(len(nums) - k + 1):
    #         max_num_in_window = max(nums[i:i + k])
    #         rtn.append(max_num_in_window)
    #     return rtn

    @staticmethod
    def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
        window = deque(maxlen=k)  # indices of nums in window, nodes flushed when values aren't ascending
        rtn: List[int] = []
        for i, num in enumerate(nums):
            while len(window) and window[-1] < i - k + 1:
                window.pop()
            while len(window) and nums[window[0]] < num:
                window.popleft()
            window.appendleft(i)
            if i + 1 >= k:
                rtn.append(nums[window[-1]])
        return rtn


def test_sort_with_mapping_to_original():
    sorted_mapped_pairs = Solution.sort_with_mapping_to_original([0, 2, 1, 4, 3])
    exp_sorted_mapped_pairs = [(4, 3), (3, 4), (2, 1), (1, 2), (0, 0)]
    for exp_pair, act_pair in zip(exp_sorted_mapped_pairs, sorted_mapped_pairs):
        assert exp_pair == act_pair


def test_max_sliding_window():
    output = Solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3)
    exp_output = [3, 3, 5, 5, 6, 7]
    assert output == exp_output

    output = Solution.maxSlidingWindow([7, 2, 4], k=2)
    exp_output = [7, 4]
    assert output == exp_output


if __name__ == "__main__":
    output = Solution.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], k=3)
