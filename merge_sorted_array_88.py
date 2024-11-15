class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        l = m - 1
        r = n - 1
        i = n + m - 1
        while r >= 0:
            if l == -1:
                nums1[i] = nums2[r]
                r -= 1
            else:
                if nums1[l] <= nums2[r]:
                    nums1[i] = nums2[r]
                    r -= 1
                else:
                    nums1[i] = nums1[l]
                    l -= 1
            i -= 1


def test_merge():
    a1 = [1, 2, 3, 0, 0, 0]
    a2 = 3
    a3 = [2, 5, 6]
    a4 = 3
    Solution().merge(a1, a2, a3, a4)
    assert a1 == [1, 2, 2, 3, 5, 6]

    b1 = [1]
    b2 = 1
    b3 = []
    b4 = 0
    Solution().merge(b1, b2, b3, b4)
    assert b1 == [1]

    c1 = [0]
    c2 = 0
    c3 = [1]
    c4 = 1
    Solution().merge(c1, c2, c3, c4)
    assert c1 == [1]


if __name__ == "__main__":
    test_merge()
