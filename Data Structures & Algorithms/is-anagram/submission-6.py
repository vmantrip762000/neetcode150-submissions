class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            if i in s_dict:
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for j in t:
            if j not in s_dict or s_dict[j] == 0:
                return False            
            s_dict[j] -= 1
        return sum(s_dict.values()) == 0
        