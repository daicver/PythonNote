# 3. 无重复字符的最长子串

# 超出时间限制
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                flag = True
                for e in s[i:j]:
                    if s[i:j].count(e) > 1: 
                         flag = False
                         break
                
                if flag == False:
                    break
                elif len(s[i:j]) > res:
                    res = len(s[i:j])

        return res
    
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 用于存储每个字母的最新位置
        dict_az = {}
        # 起始指针
        i = -1
        # 结果
        res = 0
        for j in range(len(s)):
            if s[j] in dict_az:
                # "abba" 会出现回环
                i = max(dict_az[s[j]], i)
            dict_az[s[j]] = j
            res = max(res, j-i)
        return res
    
# 给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。

# 输入: s = "abcabcbb"
# 输出: 3 
# 解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。