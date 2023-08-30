# 283. 移动零

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        sta, end = 0, len(nums)-1
        while True:
            if sta >= end: break
            if nums[sta] == 0:
                num_sta = nums[sta]
                for i in range(sta, end):
                    nums[i] = nums[i+1]
                nums[end] = num_sta
                end -= 1
            else:
                sta += 1
        return nums
        
# 输入: nums = [0,1,0,3,12]
# 输出: [1,3,12,0,0]

# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 请注意 ，必须在不复制数组的情况下原地对数组进行操作。