from typing import List


class Solution:
    @staticmethod
    def findDifferentBinaryString(nums: List[str]) -> str:
        nums.sort()
        for i in range(len(nums)):
            exp_str = bin(i)[2:]
            exp_str = f"{'0'*(len(nums) - len(exp_str))}{exp_str}"
            if nums[i] != exp_str:
                return exp_str
        bin_str = bin(len(nums))[2:]
        return f"{'0'*(len(nums) - len(bin_str))}{bin_str}"


def test_findDifferentBinaryString():
    output = Solution.findDifferentBinaryString(["01", "10"])
    assert output == "11" or output == "00"

    output = Solution.findDifferentBinaryString(["00", "01"])
    assert output == "10" or output == "11"

    output = Solution.findDifferentBinaryString(["111", "011", "001"])
    assert output == "000" or output == "010" or output == "100" or output == "101"


if __name__ == "__main__":
    test_findDifferentBinaryString()
