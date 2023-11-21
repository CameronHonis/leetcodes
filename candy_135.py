from typing import List

DEBUG = False
class Solution:
    # def candy(self, ratings: List[int]) -> int:
    #     acc_candy = 0
    #     last_candy = 0
    #     last_rating = -1
    #     min_candy = 1
    #     for rating in ratings:
    #         if rating > last_rating:
    #             curr_candy = last_candy + 1
    #         else:
    #             curr_candy = last_candy - 1
    #         acc_candy += curr_candy
    #         last_candy = curr_candy
    #         last_rating = rating
    #         min_candy = min(min_candy, last_candy)
    #     if min_candy < 1:
    #         acc_candy += (1 - min_candy) * len(ratings)
    #     return acc_candy

    def candy(self, ratings: List[int]) -> int:
        ratingss = Solution.divide_ratings(ratings)
        acc_candy = 0
        for ratings in ratingss:
            acc_candy += Solution.minimize_candies_for_sub_ratings(ratings)
        return acc_candy

    @staticmethod
    def minimize_candies_for_sub_ratings(ratings: List[int]) -> int:
        acc_candy = 0
        peak_idx = 0
        next_height = 1
        next_dir = -1
        _candies = []

        for rating_idx in range(len(ratings)):
            curr_height = next_height
            acc_candy += curr_height
            if DEBUG:
                _candies.append(curr_height)

            rating = ratings[rating_idx]
            curr_height = next_height
            last_dir = next_dir
            next_rating = ratings[rating_idx + 1] if rating_idx + 1 < len(ratings) else None
            if next_rating is None:
                next_dir = 1  # trigger valley logic below when reach end of downhill nodes
            else:
                next_dir = int((next_rating - rating) / abs(next_rating - rating))
            next_height += next_dir

            if last_dir != next_dir:
                if next_dir == -1:
                    # switching to downhill from peak
                    peak_idx = rating_idx

                else:
                    # switch to uphill from valley
                    if curr_height > 1:
                        nodes_to_shift_count = rating_idx - peak_idx
                    else:
                        # valley under the minimum candies
                        nodes_to_shift_count = rating_idx - peak_idx + 1
                    height_diff = 1 - curr_height
                    acc_candy += nodes_to_shift_count * height_diff
                    if DEBUG:
                        for _candy_idx in range(len(_candies)-nodes_to_shift_count, len(_candies)):
                            _candies[_candy_idx] += height_diff

                    next_height += height_diff
        if DEBUG:
            print(f"\n{ratings} -> {_candies}")
        return acc_candy

    @staticmethod
    def divide_ratings(ratings: List[int]) -> List[List[int]]:
        split_ratings = []
        _split_anchor = 0
        for rating_idx in range(1, len(ratings)):
            rating = ratings[rating_idx]
            last_rating = ratings[rating_idx - 1]
            if rating == last_rating:
                split_ratings.append(ratings[_split_anchor:rating_idx])
                _split_anchor = rating_idx
        split_ratings.append(ratings[_split_anchor:])
        return split_ratings


def test_candy():
    assert isinstance(Solution().candy([1, 3, 2, 2, 1]), int)
    assert Solution().candy([1, 3, 2, 2, 1]) == 7
    assert Solution().candy([1, 2, 2]) == 4
    assert Solution().candy([2, 2, 1]) == 4
    assert Solution().candy([4, 4, 4, 4]) == 4
    assert Solution().candy([1, 3, 4, 5, 2]) == 11


def test_minimize_candies_for_sub_ratings():
    assert Solution().minimize_candies_for_sub_ratings([1, 3, 2]) == 4
    assert Solution().minimize_candies_for_sub_ratings([2, 1]) == 3


def test_divide_ratings():
    divided_ratings = Solution().divide_ratings([1, 3, 2, 2, 1])
    assert len(divided_ratings) == 2
    assert len(divided_ratings[0]) == 3
    assert len(divided_ratings[1]) == 2

    divided_ratings = Solution().divide_ratings([1, 2, 2])
    assert len(divided_ratings) == 2
    assert len(divided_ratings[0]) == 2
    assert len(divided_ratings[1]) == 1

    divided_ratings = Solution().divide_ratings([2, 2, 1])
    assert len(divided_ratings) == 2
    assert len(divided_ratings[0]) == 1
    assert len(divided_ratings[1]) == 2

    divided_ratings = Solution().divide_ratings([4, 4, 4, 4])
    assert len(divided_ratings) == 4
    assert len(divided_ratings[0]) == 1
    assert len(divided_ratings[1]) == 1
    assert len(divided_ratings[2]) == 1
    assert len(divided_ratings[3]) == 1
