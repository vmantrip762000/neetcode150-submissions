class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_dict={}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1

        for iteral in t:
            if (iteral in s_dict) and s_dict[iteral] > 0:
                s_dict[iteral] -= 1

            else:
                return False
        return sum(s_dict.values()) == 0

        