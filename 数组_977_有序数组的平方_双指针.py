# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
#  示例 1：
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100]
#
#  示例 2：
#
#
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  提示：
#  1 <= nums.length <= 10⁴
#  -10⁴ <= nums[i] <= 10⁴
#  nums 已按 非递减顺序 排序
#
#
#
#
#  进阶：
#
#
#  请你设计时间复杂度为 O(n) 的算法解决本问题
#
#
#  Related Topics 数组 双指针 排序 👍 1139 👎 0
# 数组其实是有序的， 只不过负数平方之后可能成为最大数了。
#
# 那么数组平方的最大值就在数组的两端，不是最左边就是最右边，不可能是中间。
#
# 此时可以考虑双指针法了，i指向起始位置，j指向终止位置。
#
# 定义一个新数组result，和A数组一样的大小，让k指向result数组终止位置。

# leetcode submit region begin(Prohibit modification and deletion)
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = ['' for i in range(length)]
        i = 0
        j = k = length-1
        while i <= j:
            if nums[i]*nums[i] < nums[j]*nums[j]:
                result[k] = nums[j]*nums[j]
                j = j - 1
            else:
                result[k] = nums[i]*nums[i]
                i = i + 1
            k = k - 1
        return result


# leetcode submit region end(Prohibit modification and deletion)
