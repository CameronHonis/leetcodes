from typing import List


class Solution:
    @staticmethod
    def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) == 0:
            return Solution.get_median(nums2)
        if len(nums2) == 0:
            return Solution.get_median(nums1)
        return Solution.find_median_sorted_arrays(
            nums1, nums2, 0, len(nums1) - 1, 0, len(nums2) - 1
        )

    @staticmethod
    def find_median_sorted_arrays(
        nums1: List[int], nums2: List[int], l1: int, r1: int, l2: int, r2: int
    ) -> float:
        block1_size = r1 - l1 + 1
        block2_size = r2 - l2 + 1
        if block1_size == 1 and block2_size == 1:
            return (nums1[l1] + nums2[l2]) / 2
        if block1_size == 0:
            return Solution.get_median(nums2[l2 : r2 + 1])
        if block2_size == 0:
            return Solution.get_median(nums1[l1 : r1 + 1])

        m1_ptr_a = (r1 + l1) // 2
        m1_ptr_b = (r1 + l1 + 1) // 2
        m2_ptr_a = (r2 + l2) // 2
        m2_ptr_b = (r2 + l2 + 1) // 2
        m1 = (nums1[m1_ptr_a] + nums1[m1_ptr_b]) / 2
        m2 = (nums2[m2_ptr_a] + nums2[m2_ptr_b]) / 2

        if nums2[m2_ptr_a] <= m1 <= nums2[m2_ptr_b]:
            return m1
        if nums1[m1_ptr_a] <= m2 <= nums1[m1_ptr_b]:
            return m2

        if m1 == m2:
            return m1
        if m1 < m2:
            chop_count = min(m1_ptr_a - l1, r2 - m2_ptr_b) + 1
            new_l1 = l1 + chop_count
            new_r2 = r2 - chop_count
            return Solution.find_median_sorted_arrays(
                nums1, nums2, new_l1, r1, l2, new_r2
            )
        else:
            chop_count = min(r1 - m1_ptr_b, m2_ptr_a - l2) + 1
            new_r1 = r1 - chop_count
            new_l2 = l2 + chop_count
            return Solution.find_median_sorted_arrays(
                nums1, nums2, l1, new_r1, new_l2, r2
            )

    @staticmethod
    def get_median(nums: List[int]) -> float:
        ptr_a = (len(nums) - 1) // 2
        ptr_b = len(nums) // 2
        return (nums[ptr_a] + nums[ptr_b]) / 2


if __name__ == "__main__":
    output = Solution.findMedianSortedArrays([1, 3], [2])
    assert output == 2

    output = Solution.findMedianSortedArrays([1, 2], [3, 4])
    assert output == 2.5

    output = Solution.findMedianSortedArrays([1, 2], [-1, 3])
    assert output == 1.5

    output = Solution.findMedianSortedArrays([1,3], [2, 7])
    assert output == 2.5