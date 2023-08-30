# 15. 三数之和

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        hash_strs = []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0:
                        hash_str = [nums[i], nums[j], nums[k]]
                        hash_str.sort()
                        if hash_str not in hash_strs:
                            hash_strs.append(hash_str)
                            out.append([nums[i], nums[j], nums[k]])
        return out

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        h = 0
        # 索引h从0便利到数组长度-2
        for h in range(len(nums)-2):
            # 因为是排序数组，h处取值大于0，则和不可能等于0
            if nums[h] > 0: break
            # 如果h处取值和上一次一样，由于不应该重复，因此跳过
            if h > 0 and nums[h] == nums[h - 1]: continue
            # 索引i初始化为h后一个，索引j初始化为数组最后一个
            i, j = h+1, len(nums)-1
            # 如果i<j, 则未遍历完
            while i < j:
                # 三个数的和
                s = nums[h] + nums[i] + nums[j]

                # 如果s<0, 应该使总体增大，应该i+1
                if s < 0:
                    i += 1
                    # 如果改变i没有影响取值结果，则i继续+1
                    while i < j and nums[i] == nums[i-1]: i += 1
                # 如果s>0, 应该使总体减小，应该j-1
                elif s > 0:
                    j -= 1
                    # 如果改变j没有影响取值结果，则j继续-1
                    while i < j and nums[j] == nums[j+1]: j -= 1
                else:
                    # 如果三个数的和为0，则将三个数增加到结果中
                    out.append([nums[h], nums[i], nums[j]])
                    # 并且为了不避免重复：i+=1，j-=1
                    i += 1
                    j -= 1
                    # 如果改变i没有影响取值结果，则i继续+1
                    while i < j and nums[i] == nums[i-1]: i += 1
                    # 如果改变j没有影响取值结果，则j继续-1
                    while i < j and nums[j] == nums[j+1]: j -= 1
        return out

# 给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。请
# 你返回所有和为 0 且不重复的三元组。
# 注意：答案中不可以包含重复的三元组。

# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
# 解释：
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
# 不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
# 注意，输出的顺序和三元组的顺序并不重要。