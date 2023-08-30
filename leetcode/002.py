# 49. 字母异位词分组

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        def get_hash_str(str_alone: str) -> str:
            count = [0]*26
            for s_i in str_alone:
                count[ord(s_i)-ord('a')]+=1
            
            out_str=''
            for c_i,c in enumerate(count):
                if c > 0 :
                    # out_str += f"{chr(c_i)}{c_i}"
                    out_str += f"{chr(ord('a') + c_i)}{c}"
            return out_str

        hash_list = {}
        for strs_i in strs:
            s_hash = get_hash_str(strs_i)
            if s_hash not in hash_list:
                hash_list[s_hash] = []
            
            hash_list[s_hash].append(strs_i)

        return list(hash_list.values())

# 给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。
# 字母异位词 是由重新排列源单词的所有字母得到的一个新单词。

# 输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
# 输出: [["bat"],["nat","tan"],["ate","eat","tea"]]