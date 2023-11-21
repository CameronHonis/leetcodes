from typing import List


class Solution:
    @staticmethod
    def trap(heights: List[int]) -> int:
        if len(heights) < 3:
            return 0
        height_incr_is: List[int] = []
        max_height = 0
        for i, height in enumerate(heights):
            if height > max_height:
                height_incr_is.append(i)
                max_height = height
        tot_water = 0
        right_max_height = 0
        for i in range(len(heights) - 1, -1, -1):
            height = heights[i]
            right_max_height = max(right_max_height, height)

            if i == height_incr_is[-1]:
                height_incr_is.pop()
                if len(height_incr_is) == 0:
                    return tot_water
                continue

            left_max_height = heights[height_incr_is[-1]]
            container_height = min(right_max_height, left_max_height)
            if height < container_height:
                tot_water += container_height - height


if __name__ == "__main__":
    output = Solution.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    assert output == 6

    output = Solution.trap([4, 2, 0, 3, 2, 5])
    assert output == 9

    output = Solution.trap([0, 1])
    assert output == 0
