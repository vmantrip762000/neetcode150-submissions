class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        for i in s:
            s_dict[i] = 1 + s_dict.get(i, 0)
        for j in t:
            if j not in s_dict:
                return False
            if (j in s_dict) and (s_dict[j] > 0):
                s_dict[j] -= 1
        return sum(list(s_dict.values())) == 0
        