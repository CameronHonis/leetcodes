from typing import Dict

class Solution:
    @staticmethod
    def strangePrinter(s: str) -> int:
        memo = {}

        def min_turns_to_print(start, end):
            if start > end:
                return 0

            if (start, end) in memo:
                return memo[(start, end)]

            res = min_turns_to_print(start, end - 1) + 1
            for middle in range(start, end):
                if s[middle] == s[end]:
                    res = min(
                        res,
                        min_turns_to_print(start, middle)
                        + min_turns_to_print(middle + 1, end - 1),
                    )

            memo[(start, end)] = res
            return res

        return min_turns_to_print(0, len(s) - 1)
# class Solution:
#     @staticmethod
#     def strangePrinter(s: str) -> int:
#         return Solution.strange_printer(s, 0, len(s) - 1)
#
#     @staticmethod
#     def strange_printer(s: str, start_idx: int, end_idx: int) -> int:
#         if end_idx - start_idx == 0:
#             return 1
#         (
#             block_start_idx,
#             block_end_idx,
#         ) = Solution.get_longest_block_bounds(s, start_idx, end_idx)
#         acc_turns = 1
#         if block_start_idx > start_idx:
#             acc_turns += Solution.strange_printer(s, start_idx, block_start_idx - 1)
#         if block_end_idx < end_idx:
#             acc_turns += Solution.strange_printer(s, block_end_idx + 1, end_idx)
#         # trim block 'border'
#         border_char = s[block_start_idx]
#         for _ in range(block_end_idx - block_start_idx):
#             if s[block_start_idx + 1] != border_char:
#                 break
#             block_start_idx += 1
#         if block_start_idx == block_end_idx:
#             return acc_turns
#         for _ in range(block_end_idx - block_start_idx):
#             if s[block_end_idx - 1] != border_char:
#                 break
#             block_end_idx -= 1
#         acc_turns += Solution.strange_printer(s, block_start_idx + 1, block_end_idx - 1)
#         return acc_turns
#
#     @staticmethod
#     def get_longest_block_bounds(s: str, start_idx: int, end_idx: int) -> (int, int):
#         first_idx_by_char: Dict[str, int] = {}
#         most_separated_char = s[start_idx]
#         longest_block_end_idx = start_idx
#         longest_separation = 0
#         for i in range(start_idx, end_idx + 1):
#             c = s[i]
#             if c not in first_idx_by_char:
#                 first_idx_by_char[c] = i
#             c_separation = i - first_idx_by_char[c]
#             if c_separation > longest_separation:
#                 most_separated_char = c
#                 longest_separation = c_separation
#                 longest_block_end_idx = i
#         block_start = first_idx_by_char[most_separated_char]
#         return block_start, longest_block_end_idx


def test_strangePrinter():
    # output = Solution.strangePrinter("aaabbb")
    # assert output == 2
    #
    # output = Solution.strangePrinter("aba")
    # assert output == 2
    #
    # output = Solution.strangePrinter("ababc")
    # assert output == 4
    #
    # output = Solution.strangePrinter("abacadacabae")
    # assert output == 7

    output = Solution.strangePrinter("abbbaa")
    assert output == 2


def test_longest_block_bounds_and_unique_char_count():
    start, end, count = Solution.get_longest_block_bounds("aaabbb", 0, 5)
    assert start == 0
    assert end == 2
    assert count == 2


if __name__ == "__main__":
    # test_longest_block_bounds_and_unique_char_count()
    test_strangePrinter()
